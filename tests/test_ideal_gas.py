"""Tests for engcalc.thermo.ideal_gas."""

import pytest

from engcalc import ideal_gas


def test_pressure_standard():
    """Standard case: 1 mol, 300 K, 0.024 m^3."""
    P = ideal_gas.pressure(n=1, T=300, V=0.024)
    # Expected: (1 * 8.314462618 * 300) / 0.024 = 103930.78...
    assert abs(P - 103930.78) < 0.01


def test_pressure_zero_volume_raises():
    """Zero volume should raise ValueError."""
    with pytest.raises(ValueError):
        ideal_gas.pressure(n=1, T=300, V=0)


def test_pressure_negative_volume_raises():
    """Negative volume should raise ValueError."""
    with pytest.raises(ValueError):
        ideal_gas.pressure(n=1, T=300, V=-1)