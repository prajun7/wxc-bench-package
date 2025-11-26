"""
WxC-Bench: Multi-modal dataset toolkit for weather and climate downstream tasks
"""

from wxcbench.__version__ import __version__

__author__ = "Prajun Trital"
__license__ = "MIT"

from wxcbench import aviation_turbulence
from wxcbench import forecast_report_generation
from wxcbench import hurricane
from wxcbench import weather_analog
from wxcbench import long_term_precipitation_forecast
from wxcbench import nonlocal_parameterization

__all__ = [
    "aviation_turbulence",
    "forecast_report_generation",
    "hurricane",
    "weather_analog",
    "long_term_precipitation_forecast",
    "nonlocal_parameterization",
]
