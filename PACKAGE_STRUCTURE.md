# WxC-Bench Python Package Structure

```text
wxc-bench/
│
├── setup.py
├── MANIFEST.in
├── pyproject.toml
├── README.md
├── LICENSE
├── requirements.txt
├── .gitignore
│
├── wxcbench/
│   ├── __init__.py
│   ├── __version__.py
│   │
│   ├── aviation_turbulence/
│   │   ├── __init__.py
│   │   ├── PIREP_downloads.py
│   │   ├── convert2risk_map.py
│   │   ├── grid_pireps.py
│   │   ├── make_training_data.py
│   │   ├── modg_preprocess.py
│   │   ├── turb_eda_preprocessing.py
│   │   └── config.py
│   │
│   ├── forecast_report_generation/
│   │   ├── __init__.py
│   │   ├── create_metadata.py
│   │   ├── download_hrrr.py
│   │   └── weather_report_data_scraping.py
│   │
│   ├── hurricane/
│   │   ├── __init__.py
│   │   ├── hurricane_intensity.py
│   │   └── hurricane_track.py
│   │
│   ├── long_term_precipitation_forecast/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── evaluation.py
│   │   ├── data_loading.py
│   │   ├── preprocessing.py
│   │   └── visualization.py
│   │
│   ├── nonlocal_parameterization/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── download_era5.py
│   │   ├── compute_momentum_flux.py
│   │   └── coarsegrain_fluxes.py
│   │
│   └── weather_analog/
│       ├── __init__.py
│       ├── config.py
│       └── preprocess_weather_analog.py
│
└── usage/
    ├── aviation_turbulence_workflow.py
    ├── forecast_generation_example.py
    └── complete_pipeline.py
```
