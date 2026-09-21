"""Ideal gas law calculations.

The ideal gas law: PV = nRT
where:
    P = pressure (Pa)
    V = volume (m^3)
    n = amount of substance (mol)
    R = universal gas constant (8.314 J/(mol·K))
    T = absolute temperature (K)
"""

# Universal gas constant in SI units: J/(mol·K)
R = 8.314462618


def pressure(n: float, T: float, V: float) -> float:
    """Calculate pressure using ideal gas law: P = nRT/V.

    Args:
        n: Amount of substance in moles (mol).
        T: Absolute temperature in Kelvin (K).
        V: Volume in cubic meters (m^3).

    Returns:
        Pressure in Pascals (Pa).

    Raises:
        ValueError: If V is zero or negative.

    Example:
        >>> pressure(n=1, T=300, V=0.024)
        103930.782725
    """
    if V <= 0:
        raise ValueError("Volume must be positive.")
    return (n * R * T) / V