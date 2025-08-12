# SSL Certificate Info

A Python utility to fetch and display SSL/TLS certificate details for a given host and port. It connects directly to the server and prints the certificate's subject, issuer, and validity period.

## Features

- Connects to a target host and port to retrieve the SSL certificate.
- Displays the certificate's subject common name (CN) and issuer CN.
- Shows the validity dates (`notBefore` and `notAfter`).
- Uses only Python standard library modules (`ssl`, `socket`, `datetime`).

## Usage

Run the script with Python 3 and specify the host (and optional port):

```bash
python ssl_cert_info.py example.com
python ssl_cert_info.py example.com 8443
```

By default, the script uses port `443`. The output will show the subject, issuer, and validity dates of the certificate. Note that some servers may require SNI (Server Name Indication); the script sets the `server_hostname` parameter accordingly.

## Disclaimer

This script is intended for educational and informational purposes. It does not perform certificate validation beyond retrieving and displaying the certificate details. For production systems, use robust SSL/TLS libraries and follow best practices for certificate validation.
