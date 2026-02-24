---

# Simple Reflected XSS Scanner (Python)

A lightweight Python-based tool that detects **Reflected Cross-Site Scripting (XSS)** vulnerabilities by injecting test payloads into URL query parameters and checking if they are reflected in the HTTP response.

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Requests](https://img.shields.io/badge/requests-2.25%2B-orange)](https://docs.python-requests.org/)

> ⚠️ For educational and authorized security testing purposes only.

---

## Features

* Parses URL query parameters
* Injects multiple common XSS payloads
* Sends automated HTTP GET requests
* Detects reflected input in server responses
* Generates a structured vulnerability report
* Includes permission confirmation before scanning

---

## Technologies Used

* Python 3
* `requests` library
* `urllib.parse`

---

## Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/xss-scanner.git
cd xss-scanner
```

### 2️⃣ Install Dependencies

```bash
pip install requests
```

---

## Usage

Run the script:

```bash
python xss_scanner.py
```

You will be prompted to:

1. Enter a full URL including query parameters
   Example:

   ```
   http://localhost/test.php?name=test
   ```

2. Confirm you have permission to test the target

---

## Example Test Environment

This scanner can be tested safely using:

* **Damn Vulnerable Web Application**
* A local XAMPP server
* A simple vulnerable PHP file:

```php
<?php
echo $_GET['name'];
?>
```

Access via:

```
http://localhost/test.php?name=test
```

---

## Sample Output

If a vulnerability is found:

```
[!] POTENTIAL XSS FOUND on parameter: name
Payload: <script>alert('XSS')</script>
```

A report file will be generated:

```
xss_report.txt
```

---

## Report Format

```
Reflected XSS Vulnerability Report
========================================
URL: http://localhost/test.php
Vulnerable Parameter: name
Proof-of-Concept Payload: <script>alert('XSS')</script>
--------------------
```

---

## How It Works

1. Parses the provided URL
2. Extracts query parameters
3. Injects predefined XSS payloads
4. Reconstructs the URL with payloads
5. Sends HTTP requests
6. Checks if payload appears in response
7. Logs potential vulnerabilities

---

## Limitations

* Detects only **Reflected XSS**
* Does not detect DOM-based XSS
* No HTML context analysis
* May produce false positives
* Does not test POST requests

---

## Legal Disclaimer

This tool is intended for:

* Learning purposes
* Local lab environments
* Authorized penetration testing

Do NOT use this tool against websites without explicit written permission.

Unauthorized testing is illegal and unethical.

---

## Future Improvements

* Context-aware detection
* HTML parsing
* Support for POST requests
* Encoded payload detection
* Multi-threaded scanning

---

## Author

Sarah Binte Tariq -
Cybersecurity & Python Enthusiast

---
