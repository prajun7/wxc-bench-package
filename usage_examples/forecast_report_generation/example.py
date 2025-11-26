"""
Forecast Report Generation Module Example

This example demonstrates the usage of the forecast_report_generation module
to scrape weather reports, download HRRR data, and create metadata files.
"""

import wxcbench.forecast_report_generation as frg

# Step 1: Scrape weather reports from SPC
print("Step 1: Scraping weather reports from SPC...")
print("Note: Scraping data for a single date range")
print("Note: Some URLs may return 404 if data is not available")
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
print("Note: SSL certificate errors may occur - this is a network/SSL config issue")
import os
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
# Check if we have any files to process
hrrr_files = [f for f in os.listdir("./hrrr") if f.endswith('.grib2')] if os.path.exists("./hrrr") else []
csv_files = [f for f in os.listdir("./csv_reports") if f.endswith('.csv')] if os.path.exists("./csv_reports") else []

if not hrrr_files and not csv_files:
    print("WARNING: No data files found!")
    print("  - HRRR files: 0 found")
    print("  - CSV report files: 0 found")
    print("  This is likely because:")
    print("    1. Data downloads failed (SSL certificate errors)")
    print("    2. Data not available on server (404 errors)")
    print("    3. Network connectivity issues")
    print("\nSkipping metadata creation...")
    print("\nTo fix SSL certificate issues:")
    print("  - Update SSL certificates on your system")
    print("  - Or configure Python SSL settings")
    print("  - Or use a different network/VPN")
else:
    try:
        df_metadata = frg.create_metadata(
            image_dir="./hrrr",
            caption_dir="./csv_reports",
            output_file="./metadata.csv"
        )
        print(f"Created metadata with {len(df_metadata)} entries")
        print(f"Metadata saved to: ./metadata.csv")
    except ValueError as e:
        print(f"ERROR: {e}")
        print("This usually means no matching files were found to create metadata.")
print()

print("Forecast Report Generation workflow complete!")
print("\nOutput files created:")
print("  - ./csv_reports/ (weather report CSVs)")
print("  - ./hrrr/ (HRRR grib2 files)")
print("  - ./metadata.csv (paired metadata)")

