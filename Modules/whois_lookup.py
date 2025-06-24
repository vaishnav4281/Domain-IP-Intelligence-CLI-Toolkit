import whois
from datetime import datetime

def run(domain):
    print(f"\n🔍 WHOIS Lookup for: {domain}")
    print("-" * 50)

    try:
        result = whois.whois(domain)

        registrar = result.registrar or "N/A"
        creation_date = format_date(result.creation_date)
        expiration_date = format_date(result.expiration_date)
        name_servers = ", ".join(result.name_servers) if result.name_servers else "N/A"

        print(f"Registrar       : {registrar}")
        print(f"Created On      : {creation_date}")
        print(f"Expires On      : {expiration_date}")
        print(f"Name Servers    : {name_servers}")

        return {
            "domain": domain,
            "lookup_status": "Success",
            "registrar": registrar,
            "created": creation_date,
            "expires": expiration_date,
            "name_servers": name_servers
            # No status field anymore; domain_age added in bulk_whois
        }

    except Exception as e:
        print(f"❌ WHOIS Lookup Failed: {e}")
        return {
            "domain": domain,
            "lookup_status": "Failed",
            "registrar": "-",
            "created": "-",
            "expires": "-",
            "name_servers": "-"
        }

def format_date(date_obj):
    if isinstance(date_obj, list):  # some WHOIS APIs return a list
        date_obj = date_obj[0]
    if isinstance(date_obj, datetime):
        return date_obj.strftime("%Y-%m-%d")
    return "-"
