"""Unit conversion utilities for engineering calculations.

A pure-Python alternative to heavier libraries like `pint`, focused on
the units most commonly used in Mechanical Engineering.

Most categories work by defining a linear factor to a base unit:
    value_in_base = value * factor

Temperature is special (has an offset), so it uses its own logic.

Example:
    >>> from engcalc import units
    >>> units.convert(100, "cm", "m")
    1.0
    >>> units.convert(1, "atm", "psi")
    14.695948775513449
    >>> units.convert(100, "degC", "K")
    373.15
"""

# ---------------------------------------------------------------------------
# Linear conversion tables
# Each category's first entry is the base unit with factor 1.0.
# factor = how many base units in one of this unit
# ---------------------------------------------------------------------------

_LINEAR_UNITS: dict[str, dict[str, float]] = {
    "length": {
        "m": 1.0,
        "mm": 1e-3,
        "cm": 1e-2,
        "km": 1e3,
        "in": 0.0254,
        "ft": 0.3048,
        "yd": 0.9144,
        "mile": 1609.344,
    },
    "mass": {
        "kg": 1.0,
        "g": 1e-3,
        "mg": 1e-6,
        "lb": 0.45359237,
        "oz": 0.028349523125,
        "ton": 1000.0,
    },
    "time": {
        "s": 1.0,
        "ms": 1e-3,
        "us": 1e-6,
        "min": 60.0,
        "h": 3600.0,
        "day": 86400.0,
    },
    "pressure": {
        "Pa": 1.0,
        "kPa": 1e3,
        "MPa": 1e6,
        "bar": 1e5,
        "atm": 101325.0,
        "psi": 6894.757293168361,
        "mmHg": 133.322387415,
        "torr": 133.322368421,
    },
    "energy": {
        "J": 1.0,
        "kJ": 1e3,
        "MJ": 1e6,
        "cal": 4.184,
        "kcal": 4184.0,
        "BTU": 1055.05585262,
        "kWh": 3.6e6,
        "eV": 1.602176634e-19,
    },
    "power": {
        "W": 1.0,
        "kW": 1e3,
        "MW": 1e6,
        "hp": 745.6998715822702,
        "BTU/h": 0.2930710701722222,
    },
    "force": {
        "N": 1.0,
        "kN": 1e3,
        "lbf": 4.4482216152605,
        "kgf": 9.80665,
        "dyne": 1e-5,
    },
    "area": {
        "m^2": 1.0,
        "mm^2": 1e-6,
        "cm^2": 1e-4,
        "km^2": 1e6,
        "in^2": 0.00064516,
        "ft^2": 0.09290304,
        "acre": 4046.8564224,
    },
    "volume": {
        "m^3": 1.0,
        "L": 1e-3,
        "mL": 1e-6,
        "cm^3": 1e-6,
        "in^3": 1.6387064e-5,
        "ft^3": 0.028316846592,
        "gal_US": 3.785411784e-3,
    },
    "velocity": {
        "m/s": 1.0,
        "km/h": 1.0 / 3.6,
        "mph": 0.44704,
        "ft/s": 0.3048,
        "knot": 0.5144444444444444,
    },
    "angle": {
        "rad": 1.0,
        "deg": 3.141592653589793 / 180.0,
        "grad": 3.141592653589793 / 200.0,
        "turn": 2.0 * 3.141592653589793,
    },
}

_TEMPERATURE_UNITS = ("K", "degC", "degF", "degR")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _find_category(unit: str) -> str:
    """Find which category a unit belongs to. Raises KeyError if not found."""
    if unit in _TEMPERATURE_UNITS:
        return "temperature"
    for category, table in _LINEAR_UNITS.items():
        if unit in table:
            return category
    raise KeyError(f"Unknown unit: '{unit}'.")


def _to_kelvin(value: float, unit: str) -> float:
    """Convert a temperature value to Kelvin."""
    if unit == "K":
        return value
    if unit == "degC":
        return value + 273.15
    if unit == "degF":
        return (value - 32.0) * 5.0 / 9.0 + 273.15
    if unit == "degR":
        return value * 5.0 / 9.0
    raise KeyError(f"Unknown temperature unit: '{unit}'.")


def _from_kelvin(value: float, unit: str) -> float:
    """Convert a Kelvin value to another temperature unit."""
    if unit == "K":
        return value
    if unit == "degC":
        return value - 273.15
    if unit == "degF":
        return (value - 273.15) * 9.0 / 5.0 + 32.0
    if unit == "degR":
        return value * 9.0 / 5.0
    raise KeyError(f"Unknown temperature unit: '{unit}'.")


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def convert(value: float, from_unit: str, to_unit: str) -> float:
    """Convert a value from one unit to another.

    Args:
        value: Numeric value to convert.
        from_unit: Source unit symbol.
        to_unit: Target unit symbol.

    Returns:
        Converted value.

    Raises:
        KeyError: If either unit is unknown.
        ValueError: If the two units belong to different categories.

    Example:
        >>> convert(100, "cm", "m")
        1.0
        >>> convert(100, "degC", "K")
        373.15
        >>> convert(1, "atm", "psi")
        14.695948775513449
    """
    cat_from = _find_category(from_unit)
    cat_to = _find_category(to_unit)

    if cat_from != cat_to:
        raise ValueError(
            f"Cannot convert between '{from_unit}' ({cat_from}) and "
            f"'{to_unit}' ({cat_to})."
        )

    if cat_from == "temperature":
        return _from_kelvin(_to_kelvin(value, from_unit), to_unit)

    factor_from = _LINEAR_UNITS[cat_from][from_unit]
    factor_to = _LINEAR_UNITS[cat_from][to_unit]
    return value * factor_from / factor_to


def list_categories() -> list[str]:
    """Return a sorted list of all supported unit categories.

    Example:
        >>> "length" in list_categories()
        True
    """
    return sorted(list(_LINEAR_UNITS.keys()) + ["temperature"])


def list_units(category: str) -> list[str]:
    """Return all units in a given category.

    Args:
        category: Category name (see list_categories()).

    Returns:
        List of unit symbols.

    Raises:
        KeyError: If category is unknown.

    Example:
        >>> "m" in list_units("length")
        True
        >>> "degC" in list_units("temperature")
        True
    """
    if category == "temperature":
        return list(_TEMPERATURE_UNITS)
    if category not in _LINEAR_UNITS:
        raise KeyError(
            f"Unknown category: '{category}'. "
            f"Available: {list_categories()}"
        )
    return list(_LINEAR_UNITS[category].keys())


def find_category(unit: str) -> str:
    """Return the category of a given unit.

    Example:
        >>> find_category("psi")
        'pressure'
    """
    return _find_category(unit)