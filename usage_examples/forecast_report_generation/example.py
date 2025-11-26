"""
Forecast Report Generation Module Example

This example demonstrates the usage of the forecast_report_generation module
to scrape weather reports, download HRRR data, and create metadata files.
"""

import wxcbench.forecast_report_generation as frg

# Step 1: Scrape weather reports from SPC
print("Step 1: Scraping weather reports from SPC...")
print("Note: Scraping data for a single date range")
df_reports = frg.scrape_weather_reports(
    start_date="2021-06-27",
    end_date="2021-06-27",
    output_dir="./csv_reports"
)
print(f"Scraped {len(df_reports)} reports")
print(f"Reports saved to: ./csv_reports/")
print()

# Step 2: Download HRRR weather data
print("Step 2: Downloading HRRR data...")
print("Note: Downloading analysis files (forecast hour 0) for a single day")
frg.download_hrrr(
    start_date="20180101-01",
    end_date="20180102-01",
    forecast_hours=[0],
    dataset_type="nat",
    output_dir="./hrrr"
)
print("HRRR data download complete!")
print(f"HRRR files saved to: ./hrrr/")
print()

# Step 3: Create metadata file
print("Step 3: Creating metadata file...")
df_metadata = frg.create_metadata(
    image_dir="./hrrr",
    caption_dir="./csv_reports",
    output_file="./metadata.csv"
)
print(f"Created metadata with {len(df_metadata)} entries")
print(f"Metadata saved to: ./metadata.csv")
print()

print("Forecast Report Generation workflow complete!")
print("\nOutput files created:")
print("  - ./csv_reports/ (weather report CSVs)")
print("  - ./hrrr/ (HRRR grib2 files)")
print("  - ./metadata.csv (paired metadata)")

