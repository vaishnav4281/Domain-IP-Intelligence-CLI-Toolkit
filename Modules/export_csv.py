# modules/export_csv.py

import csv
import os
from datetime import datetime

def save_to_csv(data_list, filename="data/output.csv"):
    if not data_list or not isinstance(data_list, list):
        print("❌ No data to export.")
        return

    # Ensure 'data/' folder exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    try:
        # Get all unique keys across the list of dictionaries
        keys = set()
        for item in data_list:
            keys.update(item.keys())
        fieldnames = sorted(keys)

        with open(filename, mode="w", newline='', encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in data_list:
                writer.writerow(row)

        print(f"✅ CSV saved successfully to: {filename}")

    except Exception as e:
        print(f"❌ Failed to write CSV: {e}")
