# modules/bulk_whois.py

from Modules import whois_lookup, export_csv
import os
from datetime import datetime

def calculate_domain_age(created_str, expires_str):
    try:
        created = datetime.strptime(created_str, "%Y-%m-%d")
        expires = datetime.strptime(expires_str, "%Y-%m-%d")
        delta = expires - created
        years = delta.days // 365
        months = (delta.days % 365) // 30
        days = (delta.days % 365) % 30
        return f"{years} years, {months} months, {days} days"
    except:
        return "N/A"

def run(file_path, export=False):
    print(f"\n📂 Bulk WHOIS Lookup from: {file_path}")
    print("-" * 50)

    if not os.path.isfile(file_path):
        print("❌ File not found.")
        return

    try:
        with open(file_path, "r") as f:
            domains = [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"❌ Failed to read file: {e}")
        return

    results = []
    failed_domains = []
    success_count = 0
    fail_count = 0

    total = len(domains)
    for i, domain in enumerate(domains, start=1):
        print(f"\n[{i}/{total}] → Checking: {domain}")
        result = whois_lookup.run(domain)

        # Remove 'status' if present
        result.pop("status", None)

        # Add domain age
        result["domain_age"] = calculate_domain_age(result.get("created", "-"), result.get("expires", "-"))

        results.append(result)

        if result["lookup_status"] == "Success":
            success_count += 1
        else:
            fail_count += 1
            failed_domains.append(domain)

    print("\n✅ Bulk WHOIS Scan Complete!")
    print("-" * 50)
    print(f"Total Domains       : {total}")
    print(f"Successful Lookups  : {success_count}")
    print(f"Failed Lookups      : {fail_count}")

    if export:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f"data/output_{timestamp}.csv"
        export_csv.save_to_csv(results, output_file)
        print(f"📁 CSV Exported to: {output_file}")

        if failed_domains:
            failed_file = f"data/failed_{timestamp}.txt"
            with open(failed_file, "w") as f:
                for domain in failed_domains:
                    f.write(domain + "\n")
            print(f"⚠️ Failed domains saved to: {failed_file}")
