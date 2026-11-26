"""Prepare the deterministic synthetic dataset for lab 10; contains no student solutions."""

from pathlib import Path  # Resolve output paths relative to this preparation script.

import numpy as np  # Generate reproducible random values.
import pandas as pd  # Assemble and export the table.


DATA_DIR = Path(__file__).resolve().parent / "data"  # Keep the output in this lab folder.
SEED = 20261124  # Fix the simulation so every run reproduces the same CSV file.
N_RECORDS = 900  # Independent operating records of centrifugal pumps, not a time series.


def make_pumps(seed=SEED, n=N_RECORDS):
    """Simulate operating records of identical pumps with an inspection result (fault)."""
    rng = np.random.default_rng(seed)  # A dedicated random stream for the dataset.
    flow = rng.uniform(20, 80, n)  # Flow rate in m3/h, the operating point.
    nominal = 6.0 - 0.0006 * flow ** 2  # Pump curve: the expected head (pressure) falls with the square of the flow.
    deviation = rng.normal(0, 0.45, n)  # Deviation of the measured pressure from the pump curve in bar.
    pressure = nominal + deviation  # Measured discharge pressure in bar.
    bearing_temp = rng.normal(60, 6, n)  # Bearing temperature in degrees Celsius.
    current = 18 + 0.12 * flow + 0.4 * pressure + rng.normal(0, 0.6, n)  # Motor current in A; follows the operating point.
    vibration = np.exp(rng.normal(-0.5, 0.35, n))  # Vibration velocity in mm/s; unrelated to the fault in this simulation.
    ambient_temp = rng.normal(22, 4, n)  # Ambient temperature in degrees Celsius; unrelated to the fault.
    risk = (deviation / 0.45) ** 2 + ((bearing_temp - 60) / 6) ** 2 + rng.normal(0, 0.6, n)  # Distance from normal operation.
    fault = (risk > 3.2).astype(int)  # Too far from normal on either side: about 19 % faults.
    return pd.DataFrame({  # Assemble the table with realistic rounding.
        "record_id": [f"R{i:03d}" for i in range(1, n + 1)],  # Identifier, not an input feature.
        "flow": flow.round(1),
        "pressure": pressure.round(3),
        "bearing_temp": bearing_temp.round(1),
        "current": current.round(2),
        "vibration": vibration.round(3),
        "ambient_temp": ambient_temp.round(1),
        "fault": fault,  # Binary target: 1 = fault found at inspection.
    })


def main():
    DATA_DIR.mkdir(parents=True, exist_ok=True)  # Create the destination when preparing a fresh copy of the lab.
    pumps = make_pumps()  # Simulate the dataset.
    pumps.to_csv(DATA_DIR / "pumps.csv", index=False, lineterminator="\n")  # Reproducible text output.
    print(f"pumps.csv: {len(pumps)} rows, fault share {pumps['fault'].mean():.3f}")  # Report preparation without model results.


if __name__ == "__main__":  # Running the file prepares data; importing it has no filesystem effects.
    main()
