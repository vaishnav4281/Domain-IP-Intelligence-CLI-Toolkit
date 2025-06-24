# modules/dns_lookup.py

import dns.resolver

def run(domain):
    print(f"\n📡 DNS Records for: {domain}")
    print("-" * 50)

    record_types = ["A", "MX", "NS", "TXT"]

    for rtype in record_types:
        try:
            answers = dns.resolver.resolve(domain, rtype)
            print(f"{rtype} Records:")
            for rdata in answers:
                if rtype == "MX":
                    print(f"  ➤ {rdata.exchange} (Priority {rdata.preference})")
                else:
                    print(f"  ➤ {rdata.to_text()}")
        except dns.resolver.NoAnswer:
            print(f"  ➤ No {rtype} record found.")
        except dns.resolver.NXDOMAIN:
            print(f"  ❌ Domain does not exist.")
            break
        except Exception as e:
            print(f"  ❌ Error fetching {rtype} record: {e}")
