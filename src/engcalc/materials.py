"""Material property database for engineering calculations.

Data is loaded from a bundled JSON file. Properties are typical
textbook values — verify against manufacturer datasheets before
critical design use.

All values in SI units:
    density             : kg/m^3
    youngs_modulus      : Pa
    poisson_ratio       : dimensionless
    thermal_conductivity: W/(m·K)
    specific_heat       : J/(kg·K)
    thermal_expansion   : 1/K
    yield_strength      : Pa
    ultimate_strength   : Pa
"""

import json
from pathlib import Path
from typing import Any

# Load material data once at import time
_DATA_FILE = Path(__file__).parent / "data" / "materials.json"

with open(_DATA_FILE, encoding="utf-8") as f:
    _MATERIALS: dict[str, dict[str, Any]] = json.load(f)


def list_materials() -> list[str]:
    """Return a sorted list of all available material keys.

    Returns:
        List of material IDs.

    Example:
        >>> "steel_AISI_1040" in list_materials()
        True
    """
    return sorted(_MATERIALS.keys())


def get(material: str, property_name: str) -> float:
    """Get a single property of a material.

    Args:
        material: Material key (see list_materials()).
        property_name: Property name, e.g. "density", "youngs_modulus".

    Returns:
        Property value in SI units.

    Raises:
        KeyError: If material or property does not exist.
        ValueError: If property value is None (not available).

    Example:
        >>> get("steel_AISI_1040", "density")
        7850
    """
    if material not in _MATERIALS:
        raise KeyError(
            f"Unknown material: '{material}'. "
            f"Use list_materials() to see available options."
        )

    props = _MATERIALS[material]

    if property_name not in props:
        raise KeyError(
            f"Material '{material}' has no property '{property_name}'. "
            f"Available: {sorted(props.keys())}"
        )

    value = props[property_name]

    if value is None:
        raise ValueError(
            f"Property '{property_name}' is not available for '{material}'."
        )

    return value


def get_all(material: str) -> dict[str, Any]:
    """Get all properties of a material as a dictionary.

    Args:
        material: Material key.

    Returns:
        Dictionary of all properties.

    Raises:
        KeyError: If material does not exist.

    Example:
        >>> props = get_all("aluminum_6061_T6")
        >>> props["density"]
        2700
    """
    if material not in _MATERIALS:
        raise KeyError(f"Unknown material: '{material}'.")

    return dict(_MATERIALS[material])


def search(category: str) -> list[str]:
    """Find all materials in a given category.

    Args:
        category: Category name, e.g. "steel", "aluminum".

    Returns:
        List of material keys in that category.

    Example:
        >>> search("aluminum")
        ['aluminum_6061_T6', 'aluminum_7075_T6']
    """
    return sorted(
        key for key, props in _MATERIALS.items()
        if props.get("category") == category
    )


def list_categories() -> list[str]:
    """Return a sorted list of all unique material categories.

    Example:
        >>> "steel" in list_categories()
        True
    """
    return sorted({props["category"] for props in _MATERIALS.values()})