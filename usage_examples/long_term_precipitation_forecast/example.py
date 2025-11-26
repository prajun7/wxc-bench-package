"""
Long-Term Precipitation Forecast Module Example

This example demonstrates the usage of the long_term_precipitation_forecast module
for loading, preprocessing, evaluating, and visualizing precipitation forecast data.
"""

import numpy as np
import wxcbench.long_term_precipitation_forecast as precip

# Step 1: Load precipitation data
print("Step 1: Loading precipitation data...")
print("Note: This example uses placeholder data - replace with actual file paths")
print("""
# Example: Load precipitation forecast data
forecast_data = precip.load_precipitation_data('path/to/forecast_file.nc')

# Example: Load satellite observations
observation_data = precip.load_satellite_observations('path/to/observation_file.nc')
""")
print()

# Step 2: Combine observations
print("Step 2: Combining observations...")
print("""
# Example: Combine multiple observation files
combined_obs = precip.combine_observations(
    obs_files=['obs1.nc', 'obs2.nc', 'obs3.nc'],
    n_days=8
)
""")
print()

# Step 3: Regrid to MERRA grid
print("Step 3: Regridding to MERRA grid...")
print("""
# Example: Regrid precipitation data to MERRA grid
regridded_data = precip.regrid_to_merra(
    data=forecast_data['precipitation'],
    target_grid=precip.MERRA_GRID
)
""")
print()

# Step 4: Normalize data
print("Step 4: Normalizing data...")
# Create sample data for demonstration
sample_data = np.random.rand(100, 100) * 10  # Sample precipitation data

normalized = precip.normalize_data(sample_data, method='standard')
print(f"Normalized data shape: {normalized.shape}")
print(f"Normalized data stats: mean={normalized.mean():.3f}, std={normalized.std():.3f}")
print()

# Step 5: Compute evaluation metrics
print("Step 5: Computing evaluation metrics...")
# Create sample predictions and observations
predictions = np.random.rand(100, 100) * 10
observations = predictions + np.random.randn(100, 100) * 0.5  # Add some noise

bias = precip.compute_bias(predictions, observations)
mse = precip.compute_mse(predictions, observations)
rmse = precip.compute_rmse(predictions, observations)
correlation = precip.compute_correlation(predictions, observations)
mae = precip.compute_mae(predictions, observations)

print(f"Bias: {bias:.4f}")
print(f"MSE: {mse:.4f}")
print(f"RMSE: {rmse:.4f}")
print(f"Correlation: {correlation:.4f}")
print(f"MAE: {mae:.4f}")
print()

# Step 6: Evaluate forecasts comprehensively
print("Step 6: Comprehensive forecast evaluation...")
# Create sample forecast data with multiple lead times
forecast_array = np.random.rand(28, 100, 100) * 10  # 28 lead times
observation_array = forecast_array + np.random.randn(28, 100, 100) * 0.5
lead_times = list(range(1, 29))  # Days 1-28

results = precip.evaluate_forecasts(
    forecasts=forecast_array,
    observations=observation_array,
    lead_times=lead_times,
    metrics=['bias', 'mse', 'rmse', 'correlation', 'mae']
)

print(f"Evaluation results for {len(lead_times)} lead times:")
print(f"  Bias range: {np.min(results['bias']):.4f} to {np.max(results['bias']):.4f}")
print(f"  RMSE range: {np.min(results['rmse']):.4f} to {np.max(results['rmse']):.4f}")
print(f"  Correlation range: {np.min(results['correlation']):.4f} to {np.max(results['correlation']):.4f}")
print()

# Step 7: Visualize results
print("Step 7: Creating visualizations...")
print("Note: Uncomment and provide actual data paths to create plots")
print("""
# Example: Plot precipitation comparison
precip.plot_precipitation_comparison(
    forecast=forecast_array[7, :, :],  # 7-day lead time
    observation=observation_array[7, :, :],
    lead_time=7,
    output_file='precipitation_comparison_7day.png'
)

# Example: Plot evaluation metrics
precip.plot_evaluation_metrics(
    metrics_dict=results,
    output_file='evaluation_metrics.png'
)

# Example: Plot spatial distribution
precip.plot_spatial_distribution(
    data=forecast_array[0, :, :],
    title='Precipitation Forecast - Day 1',
    lons=np.linspace(-180, 180, 100),
    lats=np.linspace(-60, 60, 100),
    output_file='spatial_distribution.png'
)
""")

print("Long-Term Precipitation Forecast workflow example complete!")
print("\nNote: Replace placeholder code with actual data file paths to run full workflow")

