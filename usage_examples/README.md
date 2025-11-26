# Usage Examples

This directory contains example scripts demonstrating how to use each module in the `wxcbench` package.

## Directory Structure

```
usage_examples/
├── README.md
├── aviation_turbulence/
│   └── example.py
├── forecast_report_generation/
│   └── example.py
├── hurricane/
│   └── example.py
├── long_term_precipitation_forecast/
│   └── example.py
├── nonlocal_parameterization/
│   └── example.py
└── weather_analog/
    └── example.py
```

## How to Run Examples

### Prerequisites

1. Install the package:
   ```bash
   pip install wxcbench
   ```

2. Navigate to the specific module directory:
   ```bash
   cd usage_examples/[module_name]
   ```

3. Run the example:
   ```bash
   python example.py
   ```

## Module Examples

### 1. Aviation Turbulence (`aviation_turbulence/example.py`)

Demonstrates the complete pipeline for processing PIREP data:
- Download PIREP data
- Preprocess and categorize by flight level
- Filter MODG turbulence
- Create risk map visualization
- Grid PIREPs onto MERRA-2 grid
- Create training data

**Run:**
```bash
cd usage_examples/aviation_turbulence
python example.py
```

**Note:** Step 6 (create training data) requires MERRA2 data files.

---

### 2. Forecast Report Generation (`forecast_report_generation/example.py`)

Demonstrates downloading HRRR data and creating metadata:
- Scrape weather reports from SPC
- Download HRRR weather data
- Create metadata file pairing HRRR files with reports

**Run:**
```bash
cd usage_examples/forecast_report_generation
python example.py
```

---

### 3. Hurricane (`hurricane/example.py`)

Demonstrates hurricane track and intensity visualization:
- Plot hurricane intensity time series
- Plot hurricane tracks on maps
- Plot entire hurricane seasons

**Run:**
```bash
cd usage_examples/hurricane
python example.py
```

**Output:** Creates figures in `./hurricane_figures/` directory.

---

### 4. Long-Term Precipitation Forecast (`long_term_precipitation_forecast/example.py`)

Demonstrates precipitation forecast evaluation:
- Load and preprocess precipitation data
- Compute evaluation metrics (bias, MSE, RMSE, correlation, MAE)
- Visualize precipitation comparisons
- Evaluate forecasts across multiple lead times

**Run:**
```bash
cd usage_examples/long_term_precipitation_forecast
python example.py
```

**Note:** Some visualization examples require actual data files (commented out in example).

---

### 5. Nonlocal Parameterization (`nonlocal_parameterization/example.py`)

Demonstrates ERA5 data processing pipeline:
- Download ERA5 model level data
- Compute momentum fluxes using Helmholtz decomposition
- Coarse-grain to T42 grid

**Run:**
```bash
cd usage_examples/nonlocal_parameterization
python example.py
```

**Prerequisites:**
- CDS API credentials configured in `~/.cdsapirc`
- T42 grid file for Step 3

**Note:** Downloading ERA5 data can take significant time.

---

### 6. Weather Analog (`weather_analog/example.py`)

Demonstrates MERRA2 data processing:
- Process single MERRA2 files
- Batch process MERRA2 data for time periods
- Extract variables for specific geographic regions

**Run:**
```bash
cd usage_examples/weather_analog
python example.py
```

**Prerequisites:**
- MERRA2 data files in the input directory
- Files should follow naming pattern: `MERRA2*.{date}.SUB.nc`

---

## Tips

1. **Read the examples first:** Each example contains comments explaining what each step does.

2. **Check prerequisites:** Some examples require external data or API credentials.

3. **Start with simple examples:** The `hurricane` module example is good to start with as it doesn't require external data downloads.

4. **Customize parameters:** All examples use default parameters - feel free to modify them for your use case.

5. **Output directories:** Most examples create output directories in the current working directory. Check the example scripts for specific output paths.

## Troubleshooting

- **Import errors:** Make sure `wxcbench` is installed: `pip install wxcbench`
- **Missing data:** Some examples require external data files - check the comments in each example
- **API credentials:** Modules like `nonlocal_parameterization` require CDS API setup
- **File paths:** Adjust file paths in examples to match your local directory structure

