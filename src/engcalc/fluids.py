"""Fluid mechanics calculations.

Reference: Munson et al., "Fundamentals of Fluid Mechanics"
All values in SI units unless stated otherwise.
"""

import math


def reynolds_number(
    rho: float,
    velocity: float,
    diameter: float,
    mu: float,
) -> float:
    """Reynolds number for pipe flow.

    Formula:
        Re = (rho * v * D) / mu

    Args:
        rho: Fluid density (kg/m^3).
        velocity: Flow velocity (m/s).
        diameter: Pipe inner diameter (m).
        mu: Dynamic viscosity (Pa·s).

    Returns:
        Reynolds number (dimensionless).

    Raises:
        ValueError: If mu <= 0 or any input is negative.

    Example:
        >>> reynolds_number(rho=1000, velocity=2, diameter=0.05, mu=0.001)
        100000.0
    """
    if rho < 0 or velocity < 0 or diameter < 0:
        raise ValueError("rho, velocity, diameter must be non-negative.")
    if mu <= 0:
        raise ValueError("Dynamic viscosity must be positive.")
    return (rho * velocity * diameter) / mu


def flow_regime(Re: float) -> str:
    """Classify flow regime based on Reynolds number.

    Args:
        Re: Reynolds number.

    Returns:
        "laminar" (Re < 2300), "transitional" (2300 ≤ Re < 4000),
        or "turbulent" (Re ≥ 4000).

    Example:
        >>> flow_regime(1500)
        'laminar'
        >>> flow_regime(5000)
        'turbulent'
    """
    if Re < 2300:
        return "laminar"
    elif Re < 4000:
        return "transitional"
    else:
        return "turbulent"


def bernoulli_pressure(
    P1: float,
    v1: float,
    h1: float,
    v2: float,
    h2: float,
    rho: float,
    g: float = 9.81,
) -> float:
    """Bernoulli equation: find P2 given state 1 and velocity/elevation at state 2.

    Formula (incompressible, no losses):
        P1 + 0.5*rho*v1^2 + rho*g*h1 = P2 + 0.5*rho*v2^2 + rho*g*h2

    Args:
        P1: Pressure at point 1 (Pa).
        v1: Velocity at point 1 (m/s).
        h1: Elevation at point 1 (m).
        v2: Velocity at point 2 (m/s).
        h2: Elevation at point 2 (m).
        rho: Fluid density (kg/m^3).
        g: Gravitational acceleration (m/s^2), default 9.81.

    Returns:
        Pressure at point 2 (Pa).

    Raises:
        ValueError: If rho <= 0.

    Example:
        >>> bernoulli_pressure(P1=101325, v1=0, h1=0, v2=5, h2=0, rho=1000)
        88825.0
    """
    if rho <= 0:
        raise ValueError("Density must be positive.")
    return (
        P1
        + 0.5 * rho * (v1**2 - v2**2)
        + rho * g * (h1 - h2)
    )


def darcy_weisbach_head_loss(
    f: float,
    L: float,
    D: float,
    velocity: float,
    g: float = 9.81,
) -> float:
    """Darcy-Weisbach head loss in a pipe.

    Formula:
        h_f = f * (L/D) * (v^2 / (2*g))

    Args:
        f: Darcy friction factor (dimensionless).
        L: Pipe length (m).
        D: Pipe inner diameter (m).
        velocity: Flow velocity (m/s).
        g: Gravitational acceleration (m/s^2), default 9.81.

    Returns:
        Head loss (m).

    Raises:
        ValueError: If D <= 0 or f < 0.

    Example:
        >>> darcy_weisbach_head_loss(f=0.02, L=100, D=0.05, velocity=2)
        8.154...
    """
    if D <= 0:
        raise ValueError("Diameter must be positive.")
    if f < 0:
        raise ValueError("Friction factor must be non-negative.")
    return f * (L / D) * (velocity**2 / (2 * g))


def pump_power(
    rho: float,
    g: float,
    Q: float,
    head: float,
    efficiency: float = 1.0,
) -> float:
    """Hydraulic power required by a pump.

    Formula:
        P_hydraulic = rho * g * Q * H
        P_shaft = P_hydraulic / efficiency

    Args:
        rho: Fluid density (kg/m^3).
        g: Gravitational acceleration (m/s^2).
        Q: Volumetric flow rate (m^3/s).
        head: Pump head (m).
        efficiency: Pump efficiency (0 < eta <= 1), default 1.0.

    Returns:
        Shaft power required (W).

    Raises:
        ValueError: If efficiency not in (0, 1] or inputs invalid.

    Example:
        >>> pump_power(rho=1000, g=9.81, Q=0.01, head=10, efficiency=0.8)
        1226.25
    """
    if rho <= 0 or g <= 0 or Q < 0 or head < 0:
        raise ValueError("Invalid input: rho, g must be positive; Q, head non-negative.")
    if not (0 < efficiency <= 1):
        raise ValueError("Efficiency must be in (0, 1].")

    P_hydraulic = rho * g * Q * head
    return P_hydraulic / efficiency