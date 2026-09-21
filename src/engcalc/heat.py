"""Heat transfer calculations.

Reference: Incropera et al., "Fundamentals of Heat and Mass Transfer"
All values in SI units.
"""


def conduction_rate(
    k: float,
    A: float,
    dT: float,
    L: float,
) -> float:
    """Fourier's law of conduction through a plane wall.

    Formula:
        Q = k * A * dT / L

    Args:
        k: Thermal conductivity (W/(m·K)).
        A: Cross-sectional area (m^2).
        dT: Temperature difference (K).
        L: Wall thickness (m).

    Returns:
        Heat transfer rate (W).

    Raises:
        ValueError: If L <= 0 or k < 0 or A < 0.

    Example:
        >>> conduction_rate(k=50, A=2, dT=100, L=0.1)
        100000.0
    """
    if L <= 0:
        raise ValueError("Thickness L must be positive.")
    if k < 0 or A < 0:
        raise ValueError("k and A must be non-negative.")
    return k * A * dT / L


def convection_rate(
    h: float,
    A: float,
    T_surface: float,
    T_fluid: float,
) -> float:
    """Newton's law of cooling for convection.

    Formula:
        Q = h * A * (T_surface - T_fluid)

    Args:
        h: Convective heat transfer coefficient (W/(m^2·K)).
        A: Surface area (m^2).
        T_surface: Surface temperature (K or °C).
        T_fluid: Fluid temperature (K or °C).

    Returns:
        Heat transfer rate (W).

    Raises:
        ValueError: If h < 0 or A < 0.

    Example:
        >>> convection_rate(h=25, A=2, T_surface=350, T_fluid=300)
        2500.0
    """
    if h < 0 or A < 0:
        raise ValueError("h and A must be non-negative.")
    return h * A * (T_surface - T_fluid)


def radiation_rate(
    emissivity: float,
    A: float,
    T_surface: float,
    T_surroundings: float,
    sigma: float = 5.67e-8,
) -> float:
    """Stefan-Boltzmann law for radiation heat transfer.

    Formula:
        Q = emissivity * sigma * A * (T_surface^4 - T_surroundings^4)

    Args:
        emissivity: Surface emissivity (0 to 1).
        A: Surface area (m^2).
        T_surface: Surface temperature (K).
        T_surroundings: Surrounding temperature (K).
        sigma: Stefan-Boltzmann constant (W/(m^2·K^4)), default 5.67e-8.

    Returns:
        Net radiation heat transfer rate (W).

    Raises:
        ValueError: If emissivity not in [0, 1], or temperatures negative.

    Example:
        >>> radiation_rate(emissivity=0.9, A=1, T_surface=500, T_surroundings=300)
        2892.9...
    """
    if not (0 <= emissivity <= 1):
        raise ValueError("Emissivity must be between 0 and 1.")
    if T_surface < 0 or T_surroundings < 0:
        raise ValueError("Temperatures must be non-negative (Kelvin).")
    return emissivity * sigma * A * (T_surface**4 - T_surroundings**4)


def lmtd(
    T_hot_in: float,
    T_hot_out: float,
    T_cold_in: float,
    T_cold_out: float,
) -> float:
    """Log Mean Temperature Difference for heat exchangers.

    Formula:
        dT1 = T_hot_in - T_cold_out
        dT2 = T_hot_out - T_cold_in
        LMTD = (dT1 - dT2) / ln(dT1 / dT2)

    If dT1 ≈ dT2, returns dT1 (limit case).

    Args:
        T_hot_in: Hot fluid inlet temperature.
        T_hot_out: Hot fluid outlet temperature.
        T_cold_in: Cold fluid inlet temperature.
        T_cold_out: Cold fluid outlet temperature.

    Returns:
        LMTD in same units as inputs.

    Raises:
        ValueError: If dT1 <= 0 or dT2 <= 0 (invalid exchanger).

    Example:
        >>> lmtd(T_hot_in=400, T_hot_out=350, T_cold_in=300, T_cold_out=330)
        59.44...
    """
    dT1 = T_hot_in - T_cold_out
    dT2 = T_hot_out - T_cold_in

    if dT1 <= 0 or dT2 <= 0:
        raise ValueError("Temperature differences must be positive.")

    # Handle equal case (limit)
    if abs(dT1 - dT2) < 1e-9:
        return dT1

    import math
    return (dT1 - dT2) / math.log(dT1 / dT2)