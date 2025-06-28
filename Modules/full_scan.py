# modules/full_scan.py

from Modules import whois_lookup, ip_info, risk_check, subdomain_enum, export_csv
import socket

def run(domains, export=True):
    results = []

    for i, domain in enumerate(domains, 1):
        print(f"\n[{i}/{len(domains)}] 🔍 Scanning: {domain}")
        result = {"domain": domain}

        # WHOIS
        whois = whois_lookup.run(domain)
        result.update(whois)

        # Resolve IP
        try:
            ip = socket.gethostbyname(domain)
            result["resolved_ip"] = ip
        except Exception as e:
            print(f"❌ DNS resolution failed: {e}")
            ip = None
            result["resolved_ip"] = "N/A"

        # IP Info
        if ip:
            ipdata = ip_info.run(ip)
            result.update(ipdata)

        # Risk Check
        if ip:
            abuse = risk_check.run(ip)
            result.update(abuse)

        # Subdomains
        subs = subdomain_enum.run(domain)
        result["subdomains_found"] = len(subs)
        result["subdomains"] = ", ".join(subs[:5])  # limit preview

        results.append(result)

    if export:
        output_path = "data/full_report.csv"
        export_csv.save_to_csv(results, output_path)

    return results
