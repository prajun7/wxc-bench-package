# WxC-Bench Python Package

## Installation

```bash
pip install wxc-bench
```

## Usage

### Aviation Turbulence Module

The `aviation_turbulence` module provides a complete workflow for processing pilot reports (PIREPs) and preparing turbulence data for machine learning applications. Here's how to use each function:

#### Import the Module

```python
import wxcbench.aviation_turbulence as wab
```

#### 1. Download PIREP Data

**Function:** `get_pirep_data()`

**What it does:** Downloads historical pilot report (PIREP) data from Iowa State University archive (2003-present). The function:

- Creates URLs for monthly data downloads
- Downloads CSV files containing PIREP reports
- Removes duplicate reports and invalid entries
- Optionally combines all monthly files into a single `all_pireps.csv` file
- Creates a `pirep_downloads` folder containing monthly data files

**Parameters:**

- `start_year` (int, optional): Starting year for data download (default: 2003)
- `end_year` (int, optional): Ending year for data download. If None, uses current year (default: None)
- `output_dir` (str, optional): Directory to save downloaded files (default: `./pirep_downloads`)
- `combine_files` (bool, optional): If True, combines all files into `all_pireps.csv` (default: True)

**Example:**

```python
# Download PIREP data from 2020 to 2023
df = wab.get_pirep_data(start_year=2020, end_year=2023)
print(f"Downloaded {len(df)} PIREP records")
```

**Output:**

- Creates `pirep_downloads/` directory with monthly CSV files
- Creates `pirep_downloads/all_pireps.csv` (if `combine_files=True`)
- Returns a pandas DataFrame containing all PIREP data

---

#### 2. Preprocess Turbulence EDA

**Function:** `preprocess_turb_eda()`

**What it does:** Performs exploratory data analysis and preprocessing on PIREP data. The function:

- Adds new columns and filters data
- Categorizes reports by flight level (low, medium, high)
- Creates flight-level specific files: `low_fl.csv`, `med_fl.csv`, `high_fl.csv`
- Saves processed data to `updated_CSVs/csv_fl_rem.csv`

**Parameters:**

- `input_file` (str): Path to input CSV file (e.g., `'pirep_downloads/all_pireps.csv'`)
- `output_dir` (str, optional): Directory to save processed files (default: current directory)

**Example:**

```python
# Preprocess the downloaded PIREP data
df_processed = wab.preprocess_turb_eda('pirep_downloads/all_pireps.csv')
```

**Output:**

- Creates `updated_CSVs/` directory
- Creates `updated_CSVs/csv_fl_rem.csv` (processed data)
- Creates flight-level specific files: `low_fl.csv`, `med_fl.csv`, `high_fl.csv`
- Returns processed DataFrame

---

#### 3. Filter Moderate-or-Greater (MODG) Turbulence

**Function:** `preprocess_modg()`

**What it does:** Filters PIREP data for moderate-or-greater (MODG) turbulence reports. The function:

- Filters for reports indicating moderate or greater turbulence intensity
- Creates MODG-specific files: `low_fl_modg.csv`, `med_fl_modg.csv`, `high_fl_modg.csv`
- Saves filtered data to `updated_CSVs/csv_modg_all.csv`

**Parameters:**

- `input_file` (str): Path to input CSV file (e.g., `'updated_CSVs/csv_fl_rem.csv'`)
- `output_dir` (str, optional): Directory to save processed files (default: current directory)

**Example:**

```python
# Filter for MODG turbulence reports
df_modg = wab.preprocess_modg('updated_CSVs/csv_fl_rem.csv')
```

**Output:**

- Creates `updated_CSVs/csv_modg_all.csv` (all MODG reports)
- Creates MODG flight-level files: `low_fl_modg.csv`, `med_fl_modg.csv`, `high_fl_modg.csv`
- Returns filtered DataFrame

---

#### 4. Visualize PIREP Risk Map (Optional)

**Function:** `convert_to_risk_map()`

**What it does:** Visualizes the spatial distribution of PIREPs by creating a risk map. The function:

- Creates a visualization showing where turbulence reports are concentrated
- Generates a spatial distribution map of PIREP locations
- Helps understand geographic patterns of turbulence occurrence

**Parameters:**

- `input_file` (str): Path to input CSV file containing PIREP data
- `output_file` (str, optional): Path to save the visualization (default: `pirep_risk_map.png`)
- `**kwargs`: Additional keyword arguments for customization

**Example:**

```python
# Create a risk map visualization
wab.convert_to_risk_map('updated_CSVs/csv_fl_rem.csv', output_file='turbulence_risk_map.png')
```

**Output:**

- Creates a PNG image file showing PIREP spatial distribution

---

#### 5. Grid PIREPs onto MERRA-2 Grid

**Function:** `grid_pireps()`

**What it does:** Grids PIREP data onto the MERRA-2 atmospheric model grid. The function:

- Filters and bins PIREPs by day onto the MERRA-2 grid (0.625° x 0.5° resolution)
- Converts data to binary classification: 1 = turbulence present, 0 = no turbulence, 2 = no data
- Applies a threshold: cell is classified as turbulent if fraction of MOG reports ≥ threshold (default: 0.25)
- Creates daily NetCDF files organized by year and flight level

**Parameters:**

- `pirep_files` (List[str]): List of paths to PIREP CSV files (e.g., `['updated_CSVs/low_fl.csv', 'updated_CSVs/med_fl.csv']`)
- `output_dir` (str, optional): Directory to save gridded data (default: `./gridded_data`)
- `threshold` (float, optional): Fraction threshold for turbulence classification (default: 0.25)
- `nodata` (int, optional): Value for cells with no data (default: 2)

**Example:**

```python
# Grid PIREPs onto MERRA-2 grid
wab.grid_pireps(
    pirep_files=['updated_CSVs/low_fl.csv', 'updated_CSVs/med_fl.csv', 'updated_CSVs/high_fl.csv'],
    output_dir='./gridded_data',
    threshold=0.25
)
```

**Output:**

- Creates `gridded_data/` directory
- Creates NetCDF files: `YYYY_level_fl.nc` (e.g., `2023_low_fl.nc`)
- Each file contains daily gridded turbulence data with variables:
  - `Turbulence`: Binary turbulence presence (1=Yes, 0=No, 2=No data)
  - `Dates`: Date strings for each time step
  - `Lons`, `Lats`: Longitude and latitude grids

---

#### 6. Create Training Data

**Function:** `create_training_data()`

**What it does:** Extracts MERRA-2 atmospheric profiles matching turbulence detections from gridded PIREPs. The function:

- Matches turbulence locations from gridded PIREP data with MERRA-2 weather profiles
- Extracts 34-level atmospheric profiles (temperature, wind, humidity, pressure, etc.)
- Creates training data files for deep learning models
- Organizes data by flight level (low, med, high)

**Parameters:**

- `turbulence_dir` (str, optional): Directory containing gridded turbulence NetCDF files (default: `./gridded_data`)
- `merra2_dir` (str, required): Directory containing MERRA-2 data files
- `years` (List[int], optional): Years to process (default: `[2021, 2022]`)
- `levels` (List[str], optional): Flight levels to process (default: `['low', 'med', 'high']`)
- `output_dir` (str, optional): Directory to save training data (default: `./training_data`)

**Example:**

```python
# Create training data from gridded PIREPs and MERRA-2 profiles
wab.create_training_data(
    turbulence_dir='./gridded_data',
    merra2_dir='./MERRA2_2021-2022_1000hPa-100hPa',
    years=[2021, 2022],
    levels=['low', 'med', 'high'],
    output_dir='./training_data_20240126'
)
```

**Output:**

- Creates `training_data/` directory (or specified directory)
- Creates NetCDF files: `training_data_low_fl.nc`, `training_data_med_fl.nc`, `training_data_high_fl.nc`
- Each file contains:
  - `TURBULENCE`: Training labels (1=turbulence, 0=none)
  - `T`: Temperature profile (34 levels)
  - `U`, `V`: Wind velocity profiles (34 levels)
  - `OMEGA`: Vertical velocity profile (34 levels)
  - `RH`: Relative humidity profile (34 levels)
  - `H`: Height levels (34 levels)
  - `PL`: Pressure levels (34 levels)
  - `PHIS`: Surface geopotential

---

### Complete Workflow Example

Here's a complete example that demonstrates the full pipeline:

```python
import wxcbench.aviation_turbulence as wab

# Step 1: Download PIREP data
print("Step 1: Downloading PIREP data...")
df = wab.get_pirep_data(start_year=2020, end_year=2023)
print(f"Downloaded {len(df)} records")

# Step 2: Preprocess and categorize by flight level
print("Step 2: Preprocessing data...")
wab.preprocess_turb_eda('pirep_downloads/all_pireps.csv')

# Step 3: Filter for MODG turbulence (optional)
print("Step 3: Filtering MODG turbulence...")
wab.preprocess_modg('updated_CSVs/csv_fl_rem.csv')

# Step 4: Grid PIREPs onto MERRA-2 grid
print("Step 4: Gridding PIREPs...")
wab.grid_pireps(
    pirep_files=[
        'updated_CSVs/low_fl.csv',
        'updated_CSVs/med_fl.csv',
        'updated_CSVs/high_fl.csv'
    ],
    output_dir='./gridded_data'
)

# Step 5: Create training data
print("Step 5: Creating training data...")
wab.create_training_data(
    turbulence_dir='./gridded_data',
    merra2_dir='./MERRA2_2021-2022_1000hPa-100hPa',
    years=[2021, 2022],
    output_dir='./training_data'
)

print("Workflow complete!")
```

---

### Configuration

All default settings are built into the package and can be customized through function parameters. You don't need to edit any configuration files - simply pass the desired values as arguments when calling functions:

- **MERRA-2 Grid Parameters:** Grid resolution and dimensions (built-in defaults)
- **Turbulence Threshold:** Can be customized via `threshold` parameter in `grid_pireps()` (default: 0.25)
- **Flight Levels:** Can be customized via `levels` parameter in `create_training_data()` (default: ['low', 'med', 'high'])
- **Output Directories:** Can be customized via `output_dir` parameters in each function (defaults: `./pirep_downloads`, `./gridded_data`, `./training_data`)
