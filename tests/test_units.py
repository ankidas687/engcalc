"""Tests for engcalc.units module."""

import pytest

from engcalc import units


# ---------- Basic conversions ----------

def test_cm_to_m():
    assert abs(units.convert(100, "cm", "m") - 1.0) < 1e-9


def test_m_to_mm():
    assert abs(units.convert(1, "m", "mm") - 1000.0) < 1e-9


def test_inch_to_cm():
    assert abs(units.convert(1, "in", "cm") - 2.54) < 1e-9


def test_km_to_mile():
    """1 km = 0.621371 mile."""
    assert abs(units.convert(1, "km", "mile") - 0.621371) < 1e-5


# ---------- Mass ----------

def test_kg_to_lb():
    """1 kg = 2.20462 lb."""
    assert abs(units.convert(1, "kg", "lb") - 2.20462262185) < 1e-9


def test_lb_to_kg():
    assert abs(units.convert(1, "lb", "kg") - 0.45359237) < 1e-9


# ---------- Temperature ----------

def test_celsius_to_kelvin():
    assert abs(units.convert(100, "degC", "K") - 373.15) < 1e-9


def test_kelvin_to_celsius():
    assert abs(units.convert(273.15, "K", "degC") - 0.0) < 1e-9


def test_celsius_to_fahrenheit():
    """100 degC = 212 degF."""
    assert abs(units.convert(100, "degC", "degF") - 212.0) < 1e-9


def test_fahrenheit_to_celsius():
    """32 degF = 0 degC."""
    assert abs(units.convert(32, "degF", "degC") - 0.0) < 1e-9


def test_fahrenheit_to_kelvin():
    """32 degF = 273.15 K."""
    assert abs(units.convert(32, "degF", "K") - 273.15) < 1e-9


def test_rankine_to_kelvin():
    """491.67 degR = 273.15 K."""
    assert abs(units.convert(491.67, "degR", "K") - 273.15) < 1e-6


# ---------- Pressure ----------

def test_atm_to_pa():
    assert abs(units.convert(1, "atm", "Pa") - 101325.0) < 1e-6


def test_atm_to_psi():
    assert abs(units.convert(1, "atm", "psi") - 14.695948775513449) < 1e-9


def test_bar_to_pa():
    assert abs(units.convert(1, "bar", "Pa") - 1e5) < 1e-6


def test_mpa_to_psi():
    """1 MPa ≈ 145.038 psi."""
    assert abs(units.convert(1, "MPa", "psi") - 145.0377377) < 1e-4


# ---------- Energy ----------

def test_joule_to_calorie():
    assert abs(units.convert(4.184, "J", "cal") - 1.0) < 1e-9


def test_kwh_to_joule():
    assert abs(units.convert(1, "kWh", "J") - 3.6e6) < 1e-3


def test_btu_to_joule():
    assert abs(units.convert(1, "BTU", "J") - 1055.05585262) < 1e-6


# ---------- Power ----------

def test_hp_to_watt():
    assert abs(units.convert(1, "hp", "W") - 745.6998715822702) < 1e-6


def test_kw_to_watt():
    assert abs(units.convert(1, "kW", "W") - 1000.0) < 1e-9


# ---------- Force ----------

def test_lbf_to_n():
    assert abs(units.convert(1, "lbf", "N") - 4.4482216152605) < 1e-9


def test_kgf_to_n():
    assert abs(units.convert(1, "kgf", "N") - 9.80665) < 1e-9


# ---------- Area ----------

def test_m2_to_cm2():
    assert abs(units.convert(1, "m^2", "cm^2") - 1e4) < 1e-3


def test_ft2_to_m2():
    assert abs(units.convert(1, "ft^2", "m^2") - 0.09290304) < 1e-9


# ---------- Volume ----------

def test_liter_to_m3():
    assert abs(units.convert(1000, "L", "m^3") - 1.0) < 1e-9


def test_gal_to_liter():
    assert abs(units.convert(1, "gal_US", "L") - 3.785411784) < 1e-9


# ---------- Velocity ----------

def test_kmh_to_ms():
    """36 km/h = 10 m/s."""
    assert abs(units.convert(36, "km/h", "m/s") - 10.0) < 1e-9


def test_mph_to_kmh():
    assert abs(units.convert(1, "mph", "km/h") - 1.609344) < 1e-9


# ---------- Angle ----------

def test_deg_to_rad():
    import math
    assert abs(units.convert(180, "deg", "rad") - math.pi) < 1e-9


def test_rad_to_deg():
    import math
    assert abs(units.convert(math.pi, "rad", "deg") - 180.0) < 1e-9


# ---------- Errors ----------

def test_unknown_unit_raises():
    with pytest.raises(KeyError):
        units.convert(1, "furlong", "m")


def test_cross_category_raises():
    """Cannot convert length to mass."""
    with pytest.raises(ValueError):
        units.convert(1, "m", "kg")


# ---------- Utilities ----------

def test_list_categories_contains_length():
    assert "length" in units.list_categories()


def test_list_categories_contains_temperature():
    assert "temperature" in units.list_categories()


def test_list_units_length_contains_m():
    assert "m" in units.list_units("length")


def test_list_units_temperature_contains_degC():
    assert "degC" in units.list_units("temperature")


def test_list_units_unknown_category_raises():
    with pytest.raises(KeyError):
        units.list_units("unicorn")


def test_find_category_psi():
    assert units.find_category("psi") == "pressure"


def test_find_category_degC():
    assert units.find_category("degC") == "temperature"