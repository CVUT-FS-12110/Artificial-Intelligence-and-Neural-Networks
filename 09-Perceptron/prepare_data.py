"""Prepare the deterministic synthetic dataset for lab 09; contains no student solutions."""

from pathlib import Path  # Resolve output paths relative to this preparation script.

import numpy as np  # Generate reproducible random values.
import pandas as pd  # Assemble and export the table.


DATA_DIR = Path(__file__).resolve().parent / "data"  # Keep the output in this lab folder.
SEED = 20261118  # Fix the simulation so every run reproduces the same CSV file.
N_PARTS = 2000  # Independent moulded parts, not a time series of one machine.


def make_parts():
    """Simulate independent injection-moulded parts with an inspection result and a measured shrinkage."""
    rng = np.random.default_rng(SEED)  # A dedicated random stream for the dataset.
    z = rng.normal(size=(N_PARTS, 6))  # Standardised process deviations of six informative settings.
    melt_temp = 230 + 6 * z[:, 0]  # Melt temperature in degrees Celsius.
    pressure = 900 + 60 * z[:, 1]  # Injection pressure in bar: numbers about a hundred times larger.
    cooling_time = 12 + 1.5 * z[:, 2]  # Cooling time in seconds.
    mould_temp = 60 + 4 * z[:, 3]  # Mould temperature in degrees Celsius.
    humidity = 45 + 10 * z[:, 4]  # Relative humidity of the granulate store in percent.
    vibration = np.exp(-0.7 + 0.4 * z[:, 5])  # Vibration of the press in mm/s: small positive, right-skewed values.
    shot_weight = 52 + 0.4 * rng.normal(size=N_PARTS)  # Shot weight in grams; unrelated to the defect in this simulation.
    cycle_time = 30 + 1.0 * rng.normal(size=N_PARTS)  # Cycle time in seconds; unrelated to the defect in this simulation.
    logit = (-3.1 + 0.9 * z[:, 0] - 0.8 * z[:, 1] - 0.7 * z[:, 2]  # A linear part of the defect risk.
             + 0.5 * z[:, 4] + 0.9 * z[:, 5]
             + 0.8 * z[:, 0] * z[:, 1])  # Temperature and pressure must be balanced: an interaction term.
    defect = (rng.random(N_PARTS) < 1 / (1 + np.exp(-logit))).astype(int)  # Overlapping classes, about 11 % defects.
    shrinkage = 1.5 + 0.08 * z[:, 0] - 0.05 * z[:, 1] + 0.06 * z[:, 2] + 0.03 * z[:, 3] + rng.normal(0, 0.04, N_PARTS)  # Linear in the settings plus noise.
    return pd.DataFrame({  # Assemble the table with realistic rounding.
        "part_id": [f"P{i:04d}" for i in range(1, N_PARTS + 1)],  # Identifier, not an input feature.
        "melt_temp": melt_temp.round(1),
        "pressure": pressure.round(0),
        "cooling_time": cooling_time.round(2),
        "mould_temp": mould_temp.round(1),
        "humidity": humidity.round(1),
        "vibration": vibration.round(3),
        "shot_weight": shot_weight.round(2),
        "cycle_time": cycle_time.round(2),
        "shrinkage": shrinkage.round(3),  # Continuous quantity; not used in the lab notebooks.
        "defect": defect,  # Binary target: 1 = defective part found at inspection.
    })


def main():
    DATA_DIR.mkdir(parents=True, exist_ok=True)  # Create the destination when preparing a fresh copy of the lab.
    parts = make_parts()  # Simulate the dataset.
    parts.to_csv(DATA_DIR / "parts.csv", index=False, lineterminator="\n")  # Reproducible text output.
    print(f"parts.csv: {len(parts)} rows, defect share {parts['defect'].mean():.3f}")  # Report preparation without model results.


if __name__ == "__main__":  # Running the file prepares data; importing it has no filesystem effects.
    main()
