"""Demo script for engcalc.heat module."""

from engcalc import heat


def main():
    print("=" * 55)
    print("engcalc demo — Heat Transfer")
    print("=" * 55)

    # Conduction
    Q_cond = heat.conduction_rate(k=50, A=2, dT=100, L=0.1)
    print(f"\nConduction through wall:")
    print(f"  k=50 W/(m·K), A=2 m², ΔT=100 K, L=0.1 m")
    print(f"  Q = {Q_cond:.2f} W ({Q_cond/1000:.2f} kW)")

    # Convection
    Q_conv = heat.convection_rate(h=25, A=2, T_surface=350, T_fluid=300)
    print(f"\nConvection from surface:")
    print(f"  h=25 W/(m²·K), A=2 m², T_s=350 K, T_f=300 K")
    print(f"  Q = {Q_conv:.2f} W")

    # Radiation
    Q_rad = heat.radiation_rate(
        emissivity=0.9, A=1, T_surface=500, T_surroundings=300
    )
    print(f"\nRadiation from surface:")
    print(f"  ε=0.9, A=1 m², T_s=500 K, T_sur=300 K")
    print(f"  Q = {Q_rad:.2f} W")

    # LMTD
    lmtd_val = heat.lmtd(
        T_hot_in=400, T_hot_out=350, T_cold_in=300, T_cold_out=330
    )
    print(f"\nLMTD for heat exchanger:")
    print(f"  T_hot: 400 → 350, T_cold: 300 → 330")
    print(f"  LMTD = {lmtd_val:.2f} K")


if __name__ == "__main__":
    main()