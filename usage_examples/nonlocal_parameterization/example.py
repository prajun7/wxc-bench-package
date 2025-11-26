"""
Nonlocal Parameterization Module Example

This example demonstrates the usage of the nonlocal_parameterization module
to download ERA5 data, compute momentum fluxes, and create training datasets.
"""

import wxcbench.nonlocal_parameterization as nonlocal

# Step 1: Download ERA5 model level data
print("Step 1: Downloading ERA5 model level data...")
print("Note: This requires CDS API credentials in ~/.cdsapirc")
print("Note: Downloading data for January 2020 (can take significant time)")
print("""
# Example: Download ERA5 data for January 2020
files = nonlocal.download_era5_modellevel_data(
    year=2020,
    month=1,
    start_day=1,
    end_day=31,
    output_dir='./ERA5_data_ml'
)
""")
print()

# Step 2: Compute momentum fluxes
print("Step 2: Computing momentum fluxes from ERA5 data...")
print("Note: This step requires ERA5 data files from Step 1")
print("""
# Example: Compute momentum fluxes
flux_files = nonlocal.compute_momentum_flux_from_era5(
    year=2020,
    month=1,
    era5_data_dir='./ERA5_data_ml',
    output_dir='./momentum_fluxes',
    truncation=21  # T21 truncation
)
""")
print()

# Step 3: Coarse-grain to T42 grid
print("Step 3: Coarse-graining momentum fluxes to T42 grid...")
print("Note: This step requires momentum flux files and T42 grid file")
print("""
# Example: Coarse-grain to T42 grid
training_files = nonlocal.coarsegrain_computed_momentum_fluxes(
    year=2020,
    start_month=1,
    end_month=1,
    t42_grid_file='./t42_lat_and_latb.nc',  # Path to T42 grid file
    momentum_flux_dir='./momentum_fluxes',
    era5_data_dir='./ERA5_data_ml',
    output_dir='./training_data'
)
""")
print()

# Complete workflow example (commented out)
print("Complete workflow example:")
print("""
import wxcbench.nonlocal_parameterization as nonlocal

# Step 1: Download ERA5 model level data
print("Step 1: Downloading ERA5 data...")
nonlocal.download_era5_modellevel_data(
    year=2020,
    month=1,
    start_day=1,
    end_day=31,
    output_dir='./ERA5_data_ml'
)

# Step 2: Compute momentum fluxes
print("Step 2: Computing momentum fluxes...")
nonlocal.compute_momentum_flux_from_era5(
    year=2020,
    month=1,
    era5_data_dir='./ERA5_data_ml',
    output_dir='./momentum_fluxes'
)

# Step 3: Coarse-grain to T42 grid
print("Step 3: Coarse-graining to T42 grid...")
nonlocal.coarsegrain_computed_momentum_fluxes(
    year=2020,
    start_month=1,
    end_month=1,
    t42_grid_file='./t42_lat_and_latb.nc',
    momentum_flux_dir='./momentum_fluxes',
    training_data_dir='./training_data'
)

print("Processing complete!")
""")

print("Nonlocal Parameterization workflow example complete!")
print("\nPrerequisites:")
print("  - CDS API credentials configured in ~/.cdsapirc")
print("  - T42 grid file for Step 3")
print("\nOutput directories:")
print("  - ./ERA5_data_ml/ (ERA5 model level data)")
print("  - ./momentum_fluxes/ (computed momentum fluxes)")
print("  - ./training_data/ (coarse-grained training data)")

