# Reflected XSS Vulnerability Scanner

A lightweight Python-based scanner for detecting reflected Cross-Site Scripting (XSS) vulnerabilities in web applications. Designed for educational purposes and authorized security testing only.

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Requests](https://img.shields.io/badge/requests-2.25%2B-orange)](https://docs.python-requests.org/)


   
## Legal Disclaimer

**This tool is for educational and authorized testing purposes only.**  
Unauthorized scanning of websites or applications you do not own or have explicit permission to test is illegal and unethical. The developers assume no liability and are not responsible for any misuse or damage caused by this program.

## Features
  
- **Parameter-Based Scanning**: Automatically identifies and tests URL query parameters
- **Multiple Payload Testing**: Includes a comprehensive list of common XSS payloads
- **Reflection Detection**: Checks if injected payloads are reflected in server responses
- **Automated Reporting**: Generates detailed reports of findings with proof-of-concept payloads
- **Error Handling**: Gracefully handles connection timeouts and request failures
- **User Confirmation**: Requires explicit permission confirmation before scanning

## Prerequisites

- Python 3.6 or higher
- `requests` library

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/xss-vulnerability-scanner.git
   cd xss-vulnerability-scanner
   ```

2. **Install required dependencies**
   ```bash
   pip install requests
   ```

## Usage

### Basic Usage

1. **Run the scanner**
   ```bash
   python xss_scanner.py
   ```

2. **Enter the target URL** when prompted
   ```
   Enter the full URL with parameters to scan: http://example.com/page?param1=value1&param2=value2
   ```

3. **Confirm authorization**
   ```
   [!] LEGAL NOTICE: You must have explicit permission to test this target.
   Do you have permission? (yes/no): yes
   ```

4. **View results** - The scanner will display findings in real-time and save them to `xss_report.txt`

### Example Output

```
Simple Reflected XSS Scanner
Use only against authorized targets like DVWA.

Enter the full URL with parameters to scan: http://testphp.vulnweb.com/search.php?test=query

[*] Testing URL: http://testphp.vulnweb.com/search.php?test=query
    [!] POTENTIAL XSS FOUND on parameter: test
        Payload: <script>alert('XSS')</script>

[+] Report saved to xss_report.txt
```

### Sample Report (`xss_report.txt`)

```
Reflected XSS Vulnerability Report
========================================
URL: http://testphp.vulnweb.com/search.php?test=query
Vulnerable Parameter: test
Proof-of-Concept Payload: <script>alert('XSS')</script>
--------------------
```

## Configuration

### Customizing Payloads

You can modify the `XSS_PAYLOADS` list in the script to add or remove test payloads:

```python
XSS_PAYLOADS = [
    "<script>alert('XSS')</script>",
    "<img src=x onerror=alert(1)>",
    "javascript:alert('XSS')",
    # Add your custom payloads here
]
```

### Adjusting Request Settings

Modify the request parameters in the `scan_url_for_xss` function:

```python
# Change timeout (default: 5 seconds)
response = requests.get(test_url, timeout=10, headers=headers)

# Modify User-Agent
headers = {'User-Agent': 'Custom-Scanner/1.0'}
```

## Supported Targets

This scanner is designed for testing against:
- **DVWA (Damn Vulnerable Web Application)**
- **bWAPP (Buggy Web Application)**
- **WebGoat**
- **Other deliberately vulnerable applications**
- **Your own web applications** (with proper authorization)

## How It Works

1. **URL Parsing**: Extracts query parameters from the target URL
2. **Payload Injection**: Iteratively injects XSS payloads into each parameter
3. **Request Sending**: Sends HTTP GET requests with modified parameters
4. **Response Analysis**: Checks if payloads are reflected in the HTML response
5. **Reporting**: Records vulnerable parameters with proof-of-concept payloads

## Limitations

- **GET requests only**: Does not test POST parameters or form submissions
- **Basic reflection detection**: May miss context-aware XSS or DOM-based XSS
- **No JavaScript execution**: Cannot detect client-side execution of payloads
- **Limited evasion techniques**: Does not include encoding or filter bypass mechanisms

## Future Improvements

- [ ] Add POST request support
- [ ] Implement HTML form parsing and submission
- [ ] Include more sophisticated payload encoding
- [ ] Add multithreading for faster scanning
- [ ] Integrate with headless browsers for DOM XSS detection
- [ ] Create HTML report generation

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [OWASP XSS Filter Evasion Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/XSS_Filter_Evasion_Cheat_Sheet.html)
- [PortSwigger XSS Research](https://portswigger.net/web-security/cross-site-scripting)
- The Python `requests` library team

## Contact

For questions, suggestions, or issues, please:
- Open an issue on GitHub
- Submit a pull request with improvements

---
