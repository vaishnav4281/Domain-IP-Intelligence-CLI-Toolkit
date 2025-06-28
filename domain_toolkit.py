# domain_toolkit.py

import argparse
from Modules import whois_lookup, dns_lookup, ip_info, risk_check, subdomain_enum, bulk_whois

def main():
    parser = argparse.ArgumentParser(description="🔍 Domain & IP Intelligence CLI Toolkit")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # WHOIS Command
    whois_cmd = subparsers.add_parser("whois", help="Perform WHOIS lookup")
    whois_cmd.add_argument("domain", help="Domain name to query")

    # DNS Command
    dns_cmd = subparsers.add_parser("dns", help="Fetch DNS records")
    dns_cmd.add_argument("domain", help="Domain name to query")

    # IP Info Command
    ip_cmd = subparsers.add_parser("ipinfo", help="Get IP geolocation and risk info")
    ip_cmd.add_argument("ip", help="IP address to query")

    # Subdomain Enumeration
    sub_cmd = subparsers.add_parser("subdomains", help="Find subdomains via crt.sh")
    sub_cmd.add_argument("domain", help="Domain name to query")

    # Bulk WHOIS
    bulk_cmd = subparsers.add_parser("bulk", help="Perform WHOIS for a list of domains")
    bulk_cmd.add_argument("file", help="Text file with domains (one per line)")
    bulk_cmd.add_argument("--export", action="store_true", help="Export result as CSV")

    args = parser.parse_args()

    if args.command == "whois":
        whois_lookup.run(args.domain)

    elif args.command == "dns":
        dns_lookup.run(args.domain)

    elif args.command == "ipinfo":
        ip_info.run(args.ip)
        risk_check.run(args.ip)

    elif args.command == "subdomains":
        subdomain_enum.run(args.domain)

    elif args.command == "bulk":
        bulk_whois.run(args.file, args.export)

if __name__ == "__main__":
    main()
