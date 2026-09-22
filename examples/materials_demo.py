"""Demo script for engcalc.materials module."""

from engcalc import materials


def main():
    print("=" * 60)
    print("engcalc demo — Materials Database")
    print("=" * 60)

    # List all categories
    cats = materials.list_categories()
    print(f"\nAvailable categories ({len(cats)}):")
    for c in cats:
        print(f"  - {c}")

    # List all materials
    all_mats = materials.list_materials()
    print(f"\nTotal materials: {len(all_mats)}")

    # Steel list
    steels = materials.search("steel")
    print(f"\nSteel grades ({len(steels)}):")
    for s in steels:
        print(f"  - {s}")

    # Aluminum list
    aluminums = materials.search("aluminum")
    print(f"\nAluminum alloys ({len(aluminums)}):")
    for a in aluminums:
        print(f"  - {a}")

    # Detailed properties of one material
    print("\n" + "=" * 60)
    print("Detailed: Aluminum 6061-T6")
    print("=" * 60)
    props = materials.get_all("aluminum_6061_T6")
    for key, value in props.items():
        if isinstance(value, float) and value > 1e6:
            print(f"  {key:25s}: {value:.3e}")
        else:
            print(f"  {key:25s}: {value}")


if __name__ == "__main__":
    main()