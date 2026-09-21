"""Demo script for engcalc.fluids module."""

from engcalc import fluids


def main():
    print("=" * 55)
    print("engcalc demo — Fluid Mechanics")
    print("=" * 55)

    # Reynolds number
    Re = fluids.reynolds_number(rho=1000, velocity=2, diameter=0.05, mu=0.001)
    regime = fluids.flow_regime(Re)
    print(f"\nReynolds number (water in pipe):")
    print(f"  rho=1000, v=2 m/s, D=0.05 m, mu=0.001")
    print(f"  Re = {Re:.0f} → {regime}")

    # Bernoulli
    P2 = fluids.bernoulli_pressure(
        P1=101325, v1=0, h1=0, v2=5, h2=0, rho=1000
    )
    print(f"\nBernoulli equation:")
    print(f"  P1=101325 Pa, v1=0, v2=5 m/s")
    print(f"  P2 = {P2:.2f} Pa")

    # Darcy-Weisbach
    h_f = fluids.darcy_weisbach_head_loss(
        f=0.02, L=100, D=0.05, velocity=2
    )
    print(f"\nDarcy-Weisbach head loss:")
    print(f"  f=0.02, L=100 m, D=0.05 m, v=2 m/s")
    print(f"  h_f = {h_f:.4f} m")

    # Pump power
    P = fluids.pump_power(rho=1000, g=9.81, Q=0.01, head=10, efficiency=0.8)
    print(f"\nPump power:")
    print(f"  Q=0.01 m^3/s, head=10 m, eta=0.8")
    print(f"  P = {P:.2f} W ({P/1000:.3f} kW)")


if __name__ == "__main__":
    main()