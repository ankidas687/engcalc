# engcalc

> Mechanical Engineering calculations in Python — fast, tested, and easy to use.

[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://github.com/ankidas687/engcalc/actions/workflows/tests.yml/badge.svg)](https://github.com/ankidas687/engcalc/actions/workflows/tests.yml)
[![PyPI](https://img.shields.io/badge/PyPI-coming%20soon-orange)]()

`engcalc` is a pure-Python library for common Mechanical Engineering
calculations — thermodynamics, fluid mechanics, heat transfer,
material properties, and unit conversions. Designed for students,
engineers, and researchers who want clean, tested formulas without
the spreadsheet mess.

## Features

- **Thermodynamics** — ideal gas law, Carnot, Otto, Diesel, Brayton cycles
- **Fluid Mechanics** — Reynolds number, Bernoulli, Darcy-Weisbach, pump power
- **Heat Transfer** — conduction, convection, radiation, LMTD
- **Materials Database** — 10 common engineering materials (steel, aluminum, copper, titanium, cast iron) with 8 properties each
- **Unit Conversions** — 60+ units across 12 categories (length, mass, time, temperature, pressure, energy, power, force, area, volume, velocity, angle)
- **SI units** throughout — no unit confusion
- **Zero heavy dependencies** — only NumPy
- **Fully type-hinted** and tested (91 tests passing)

## Installation

```bash
pip install engcalc
```

> ⚠️ Not yet on PyPI. Install from source for now:

```bash
git clone https://github.com/ankidas687/engcalc.git
cd engcalc
pip install -e .
```

## Quick Start

```python
from engcalc import ideal_gas, cycles, fluids, heat, materials, units

# Ideal gas law: PV = nRT
P = ideal_gas.pressure(n=1, T=300, V=0.024)
print(f"Pressure: {P:.2f} Pa")            # 103930.78 Pa

# Carnot cycle efficiency
eta = cycles.carnot_efficiency(T_hot=800, T_cold=300)
print(f"Carnot efficiency: {eta * 100:.2f}%")   # 62.50%

# Reynolds number
Re = fluids.reynolds_number(rho=1000, velocity=2, diameter=0.05, mu=0.001)
print(f"Re = {Re:.0f} → {fluids.flow_regime(Re)}")   # 100000 → turbulent

# Heat conduction through a wall
Q = heat.conduction_rate(k=50, A=2, dT=100, L=0.1)
print(f"Heat rate: {Q:.2f} W")            # 100000.00 W

# Material property lookup
rho = materials.get("steel_AISI_1040", "density")
print(f"Steel density: {rho} kg/m^3")     # 7850 kg/m^3

# Unit conversion
temp_K = units.convert(100, "degC", "K")
print(f"100 °C = {temp_K:.2f} K")         # 373.15 K
```

## Modules

| Module | Functions | Description |
|---|---|---|
| `engcalc.ideal_gas` | `pressure`, `volume`, `temperature`, `moles` | Ideal gas law (PV = nRT) |
| `engcalc.cycles` | `carnot_efficiency`, `otto_efficiency`, `diesel_efficiency`, `brayton_efficiency` | Thermodynamic cycle efficiencies |
| `engcalc.fluids` | `reynolds_number`, `flow_regime`, `bernoulli_pressure`, `darcy_weisbach_head_loss`, `pump_power` | Fluid mechanics |
| `engcalc.heat` | `conduction_rate`, `convection_rate`, `radiation_rate`, `lmtd` | Heat transfer |
| `engcalc.materials` | `get`, `get_all`, `list_materials`, `search`, `list_categories` | Material property database |
| `engcalc.units` | `convert`, `list_categories`, `list_units`, `find_category` | Unit conversion utilities |

## Examples

Check the [`examples/`](examples/) folder for complete demo scripts:

- `examples/demo.py` — Ideal gas law
- `examples/cycles_demo.py` — Thermodynamic cycles
- `examples/fluids_demo.py` — Fluid mechanics
- `examples/heat_demo.py` — Heat transfer
- `examples/materials_demo.py` — Materials database
- `examples/units_demo.py` — Unit conversions

Run any demo:

```bash
python examples/cycles_demo.py
```

## Development

```bash
# Clone the repo
git clone https://github.com/ankidas687/engcalc.git
cd engcalc

# Create virtual environment
python -m venv venv
venv\Scripts\Activate.ps1    # Windows
# source venv/bin/activate   # macOS/Linux

# Install with dev dependencies
pip install -e ".[dev]"

# Run tests
pytest
```

## Contributing

Contributions are welcome! If you find a bug or want to add a new
calculation, feel free to:

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/new-formula`)
3. Commit your changes (`git commit -m "Add new formula"`)
4. Push to the branch (`git push origin feature/new-formula`)
5. Open a Pull Request

## Roadmap

- [x] Thermodynamics (ideal gas, cycles)
- [x] Fluid mechanics
- [x] Heat transfer
- [x] Materials database
- [x] Unit conversion utilities
- [ ] Mechanics of materials (stress, strain, beam)
- [ ] Publish to PyPI

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

## Author

**Ankita Das** — [@ankidas687](https://github.com/ankidas687)

---

⭐ If you find this useful, consider giving it a star!