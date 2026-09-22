"""Demo script for engcalc.units module."""

from engcalc import units


def main():
    print("=" * 60)
    print("engcalc demo — Unit Conversion Utilities")
    print("=" * 60)

    # Categories
    cats = units.list_categories()
    print(f"\nSupported categories ({len(cats)}):")
    for c in cats:
        units_in_cat = units.list_units(c)
        print(f"  {c:12s} ({len(units_in_cat)} units): {', '.join(units_in_cat)}")

    # Length
    print("\n" + "=" * 60)
    print("Length conversions")
    print("=" * 60)
    print(f"  100 cm  = {units.convert(100, 'cm', 'm'):.4f} m")
    print(f"  1 m     = {units.convert(1, 'm', 'mm'):.1f} mm")
    print(f"  1 in    = {units.convert(1, 'in', 'cm'):.4f} cm")
    print(f"  1 km    = {units.convert(1, 'km', 'mile'):.6f} mile")

    # Temperature
    print("\n" + "=" * 60)
    print("Temperature conversions")
    print("=" * 60)
    print(f"  100 °C  = {units.convert(100, 'degC', 'K'):.2f} K")
    print(f"  100 °C  = {units.convert(100, 'degC', 'degF'):.2f} °F")
    print(f"  32 °F   = {units.convert(32, 'degF', 'degC'):.2f} °C")
    print(f"  0 K     = {units.convert(0, 'K', 'degC'):.2f} °C")

    # Pressure
    print("\n" + "=" * 60)
    print("Pressure conversions")
    print("=" * 60)
    print(f"  1 atm   = {units.convert(1, 'atm', 'Pa'):.2f} Pa")
    print(f"  1 atm   = {units.convert(1, 'atm', 'psi'):.4f} psi")
    print(f"  1 bar   = {units.convert(1, 'bar', 'Pa'):.2f} Pa")
    print(f"  1 MPa   = {units.convert(1, 'MPa', 'psi'):.4f} psi")

    # Energy & Power
    print("\n" + "=" * 60)
    print("Energy & Power")
    print("=" * 60)
    print(f"  1 kWh   = {units.convert(1, 'kWh', 'J'):.2e} J")
    print(f"  1 BTU   = {units.convert(1, 'BTU', 'J'):.2f} J")
    print(f"  1 hp    = {units.convert(1, 'hp', 'W'):.2f} W")
    print(f"  1 hp    = {units.convert(1, 'hp', 'kW'):.4f} kW")

    # Fluid-related
    print("\n" + "=" * 60)
    print("Fluid & Mechanics")
    print("=" * 60)
    print(f"  1 lbf   = {units.convert(1, 'lbf', 'N'):.4f} N")
    print(f"  1 kgf   = {units.convert(1, 'kgf', 'N'):.4f} N")
    print(f"  36 km/h = {units.convert(36, 'km/h', 'm/s'):.4f} m/s")
    print(f"  1 gal   = {units.convert(1, 'gal_US', 'L'):.4f} L")


if __name__ == "__main__":
    main()