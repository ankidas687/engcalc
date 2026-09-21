"""Demo script for engcalc.ideal_gas module."""

from engcalc import ideal_gas


def main():
    print("=" * 50)
    print("engcalc demo — Ideal Gas Law")
    print("=" * 50)

    # Standard case
    n = 1.0       # moles
    T = 300.0     # Kelvin
    V = 0.024     # m^3

    P = ideal_gas.pressure(n=n, T=T, V=V)
    print(f"\nInput:  n={n} mol, T={T} K, V={V} m^3")
    print(f"Output: P = {P:.2f} Pa")
    print(f"        P = {P / 1000:.2f} kPa")
    print(f"        P = {P / 101325:.4f} atm")


if __name__ == "__main__":
    main()