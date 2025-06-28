import whois
from datetime import datetime
from dateutil.relativedelta import relativedelta

def run(domain):
    print(f"WHOIS Lookup for: {domain}")
    print("-" * 50)

    try:
        result = whois.whois(domain)

        registrar = result.registrar or "N/A"
        creation_date = format_date(result.creation_date)
        expiration_date = format_date(result.expiration_date)
        name_servers = ", ".join(result.name_servers) if result.name_servers else "N/A"

        # Calculate domain age
        if creation_date != "-":
            created = datetime.strptime(creation_date, "%Y-%m-%d")
            current_date = datetime.now()
            delta = relativedelta(current_date, created)
            years = delta.years
            months = delta.months
            days = delta.days
            
            age_parts = []
            if years > 0:
                age_parts.append(f"{years} year{'s' if years > 1 else ''}")
            if months > 0 or (years == 0 and days > 0):
                age_parts.append(f"{months} month{'s' if months > 1 else ''}")
            if days > 0 or (years == 0 and months == 0):
                age_parts.append(f"{days} day{'s' if days > 1 else ''}")
                
            domain_age = " and ".join(age_parts)
        else:
            domain_age = "N/A"

        print(f"Registrar       : {registrar}")
        print(f"Created On      : {creation_date}")
        print(f"Domain Age      : {domain_age}")
        print(f"Expires On      : {expiration_date}")
        print(f"Name Servers    : {name_servers}")

        return {
            "domain": domain,
            "lookup_status": "Success",
            "registrar": registrar,
            "created": creation_date,
            "expires": expiration_date,
            "name_servers": name_servers,
            "domain_age": domain_age
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
