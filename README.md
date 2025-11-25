# WxC-Bench Python Package Structure

```text
wxc-bench/
│
├── setup.py
├── setup.cfg
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
│   │   ├── data_acquisition.py         # get_pirep_data, download_merra2_data
│   │   ├── data_processing.py          # filter_pireps, categorize_by_altitude
│   │   ├── training_data.py            # create_training_data, generate_labels
│   │   ├── visualization.py            # plot_turbulence_patterns, visualize_risk
│   │   ├── grid_operations.py          # create_grids, spatial_matching
│   │   ├── utils.py                    # Helper functions
│   │   └── config.py                   # Configuration settings
│   │
│   ├── forecast_report_generation/
│   │   ├── __init__.py
│   │   ├── data_loader.py
│   │   ├── text_generation.py
│   │   ├── evaluation.py
│   │   └── utils.py
│   │
│   ├── gravity_wave/
│   │   ├── __init__.py
│   │   ├── data_loader.py
│   │   ├── flux_calculation.py
│   │   ├── parameterization.py
│   │   └── utils.py
│   │
│   ├── hurricane_tracking/
│   │   ├── __init__.py
│   │   ├── data_loader.py
│   │   ├── track_prediction.py
│   │   ├── intensity_prediction.py
│   │   └── visualization.py
│   │
│   ├── weather_analogs/
│   │   ├── __init__.py
│   │   ├── data_loader.py
│   │   ├── similarity_search.py
│   │   └── utils.py
│   │
│   ├── precipitation_forecast/
│   │   ├── __init__.py
│   │   ├── data_loader.py
│   │   ├── forecast.py
│   │   └── evaluation.py
│   │
│   ├── common/
│   │   ├── __init__.py
│   │   ├── data_utils.py              # Common data utilities
│   │   ├── io_utils.py                # File I/O operations
│   │   ├── constants.py               # Package-wide constants
│   │   └── exceptions.py              # Custom exceptions
│   │
│   └── cli/
│       ├── __init__.py
│       └── main.py                    # Command-line interface
│
├── tests/
│   ├── __init__.py
│   ├── test_aviation_turbulence/
│   │   ├── __init__.py
│   │   ├── test_data_acquisition.py
│   │   ├── test_data_processing.py
│   │   └── test_training_data.py
│   ├── test_forecast_report_generation/
│   └── test_common/
│
├── docs/
│   ├── index.md
│   ├── installation.md
│   ├── quickstart.md
│   ├── api/
│   │   ├── aviation_turbulence.md
│   │   ├── forecast_report_generation.md
│   │   └── ...
│   └── examples/
│       ├── aviation_turbulence_example.ipynb
│       └── ...
│
└── examples/
    ├── aviation_turbulence_workflow.py
    ├── forecast_generation_example.py
    └── complete_pipeline.py
```
