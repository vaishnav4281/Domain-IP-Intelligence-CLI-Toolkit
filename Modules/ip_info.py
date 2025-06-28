# modules/ip_info.py

import requests

def run(ip):
    print(f"\n🌍 IP Intelligence for: {ip}")
    print("-" * 50)

    try:
        url = f"http://ip-api.com/json/{ip}"
        response = requests.get(url, timeout=5)
        data = response.json()

        if data["status"] != "success":
            print("❌ IP lookup failed.")
            return {}

        print(f"Country         : {data.get('country', '-')}")
        print(f"Region          : {data.get('regionName', '-')}")
        print(f"City            : {data.get('city', '-')}")
        print(f"ISP             : {data.get('isp', '-')}")
        print(f"Organization    : {data.get('org', '-')}")
        print(f"ASN             : {data.get('as', '-')}")
        print(f"Timezone        : {data.get('timezone', '-')}")
        print(f"Latitude/Long   : {data.get('lat', '-')}, {data.get('lon', '-')}")

        return {
            "ip": ip,
            "country": data.get("country", "-"),
            "region": data.get("regionName", "-"),
            "city": data.get("city", "-"),
            "isp": data.get("isp", "-"),
            "asn": data.get("as", "-"),
            "org": data.get("org", "-"),
            "timezone": data.get("timezone", "-"),
            "latitude": data.get("lat", "-"),
            "longitude": data.get("lon", "-"),
            "lookup_status": "Success"
        }

    except Exception as e:
        print(f"❌ Error: {e}")
        return {
            "ip": ip,
            "lookup_status": "Failed"
        }
