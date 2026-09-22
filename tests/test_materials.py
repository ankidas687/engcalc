"""Tests for engcalc.materials module."""

import pytest

from engcalc import materials


# ---------- list_materials ----------

def test_list_materials_not_empty():
    """At least one material available."""
    assert len(materials.list_materials()) > 0


def test_list_materials_contains_steel():
    assert "steel_AISI_1040" in materials.list_materials()


# ---------- list_categories ----------

def test_list_categories_contains_steel():
    assert "steel" in materials.list_categories()


def test_list_categories_contains_aluminum():
    assert "aluminum" in materials.list_categories()


# ---------- get ----------

def test_get_density_steel():
    """AISI 1040 density = 7850 kg/m^3."""
    assert materials.get("steel_AISI_1040", "density") == 7850


def test_get_youngs_modulus_aluminum():
    """Aluminum 6061-T6 E = 68.9 GPa."""
    E = materials.get("aluminum_6061_T6", "youngs_modulus")
    assert abs(E - 68.9e9) < 1e6


def test_get_unknown_material_raises():
    with pytest.raises(KeyError):
        materials.get("nonexistent_material", "density")


def test_get_unknown_property_raises():
    with pytest.raises(KeyError):
        materials.get("steel_AISI_1040", "fake_property")


def test_get_none_value_raises():
    """Gray cast iron has no yield strength (null in JSON)."""
    with pytest.raises(ValueError):
        materials.get("cast_iron_gray", "yield_strength")


# ---------- get_all ----------

def test_get_all_returns_dict():
    props = materials.get_all("steel_AISI_1040")
    assert isinstance(props, dict)
    assert "density" in props
    assert "youngs_modulus" in props


def test_get_all_unknown_raises():
    with pytest.raises(KeyError):
        materials.get_all("nonexistent")


# ---------- search ----------

def test_search_steel():
    steels = materials.search("steel")
    assert "steel_AISI_1040" in steels
    assert "steel_SS_304" in steels


def test_search_aluminum():
    aluminums = materials.search("aluminum")
    assert "aluminum_6061_T6" in aluminums
    assert "aluminum_7075_T6" in aluminums


def test_search_unknown_category_empty():
    assert materials.search("unicorn") == []