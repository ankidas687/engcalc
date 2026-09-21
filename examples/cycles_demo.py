"""Demo script for engcalc.cycles module."""

from engcalc import cycles


def main():
    print("=" * 55)
    print("engcalc demo — Thermodynamic Cycles")
    print("=" * 55)

    # Carnot
    eta_carnot = cycles.carnot_efficiency(T_hot=800, T_cold=300)
    print(f"\nCarnot cycle (T_hot=800K, T_cold=300K):")
    print(f"  Efficiency: {eta_carnot * 100:.2f}%")

    # Otto
    eta_otto = cycles.otto_efficiency(compression_ratio=8)
    print(f"\nOtto cycle (r=8, petrol engine):")
    print(f"  Efficiency: {eta_otto * 100:.2f}%")

    # Diesel
    eta_diesel = cycles.diesel_efficiency(compression_ratio=18, cutoff_ratio=2)
    print(f"\nDiesel cycle (r=18, rc=2):")
    print(f"  Efficiency: {eta_diesel * 100:.2f}%")

    # Brayton
    eta_brayton = cycles.brayton_efficiency(pressure_ratio=10)
    print(f"\nBrayton cycle (rp=10, gas turbine):")
    print(f"  Efficiency: {eta_brayton * 100:.2f}%")


if __name__ == "__main__":
    main()