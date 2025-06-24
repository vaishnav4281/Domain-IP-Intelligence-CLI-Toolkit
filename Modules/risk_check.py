# modules/risk_check.py

import requests
import os

def run(ip):
    print(f"\n🛡️ Risk Check (AbuseIPDB) for: {ip}")
    print("-" * 50)

    api_key = os.getenv("ABUSEIPDB_API_KEY")
    if not api_key:
        print("❌ ABUSEIPDB_API_KEY not found in environment.")
        return {}

    try:
        url = "https://api.abuseipdb.com/api/v2/check"
        headers = {
            "Key": api_key,
            "Accept": "application/json"
        }
        params = {
            "ipAddress": ip,
            "maxAgeInDays": 90
        }

        response = requests.get(url, headers=headers, params=params, timeout=5)
        data = response.json()["data"]

        print(f"Abuse Score     : {data.get('abuseConfidenceScore')}%")
        print(f"Country         : {data.get('countryCode')}")
        print(f"ISP             : {data.get('isp')}")
        print(f"Usage Type      : {data.get('usageType')}")
        print(f"Domain          : {data.get('domain')}")
        print(f"Total Reports   : {data.get('totalReports')}")
        print(f"Last Reported   : {data.get('lastReportedAt') or 'Never'}")

        is_proxy = "proxy" in (data.get("usageType") or "").lower()
        is_vpn    = "vpn" in (data.get("usageType") or "").lower()

        if is_proxy or is_vpn:
            print("⚠️ Possible VPN or Proxy Detected!")
        else:
            print("✅ No VPN/Proxy activity detected.")

        return {
            "ip": ip,
            "abuse_score": data.get("abuseConfidenceScore", 0),
            "total_reports": data.get("totalReports", 0),
            "last_reported": data.get("lastReportedAt", "-"),
            "usage_type": data.get("usageType", "-"),
            "is_vpn_or_proxy": is_proxy or is_vpn,
            "status": "Success"
        }

    except Exception as e:
        print(f"❌ Risk check failed: {e}")
        return {
            "ip": ip,
            "status": "Failed"
        }
