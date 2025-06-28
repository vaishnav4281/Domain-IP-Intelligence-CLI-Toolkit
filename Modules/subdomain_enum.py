# modules/subdomain_enum.py

import requests
from bs4 import BeautifulSoup

def run(domain):
    print(f"\n🔍 Subdomain Enumeration via crt.sh for: {domain}")
    print("-" * 50)

    try:
        url = f"https://crt.sh/?q=%25.{domain}&output=json"
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            print(f"❌ Failed to fetch data. Status Code: {response.status_code}")
            return []

        json_data = response.json()
        subdomains = set()

        for entry in json_data:
            name = entry.get("name_value", "")
            for sub in name.split("\n"):
                if sub.endswith(domain):
                    subdomains.add(sub.strip())

        subdomains = sorted(subdomains)

        if subdomains:
            print(f"✅ Found {len(subdomains)} unique subdomains:")
            for sub in subdomains:
                print(f"  ➤ {sub}")
        else:
            print("⚠️ No subdomains found.")

        return list(subdomains)

    except Exception as e:
        print(f"❌ Error during subdomain enumeration: {e}")
        return []
