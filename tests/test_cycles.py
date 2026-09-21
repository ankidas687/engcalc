"""Tests for engcalc.cycles module."""

import pytest

from engcalc import cycles


# ---------- Carnot ----------

def test_carnot_standard():
    """Carnot: T_hot=800 K, T_cold=300 K → 0.625."""
    eta = cycles.carnot_efficiency(T_hot=800, T_cold=300)
    assert abs(eta - 0.625) < 1e-9


def test_carnot_equal_temperatures_raises():
    """T_hot == T_cold → ValueError."""
    with pytest.raises(ValueError):
        cycles.carnot_efficiency(T_hot=300, T_cold=300)


def test_carnot_negative_temperature_raises():
    """Negative temperature → ValueError."""
    with pytest.raises(ValueError):
        cycles.carnot_efficiency(T_hot=-100, T_cold=300)


# ---------- Otto ----------

def test_otto_standard():
    """Otto: r=8, gamma=1.4 → about 0.5647."""
    eta = cycles.otto_efficiency(compression_ratio=8)
    assert abs(eta - 0.5647) < 0.001


def test_otto_invalid_ratio_raises():
    """r <= 1 → ValueError."""
    with pytest.raises(ValueError):
        cycles.otto_efficiency(compression_ratio=1)


# ---------- Diesel ----------

def test_diesel_standard():
    """Diesel: r=18, rc=2, gamma=1.4 → about 0.631."""
    eta = cycles.diesel_efficiency(compression_ratio=18, cutoff_ratio=2)
    assert abs(eta - 0.631) < 0.001


def test_diesel_invalid_cutoff_raises():
    """rc <= 1 → ValueError."""
    with pytest.raises(ValueError):
        cycles.diesel_efficiency(compression_ratio=18, cutoff_ratio=1)


# ---------- Brayton ----------

def test_brayton_standard():
    """Brayton: rp=10, gamma=1.4 → about 0.482."""
    eta = cycles.brayton_efficiency(pressure_ratio=10)
    assert abs(eta - 0.482) < 0.001


def test_brayton_invalid_ratio_raises():
    """rp <= 1 → ValueError."""
    with pytest.raises(ValueError):
        cycles.brayton_efficiency(pressure_ratio=1)