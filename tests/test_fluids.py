"""Tests for engcalc.fluids module."""

import pytest

from engcalc import fluids


# ---------- Reynolds Number ----------

def test_reynolds_standard():
    """Re = (1000 * 2 * 0.05) / 0.001 = 100000."""
    Re = fluids.reynolds_number(rho=1000, velocity=2, diameter=0.05, mu=0.001)
    assert abs(Re - 100000.0) < 1e-6


def test_reynolds_zero_viscosity_raises():
    """mu = 0 → ValueError."""
    with pytest.raises(ValueError):
        fluids.reynolds_number(rho=1000, velocity=2, diameter=0.05, mu=0)


def test_reynolds_negative_input_raises():
    """Negative density → ValueError."""
    with pytest.raises(ValueError):
        fluids.reynolds_number(rho=-1000, velocity=2, diameter=0.05, mu=0.001)


# ---------- Flow Regime ----------

def test_flow_regime_laminar():
    assert fluids.flow_regime(1500) == "laminar"


def test_flow_regime_transitional():
    assert fluids.flow_regime(3000) == "transitional"


def test_flow_regime_turbulent():
    assert fluids.flow_regime(5000) == "turbulent"


# ---------- Bernoulli ----------

def test_bernoulli_standard():
    """P1=101325, v1=0, h1=0, v2=5, h2=0, rho=1000."""
    P2 = fluids.bernoulli_pressure(
        P1=101325, v1=0, h1=0, v2=5, h2=0, rho=1000
    )
    # 101325 - 0.5*1000*25 = 101325 - 12500 = 88825
    assert abs(P2 - 88825) < 1e-6


def test_bernoulli_invalid_density_raises():
    with pytest.raises(ValueError):
        fluids.bernoulli_pressure(
            P1=101325, v1=0, h1=0, v2=5, h2=0, rho=0
        )


# ---------- Darcy-Weisbach ----------

def test_darcy_standard():
    """h_f = 0.02 * (100/0.05) * (4 / 19.62) = 8.154..."""
    h_f = fluids.darcy_weisbach_head_loss(f=0.02, L=100, D=0.05, velocity=2)
    assert abs(h_f - 8.154) < 0.01


def test_darcy_zero_diameter_raises():
    with pytest.raises(ValueError):
        fluids.darcy_weisbach_head_loss(f=0.02, L=100, D=0, velocity=2)


def test_darcy_negative_friction_raises():
    with pytest.raises(ValueError):
        fluids.darcy_weisbach_head_loss(f=-0.01, L=100, D=0.05, velocity=2)


# ---------- Pump Power ----------

def test_pump_power_standard():
    """P = 1000 * 9.81 * 0.01 * 10 / 0.8 = 1226.25 W."""
    P = fluids.pump_power(rho=1000, g=9.81, Q=0.01, head=10, efficiency=0.8)
    assert abs(P - 1226.25) < 1e-6


def test_pump_power_perfect_efficiency():
    """eta = 1: P = 1000 * 9.81 * 0.01 * 10 = 981 W."""
    P = fluids.pump_power(rho=1000, g=9.81, Q=0.01, head=10, efficiency=1.0)
    assert abs(P - 981.0) < 1e-6


def test_pump_power_invalid_efficiency_raises():
    with pytest.raises(ValueError):
        fluids.pump_power(rho=1000, g=9.81, Q=0.01, head=10, efficiency=1.5)