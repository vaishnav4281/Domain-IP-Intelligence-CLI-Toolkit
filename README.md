# 🔍 Domain & IP Intelligence CLI Toolkit

A fully modular and extensible **Command-Line Reconnaissance Tool** that scans domains for **WHOIS data, DNS records, IP reputation, geolocation, VPN detection**, and more — with **CSV reporting** and **bulk scanning** capability.

> 🎯 Built with Python by **Vaishnav K**  
> 🔓 Powered by Open Source & Free APIs

---

## ✨ Key Features

✅ **WHOIS Lookup** – Registrar, creation/expiration date, name servers  
🌐 **DNS Records** – A, MX, NS, TXT records  
🌍 **IP Geolocation & ASN** – ISP, region, org, timezone  
🧠 **Abuse Detection** – Score, report count, last seen (via AbuseIPDB)  
🛰️ **VPN/Proxy Detection** – Usage type and anonymity check  
🔍 **Subdomain Discovery** – Using public certificate logs (crt.sh)  
📦 **Bulk Domain Input** – Accepts `.txt` lists  
📊 **CSV Reporting** – With domain age: years, months, days  
📁 **Failed Lookup Logging** – Easily trace failed scans  
💯 **Open Source & Free APIs** – No paid services required

---

## 📁 Project Structure

```

domain-intel-cli/
├── domain\_toolkit.py            # Main CLI controller
├── modules/
│   ├── whois\_lookup.py          # WHOIS logic
│   ├── dns\_lookup.py            # DNS record fetcher
│   ├── ip\_info.py               # Geolocation, ASN
│   ├── risk\_check.py            # AbuseIPDB risk analysis
│   ├── subdomain\_enum.py        # crt.sh subdomain parser
│   ├── bulk\_whois.py            # Domain age + bulk scanner
│   └── export\_csv.py            # CSV writer
├── data/
│   └── output\_<timestamp>.csv   # Final reports
│   └── failed\_<timestamp>.txt   # Failed lookups
├── inputs/
│   └── domains.txt              # Domain list input
├── .env                         # API keys (e.g., AbuseIPDB)
└── README.md

````

---

## 📂 Example Output Summary

```bash
✅ Bulk WHOIS Scan Complete!
--------------------------------------------------
📦 Total Domains Scanned    : 56
✅ Successful Lookups        : 52
❌ Failed Lookups            : 4

📁 CSV Report Saved To       : data/output_20250624_125057.csv
⚠️  Failed Domains Logged To : data/failed_20250624_125057.txt
🕒 Scan Timestamp            : 2025-06-24 12:50:57
````

---

## 🧾 Sample CSV Output (Columns)

| domain     | created    | expires    | domain\_age                | registrar         | name\_servers          | abuse\_score | is\_vpn\_or\_proxy | subdomains        |
| ---------- | ---------- | ---------- | -------------------------- | ----------------- | ---------------------- | ------------ | ------------------ | ----------------- |
| google.com | 1997-09-15 | 2028-09-14 | 31 years, 0 months, 7 days | MarkMonitor, Inc. | ns1.google.com, ns2... | 0            | False              | mail, drive, etc. |
| github.com | 2007-10-09 | 2026-10-09 | 19 years, 0 months, 5 days | MarkMonitor, Inc. | dns1.p08.nsone.net...  | 3            | True               | api, gist, docs   |

---

## 🛠 Setup & Usage

### 1️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Create `.env` file for API keys

```
ABUSEIPDB_API_KEY=your_api_key_here
```

### 3️⃣ Add domains to `inputs/domains.txt`

```txt
google.com
github.com
invalid.com
```

### 4️⃣ Run the CLI Tool

```bash
python domain_toolkit.py bulk inputs/domains.txt --export
```

### 5️⃣ Check output

* ✅ CSV: `data/output_<timestamp>.csv`
* ❌ Failed: `data/failed_<timestamp>.txt`

---

## 🧠 APIs & Libraries Used

| Function            | Source/API                                               |
| ------------------- | -------------------------------------------------------- |
| WHOIS Lookup        | [`python-whois`](https://pypi.org/project/python-whois/) |
| DNS Records         | `dnspython`, `socket`                                    |
| Geolocation/IP Info | [`ipapi.co`](https://ipapi.co/) or `ipinfo.io`           |
| VPN/Proxy Check     | [`ipqualityscore.com`](https://www.ipqualityscore.com/)  |
| Risk/Abuse Reports  | [`AbuseIPDB`](https://abuseipdb.com/)                    |
| Subdomains          | `crt.sh` scraping (public logs)                          |
| CSV Export          | `csv`, `datetime`, Python built-in                       |

---

## ✅ Use Cases

* OSINT for cybersecurity analysis
* Blacklist cleanup and domain monitoring
* DNS or hosting provider audit
* Research on expired or suspicious domains
* Recon during bug bounty or CTF

---

## 👤 Author

**Vaishnav K**
📧 Email: [k.vaishnav.ae@gmail.com](mailto:k.vaishnav.ae@gmail.com)
🌐 GitHub: [github.com/vaishnav4281](https://github.com/vaishnav4281)

---

## 📜 License

**MIT License**
Free for personal, academic, and commercial use — credit appreciated!

---

## 🌟 Future Roadmap

* [ ] Flask/Django REST API version
* [ ] Web UI in Next.js
* [ ] Historical WHOIS record lookup
* [ ] PDF/HTML export for reports
* [ ] Dashboard visualizer for reports

---

## 🙌 Contributing

Pull requests are welcome!

```bash
# GitHub Setup
git init
git remote add origin https://github.com/vaishnav4281/Domain-IP-Intelligence-CLI-Toolkit.git
git add .
git commit -m "Initial commit"
git push -u origin master
```

---

📁 Need help pushing the code?
📦 Want a zipped release?
🧪 Ready to build the Next.js frontend?

Let me know and I’ll help with next steps!

```

---

✅ I can now:
- Save this as a `README.md` file  
- Export your full project as `.zip` with this README  
- Scaffold a GitHub repository push-ready  
- Start building the Next.js frontend

Would you like the zip + README exported now?
```
