"""
Aviation Turbulence Module Example

This example demonstrates the usage of the aviation_turbulence module
to process PIREP data and create training datasets.
"""

import wxcbench.aviation_turbulence as wab

# Step 1: Download PIREP data
print("Step 1: Downloading PIREP data...")
print("Note: This will download data from 2020-2023 (can take several minutes)")
print("Note: If you encounter SSL certificate errors, the download may fail")
df = wab.get_pirep_data(start_year=2020, end_year=2023, output_dir='./pirep_downloads')
print(f"Downloaded {len(df)} PIREP records")
print()

# Step 2: Preprocess and categorize by flight level
print("Step 2: Preprocessing data...")
import os
if not os.path.exists('pirep_downloads/all_pireps.csv'):
    print("ERROR: pirep_downloads/all_pireps.csv not found!")
    print("Step 1 (data download) likely failed. Please check:")
    print("  1. Internet connection")
    print("  2. SSL certificate issues (may need to configure SSL certificates)")
    print("  3. Try downloading a smaller date range first")
    print("\nSkipping remaining steps...")
    exit(1)

df_processed = wab.preprocess_turb_eda('pirep_downloads/all_pireps.csv', output_dir='./updated_CSVs')
print(f"Preprocessed data shape: {df_processed.shape}")
print()

# Step 3: Filter for MODG turbulence (optional)
print("Step 3: Filtering MODG turbulence...")
df_modg = wab.preprocess_modg('updated_CSVs/csv_fl_rem.csv', output_dir='./updated_CSVs')
print(f"MODG filtered data shape: {df_modg.shape}")
print()

# Step 4: Create risk map visualization (optional)
print("Step 4: Creating risk map visualization...")
wab.convert_to_risk_map(
    'updated_CSVs/csv_fl_rem.csv',
    output_file='turbulence_risk_map.png'
)
print("Risk map saved to: turbulence_risk_map.png")
print()

# Step 5: Grid PIREPs onto MERRA-2 grid
print("Step 5: Gridding PIREPs onto MERRA-2 grid...")
wab.grid_pireps(
    pirep_files=[
        'updated_CSVs/low_fl.csv',
        'updated_CSVs/med_fl.csv',
        'updated_CSVs/high_fl.csv'
    ],
    output_dir='./gridded_data',
    threshold=0.25
)
print("Gridding complete!")
print()

# Step 6: Create training data (requires MERRA2 data)
print("Step 6: Creating training data...")
print("Note: This step requires MERRA2 data files in the specified directory")
print("Example call (commented out - uncomment and provide MERRA2 data path):")
print("""
wab.create_training_data(
    turbulence_dir='./gridded_data',
    merra2_dir='./MERRA2_2021-2022_1000hPa-100hPa',
    years=[2021, 2022],
    levels=['low', 'med', 'high'],
    output_dir='./training_data'
)
""")

print("Aviation Turbulence workflow example complete!")
print("\nOutput directories created:")
print("  - ./pirep_downloads/")
print("  - ./updated_CSVs/")
print("  - ./gridded_data/")
print("  - ./training_data/ (if Step 6 is executed)")

