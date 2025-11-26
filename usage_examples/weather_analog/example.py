"""
Weather Analog Module Example

This example demonstrates the usage of the weather_analog module
to process MERRA2 data for weather analog applications.
"""

from datetime import datetime
import wxcbench.weather_analog as weather_analog

# Step 1: Process single file
print("Step 1: Processing a single MERRA2 file...")
print("Note: Replace with actual MERRA2 file path")
print("""
# Example: Process a single MERRA2 file
success = weather_analog.process_single_file(
    input_file='./MERRA2_data/M2I1NXASM/MERRA2.20190101.SUB.nc',
    output_file='./MERRA2_processed/MERRA2_SLP_T2M_20190101.nc',
    variables=['SLP', 'T2M'],
    lon_bounds=(-15, 0),
    lat_bounds=(42, 58)
)

if success:
    print("Single file processing successful!")
else:
    print("Processing failed!")
""")
print()

# Step 2: Preprocess weather analog data for a time period
print("Step 2: Processing MERRA2 data for a time period...")
print("Note: Replace with actual MERRA2 data directory path")
print("""
# Example: Process data for 2019
processed_files = weather_analog.preprocess_weather_analog(
    start_date=datetime(2019, 1, 1),
    end_date=datetime(2019, 12, 31),
    input_dir='./MERRA2_data/M2I1NXASM',
    output_dir='./MERRA2_processed',
    lon_bounds=(-15, 0),
    lat_bounds=(42, 58),
    variables=['SLP', 'T2M']
)

print(f"Processed {len(processed_files)} files")
""")
print()

# Step 3: Process with different geographic bounds
print("Step 3: Processing with custom geographic bounds...")
print("""
# Example: Process data for a different region (e.g., Eastern US)
processed_files = weather_analog.preprocess_weather_analog(
    start_date=datetime(2020, 1, 1),
    end_date=datetime(2020, 6, 30),
    input_dir='./MERRA2_data/M2I1NXASM',
    output_dir='./MERRA2_processed_eastern_us',
    lon_bounds=(-90, -60),  # Eastern US longitude range
    lat_bounds=(25, 50),    # Eastern US latitude range
    variables=['SLP', 'T2M'],
    skip_existing=True  # Skip already processed files
)
""")
print()

# Complete workflow example
print("Complete workflow example:")
print("""
from datetime import datetime
import wxcbench.weather_analog as weather_analog

# Process MERRA2 data for 2019
print("Processing MERRA2 data for 2019...")
processed_files = weather_analog.preprocess_weather_analog(
    start_date=datetime(2019, 1, 1),
    end_date=datetime(2019, 12, 31),
    input_dir='./MERRA2_data/M2I1NXASM',
    output_dir='./MERRA2_processed',
    lon_bounds=(-15, 0),
    lat_bounds=(42, 58)
)

print(f"Processed {len(processed_files)} files")

# Verify by processing a single file
print("\\nVerifying with single file...")
success = weather_analog.process_single_file(
    input_file='./MERRA2_data/M2I1NXASM/MERRA2.20190101.SUB.nc',
    output_file='./MERRA2_processed/test_20190101.nc',
    variables=['SLP', 'T2M'],
    lon_bounds=(-15, 0),
    lat_bounds=(42, 58)
)

if success:
    print("Single file processing successful!")
else:
    print("Processing failed!")

print("Workflow complete!")
""")

print("Weather Analog workflow example complete!")
print("\nPrerequisites:")
print("  - MERRA2 data files in the input directory")
print("  - MERRA2 files should follow naming pattern: MERRA2*.{date}.SUB.nc")
print("\nOutput directory:")
print("  - ./MERRA2_processed/ (processed NetCDF files)")

