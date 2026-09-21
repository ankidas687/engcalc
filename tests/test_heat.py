"""Tests for engcalc.heat module."""

import pytest

from engcalc import heat


# ---------- Conduction ----------

def test_conduction_standard():
    """Q = 50 * 2 * 100 / 0.1 = 100000 W."""
    Q = heat.conduction_rate(k=50, A=2, dT=100, L=0.1)
    assert abs(Q - 100000.0) < 1e-6


def test_conduction_zero_thickness_raises():
    with pytest.raises(ValueError):
        heat.conduction_rate(k=50, A=2, dT=100, L=0)


def test_conduction_negative_k_raises():
    with pytest.raises(ValueError):
        heat.conduction_rate(k=-50, A=2, dT=100, L=0.1)


# ---------- Convection ----------

def test_convection_standard():
    """Q = 25 * 2 * (350 - 300) = 2500 W."""
    Q = heat.convection_rate(h=25, A=2, T_surface=350, T_fluid=300)
    assert abs(Q - 2500.0) < 1e-6


def test_convection_negative_h_raises():
    with pytest.raises(ValueError):
        heat.convection_rate(h=-25, A=2, T_surface=350, T_fluid=300)


# ---------- Radiation ----------

def test_radiation_standard():
    """Q = 0.9 * 5.67e-8 * 1 * (500^4 - 300^4) ≈ 2776.03 W."""
    Q = heat.radiation_rate(
        emissivity=0.9, A=1, T_surface=500, T_surroundings=300
    )
    assert abs(Q - 2776.03) < 0.1


def test_radiation_invalid_emissivity_raises():
    with pytest.raises(ValueError):
        heat.radiation_rate(
            emissivity=1.5, A=1, T_surface=500, T_surroundings=300
        )


def test_radiation_negative_temperature_raises():
    with pytest.raises(ValueError):
        heat.radiation_rate(
            emissivity=0.9, A=1, T_surface=-100, T_surroundings=300
        )


# ---------- LMTD ----------

def test_lmtd_standard():
    """LMTD = (70 - 50) / ln(70/50) ≈ 59.44."""
    val = heat.lmtd(
        T_hot_in=400, T_hot_out=350, T_cold_in=300, T_cold_out=330
    )
    assert abs(val - 59.44) < 0.01


def test_lmtd_equal_temperatures():
    """dT1 == dT2 case: returns dT1."""
    val = heat.lmtd(
        T_hot_in=400, T_hot_out=350, T_cold_in=300, T_cold_out=350
    )
    assert abs(val - 50.0) < 1e-9


def test_lmtd_invalid_temperatures_raises():
    with pytest.raises(ValueError):
        heat.lmtd(
            T_hot_in=300, T_hot_out=350, T_cold_in=400, T_cold_out=330
        )