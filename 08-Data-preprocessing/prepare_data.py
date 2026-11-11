"""Prepare deterministic synthetic datasets before the lab; no student solutions."""

from pathlib import Path  # Resolve output paths relative to this preparation script.

import numpy as np  # Generate reproducible independent random values.
import pandas as pd  # Assemble and export labelled tables.


DATA_DIR = Path(__file__).resolve().parent / "data"  # Keep all outputs in this lab folder.
SEED = 20261110  # Fix the simulation so every run reproduces the same CSV files.
N_SITUATIONS = 720  # These situations are independent, not repeated device measurements.
NUMERIC_COLUMNS = ["temperature", "vibration", "pressure", "power", "speed", "load"]  # Define numeric inputs.
CATEGORICAL_COLUMNS = ["mode", "environment"]  # Define nominal inputs without an intrinsic order.


def make_machine_records():
    """Simulate independent operating situations, then inject documented data defects."""
    rng = np.random.default_rng(SEED)  # Use a dedicated random stream for the main dataset.
    stress = rng.normal(size=N_SITUATIONS)  # Represent an unobserved condition affecting several inputs.
    activity = rng.normal(size=N_SITUATIONS)  # Represent a separate operating-intensity factor.
    high_indices = rng.choice(N_SITUATIONS, size=8, replace=False)  # Select genuine rare high-stress situations.
    stress[high_indices] += 4.2  # Create real positive extremes rather than erroneous negative measurements.
    mode = rng.choice(["auto", "manual", "eco"], size=N_SITUATIONS, p=[0.5, 0.3, 0.2])  # Sample operating modes.
    environment = rng.choice(["indoor", "outdoor"], size=N_SITUATIONS, p=[0.65, 0.35])  # Sample operating environments.
    temperature = 43 + 8 * stress + 2.5 * activity + rng.normal(0, 1.7, N_SITUATIONS)  # Correlate temperature with condition.
    vibration = np.maximum(0.04, 1.5 + 0.52 * stress + 0.10 * activity + rng.normal(0, 0.11, N_SITUATIONS))  # Use a much smaller numeric scale.
    pressure = 105 + 12 * activity - 3 * stress + rng.normal(0, 4, N_SITUATIONS)  # Make pressure share the activity factor.
    power = 500 + 1000 * np.exp(0.30 * activity + rng.normal(0, 0.65, N_SITUATIONS))  # Add large-scale variation unrelated to the target condition.
    speed = np.maximum(100, 1800 + 300 * activity + rng.normal(0, 450, N_SITUATIONS))  # Add another large-scale input.
    load = 100 / (1 + np.exp(-0.75 * activity - rng.normal(0, 0.18, N_SITUATIONS)))  # Keep illustrative load within zero and one hundred.
    risk = stress + 0.30 * (mode == "manual") - 0.15 * (mode == "eco") + 0.10 * (environment == "outdoor")  # Define a latent binary condition.
    risk += rng.normal(0, 0.26, N_SITUATIONS)  # Allow overlapping classes instead of a perfectly separable task.
    state = (risk > 0.68).astype(int)  # Mark the minority condition without changing its prevalence by resampling.
    records = pd.DataFrame({  # Assemble the clean independent situations.
        "record_id": [f"R{i:04d}" for i in range(1, N_SITUATIONS + 1)],  # Supply identifiers for duplicate inspection only.
        "temperature": temperature,  # Store the illustrative temperature in degrees Celsius.
        "vibration": vibration,  # Store the illustrative vibration in millimetres per second.
        "pressure": pressure,  # Store the illustrative pressure in kilopascals.
        "power": power,  # Store the illustrative power in watts.
        "speed": speed,  # Store the illustrative rotational speed in revolutions per minute.
        "load": load,  # Store the illustrative percentage load.
        "mode": pd.Series(mode, dtype=object),  # Allow real missing cells in this nominal column.
        "environment": pd.Series(environment, dtype=object),  # Allow real missing cells in the second nominal column.
        "state": state,  # Keep the target observed for every training example.
    })
    for column in NUMERIC_COLUMNS + CATEGORICAL_COLUMNS:  # Inject missing entries independently by input column.
        missing_indices = rng.choice(N_SITUATIONS, size=36, replace=False)  # Exactly five percent of the 720 situations.
        records.loc[missing_indices, column] = np.nan  # Export these entries as empty CSV fields.
    valid_temperature_indices = records.index[records["temperature"].notna()].difference(high_indices)  # Preserve the genuine high-temperature examples.
    sentinel_indices = rng.choice(valid_temperature_indices, size=4, replace=False)  # Select four observed ordinary temperatures.
    records.loc[sentinel_indices, "temperature"] = -999.0  # Insert the only explicitly known invalid numeric sentinel.
    automatic_indices = records.index[records["mode"] == "auto"]  # Find observed labels suitable for a spelling variant.
    uppercase_indices = rng.choice(automatic_indices, size=5, replace=False)  # Select five otherwise valid automatic modes.
    records.loc[uppercase_indices, "mode"] = "AUTO"  # Introduce inconsistent capitalization without adding a new category.
    duplicate_indices = rng.choice(N_SITUATIONS, size=6, replace=False)  # Select six distinct complete records to duplicate.
    duplicated = pd.concat([records, records.loc[duplicate_indices]], ignore_index=True)  # Copy every field, including record_id and target.
    duplicated = duplicated.iloc[rng.permutation(len(duplicated))].reset_index(drop=True)  # Scatter duplicates among the records.
    assert len(duplicated) == 726 and duplicated.duplicated().sum() == 6  # Verify the intended duplicate boundary case.
    assert duplicated["record_id"].nunique() == N_SITUATIONS  # Ensure there are still exactly 720 independent situations.
    assert 0.25 <= records["state"].mean() <= 0.35  # Keep the intended moderately imbalanced binary task.
    return duplicated  # Return corrupted input data without cleaning it for students.


def make_new_records():
    """Supply four new situations without target values or reference predictions."""
    return pd.DataFrame([  # Keep these records independent of any training, validation or test partition.
        ["N0001", 42.5, 1.40, 108.0, 2050.0, 1820.0, 54.0, "auto", "indoor"],  # A fully observed familiar mode.
        ["N0002", np.nan, 2.10, 102.0, 1440.0, 1760.0, 48.0, "manual", "outdoor"],  # A missing numeric input.
        ["N0003", 49.0, 1.85, 111.0, np.nan, 2010.0, 61.0, "service", "indoor"],  # A previously unseen nominal value.
        ["N0004", 39.5, np.nan, 96.0, 1630.0, 1680.0, 41.0, "eco", np.nan],  # Missing numeric and categorical inputs.
    ], columns=["record_id"] + NUMERIC_COLUMNS + CATEGORICAL_COLUMNS)  # Deliberately omit the target column.


def make_grouped_records():
    """Create repeated observations whose device identities define dependent groups."""
    rng = np.random.default_rng(SEED + 1)  # Keep this dataset unchanged if the main generator is extended.
    n_groups = 36  # Simulate thirty-six devices.
    repeats = 8  # Observe each device eight times.
    condition = rng.normal(size=n_groups)  # Assign one latent condition to each device.
    device_temperature = 43 + 7 * condition + rng.normal(0, 4, n_groups)  # Give each device a persistent temperature profile.
    device_vibration = np.maximum(0.1, 1.6 + 0.5 * condition + rng.normal(0, 0.15, n_groups))  # Give each device a persistent vibration profile.
    device_state = (condition > 0.45).astype(int)  # Keep the condition label constant within each device.
    group_index = np.repeat(np.arange(n_groups), repeats)  # Map each measurement to its device.
    records = pd.DataFrame({  # Supply two measured inputs and explicit group identity.
        "group_id": [f"G{i + 1:03d}" for i in group_index],  # Group identity is for splitting, not a predictive input.
        "temperature": device_temperature[group_index] + rng.normal(0, 0.55, n_groups * repeats),  # Add small measurement noise.
        "vibration": np.maximum(0.02, device_vibration[group_index] + rng.normal(0, 0.045, n_groups * repeats)),  # Add small vibration noise.
        "state": device_state[group_index],  # Reuse the observed condition label for that device.
    })
    return records.iloc[rng.permutation(len(records))].reset_index(drop=True)  # Avoid relying on adjacent rows to identify a device.


def make_time_series():
    """Build next-hour prediction rows only when a simulated next observation exists."""
    rng = np.random.default_rng(SEED + 2)  # Use a separate deterministic stream for the temporal process.
    n_observations = 242  # Two boundary observations support 240 complete supervised rows.
    timestamps = pd.date_range("2025-01-01", periods=n_observations, freq="h")  # Use a regular hourly clock.
    hour = np.arange(n_observations)  # Locate each simulated measurement in time.
    baseline = 50 + 0.025 * hour + 6 * np.sin(2 * np.pi * hour / 24)  # Combine a slow trend with a daily pattern.
    noise = rng.normal(0, 0.8, n_observations)  # Generate genuinely observed random variation in the simulation.
    deviation = np.zeros(n_observations)  # Reserve an autocorrelated deviation process.
    deviation[0] = noise[0]  # Initialize the observed process.
    for i in range(1, n_observations):  # Advance one observed hour at a time.
        deviation[i] = 0.65 * deviation[i - 1] + noise[i]  # Make neighbouring observations dependent.
    observations = pd.DataFrame({"timestamp": timestamps, "current_value": baseline + deviation})  # Store the complete measured series.
    observations["lag1"] = observations["current_value"].shift(1)  # Use the previous measurement as a past-only feature.
    observations["next_value"] = observations["current_value"].shift(-1)  # Obtain the target by shifting actual simulated observations.
    observations["target_available_time"] = observations["timestamp"].shift(-1)  # Record when that next measurement actually becomes known.
    records = observations.dropna(subset=["lag1", "next_value", "target_available_time"]).copy()  # Remove both incomplete boundaries rather than inventing a target.
    records = records[["timestamp", "current_value", "lag1", "next_value", "target_available_time"]]  # Keep a stable teaching schema.
    assert len(records) == 240  # Confirm the final row also has an observed future outcome.
    assert ((records["target_available_time"] - records["timestamp"]) == pd.Timedelta(hours=1)).all()  # Verify the explicit one-hour availability delay.
    return records.reset_index(drop=True)  # Export contiguous table indices without treating them as time.


def make_stratification_records():
    """Provide the fixed miniature table for categorical and interval stratification."""
    states = np.repeat(["normal", "warning", "fault"], [84, 24, 12])  # Preserve the original example's category counts and order.
    loads = np.linspace(10.0, 100.0, 120)  # Preserve the original distinct, evenly spaced numeric values.
    return pd.DataFrame({"state": states, "load": loads})  # Export data rather than preparing it inside the student task.


def main():
    DATA_DIR.mkdir(parents=True, exist_ok=True)  # Create the destination when preparing a fresh copy of the lab.
    datasets = {  # Name the five complementary teaching datasets.
        "machine-records.csv": make_machine_records(),  # Main independent binary classification example.
        "new-records.csv": make_new_records(),  # New observations without ground truth.
        "grouped-records.csv": make_grouped_records(),  # Repeated measurements for group-aware splitting.
        "time-series.csv": make_time_series(),  # Forecasting example with explicit target availability.
        "stratification-records.csv": make_stratification_records(),  # Fixed miniature table for stratification exercises.
    }
    for filename, records in datasets.items():  # Export every dataset using the same conventions.
        precision = "%.17g" if filename == "stratification-records.csv" else "%.6f"  # Preserve the miniature table's original numeric precision without changing other CSV files.
        records.to_csv(DATA_DIR / filename, index=False, na_rep="", float_format=precision, date_format="%Y-%m-%dT%H:%M:%S", lineterminator="\n")  # Keep missing cells empty and output reproducible.
        print(f"{filename}: {len(records)} rows")  # Report preparation progress without publishing model results.


if __name__ == "__main__":  # Running the file prepares data; importing it has no filesystem effects.
    main()  # Execute dataset preparation only when explicitly requested.
