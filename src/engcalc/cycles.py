"""Thermodynamic cycle efficiency calculations.

Reference: Cengel & Boles, "Thermodynamics: An Engineering Approach"
All temperatures must be in Kelvin (K).
Efficiency is returned as a fraction between 0 and 1 (multiply by 100 for %).
"""


def carnot_efficiency(T_hot: float, T_cold: float) -> float:
    """Carnot cycle thermal efficiency.

    The Carnot cycle is the most efficient cycle operating between
    two thermal reservoirs.

    Formula:
        eta = 1 - T_cold / T_hot

    Args:
        T_hot: Hot reservoir temperature in Kelvin (K).
        T_cold: Cold reservoir temperature in Kelvin (K).

    Returns:
        Thermal efficiency as a fraction (0 to 1).

    Raises:
        ValueError: If T_hot <= T_cold or T_hot <= 0.

    Example:
        >>> carnot_efficiency(T_hot=800, T_cold=300)
        0.625
    """
    if T_hot <= 0:
        raise ValueError("T_hot must be positive (Kelvin).")
    if T_cold <= 0:
        raise ValueError("T_cold must be positive (Kelvin).")
    if T_hot <= T_cold:
        raise ValueError("T_hot must be greater than T_cold.")

    return 1 - (T_cold / T_hot)


def otto_efficiency(compression_ratio: float, gamma: float = 1.4) -> float:
    """Otto cycle thermal efficiency (petrol engine).

    Formula:
        eta = 1 - 1 / r^(gamma - 1)

    where:
        r = compression ratio (V1/V2)
        gamma = specific heat ratio (Cp/Cv), default 1.4 for air

    Args:
        compression_ratio: Compression ratio r (> 1).
        gamma: Specific heat ratio, default 1.4 for air.

    Returns:
        Thermal efficiency as a fraction (0 to 1).

    Raises:
        ValueError: If compression_ratio <= 1 or gamma <= 1.

    Example:
        >>> otto_efficiency(compression_ratio=8)
        0.5647...
    """
    if compression_ratio <= 1:
        raise ValueError("Compression ratio must be greater than 1.")
    if gamma <= 1:
        raise ValueError("Gamma must be greater than 1.")

    return 1 - 1 / (compression_ratio ** (gamma - 1))


def diesel_efficiency(
    compression_ratio: float,
    cutoff_ratio: float,
    gamma: float = 1.4,
) -> float:
    """Diesel cycle thermal efficiency.

    Formula:
        eta = 1 - (1 / r^(gamma-1)) * (rc^gamma - 1) / (gamma * (rc - 1))

    where:
        r = compression ratio
        rc = cutoff ratio (V3/V2)
        gamma = specific heat ratio

    Args:
        compression_ratio: Compression ratio r (> 1).
        cutoff_ratio: Cutoff ratio rc (> 1).
        gamma: Specific heat ratio, default 1.4 for air.

    Returns:
        Thermal efficiency as a fraction (0 to 1).

    Raises:
        ValueError: If inputs are out of valid range.

    Example:
        >>> diesel_efficiency(compression_ratio=18, cutoff_ratio=2)
        0.631...
    """
    if compression_ratio <= 1:
        raise ValueError("Compression ratio must be greater than 1.")
    if cutoff_ratio <= 1:
        raise ValueError("Cutoff ratio must be greater than 1.")
    if gamma <= 1:
        raise ValueError("Gamma must be greater than 1.")

    r = compression_ratio
    rc = cutoff_ratio

    term1 = 1 / (r ** (gamma - 1))
    term2 = (rc**gamma - 1) / (gamma * (rc - 1))

    return 1 - term1 * term2


def brayton_efficiency(pressure_ratio: float, gamma: float = 1.4) -> float:
    """Brayton cycle thermal efficiency (gas turbine).

    Formula:
        eta = 1 - 1 / rp^((gamma-1)/gamma)

    where:
        rp = pressure ratio (P2/P1)

    Args:
        pressure_ratio: Pressure ratio rp (> 1).
        gamma: Specific heat ratio, default 1.4 for air.

    Returns:
        Thermal efficiency as a fraction (0 to 1).

    Raises:
        ValueError: If inputs are out of valid range.

    Example:
        >>> brayton_efficiency(pressure_ratio=10)
        0.482...
    """
    if pressure_ratio <= 1:
        raise ValueError("Pressure ratio must be greater than 1.")
    if gamma <= 1:
        raise ValueError("Gamma must be greater than 1.")

    return 1 - 1 / (pressure_ratio ** ((gamma - 1) / gamma))