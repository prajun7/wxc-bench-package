"""
Hurricane Module Example

This example demonstrates the usage of the hurricane module
to visualize hurricane tracks and intensities.
"""

import wxcbench.hurricane as hurricane

# Step 1: Plot intensity for multiple hurricanes
print("Step 1: Plotting hurricane intensities...")
print("Plotting intensity for Hurricane Harvey (2017)...")
hurricane.plot_intensity(name='harvey', year=2017, start=2, output_dir='./hurricane_figures')
print("Plotting intensity for Hurricane Laura (2020)...")
hurricane.plot_intensity(name='laura', year=2020, start=2, output_dir='./hurricane_figures')
print("Plotting intensity for Hurricane Michael (2018)...")
hurricane.plot_intensity(name='michael', year=2018, start=2, output_dir='./hurricane_figures')
print()

# Step 2: Plot tracks for specific hurricanes
print("Step 2: Plotting hurricane tracks...")
print("Plotting track for Hurricane Harvey (2017)...")
hurricane.plot_track(storm_name='harvey', year=2017, output_dir='./hurricane_figures')
print("Plotting track for Hurricane Laura (2020)...")
hurricane.plot_track(storm_name='laura', year=2020, output_dir='./hurricane_figures')
print()

# Step 3: Plot entire season
print("Step 3: Plotting 2017 Atlantic hurricane season...")
hurricane.plot_track(year=2017, output_dir='./hurricane_figures')
print()

# Step 4: Plot with custom domain
print("Step 4: Plotting 2020 season with custom domain...")
hurricane.plot_track(
    year=2020,
    domain_bb=[-100, -60, 20, 40],  # Custom bounding box
    output_dir='./hurricane_figures'
)
print()

print("Hurricane analysis complete!")
print("\nOutput figures saved to: ./hurricane_figures/")
print("Files created:")
print("  - Intensity_HARVEY_2017.jpeg")
print("  - Intensity_LAURA_2020.jpeg")
print("  - Intensity_MICHAEL_2018.jpeg")
print("  - Track_HARVEY_2017.png")
print("  - Track_LAURA_2020.png")
print("  - Track_SEASON_2017.png")
print("  - Track_SEASON_2020.png")

