#!/usr/bin/env python3
"""
SSL Certificate Info Tool

This script connects to a given host and port (default 443), retrieves the SSL certificate and prints
information such as the subject common name, issuer common name and validity dates.

Usage:
    python ssl_cert_info.py example.com 443

"""
import sys
import socket
import ssl
from datetime import datetime


def get_certificate(host: str, port: int = 443) -> dict:
    """Retrieve the SSL certificate for a host and port.

    :param host: The hostname to connect to.
    :param port: The port to connect to (default 443).
    :return: A dictionary representing the certificate.
    """
    context = ssl.create_default_context()
    with context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=host) as sock:
        sock.settimeout(10)
        sock.connect((host, port))
        cert = sock.getpeercert()
    return cert


def main():
    if len(sys.argv) < 2:
        print("Usage: python ssl_cert_info.py <host> [port]")
        sys.exit(1)
    host = sys.argv[1]
    port = int(sys.argv[2]) if len(sys.argv) >= 3 else 443
    try:
        cert = get_certificate(host, port)
    except Exception as e:
        print(f"Failed to retrieve certificate from {host}:{port} - {e}")
        sys.exit(1)
    # Extract subject and issuer common names
    subject = dict(x[0] for x in cert.get('subject', []))
    issuer = dict(x[0] for x in cert.get('issuer', []))
    # Parse validity dates
    try:
        not_before = datetime.strptime(cert['notBefore'], "%b %d %H:%M:%S %Y %Z")
        not_after = datetime.strptime(cert['notAfter'], "%b %d %H:%M:%S %Y %Z")
    except Exception:
        not_before = cert.get('notBefore')
        not_after = cert.get('notAfter')
    print(f"Subject CN: {subject.get('commonName')}")
    print(f"Issuer CN: {issuer.get('commonName')}")
    print(f"Valid from: {not_before}")
    print(f"Valid until: {not_after}")


if __name__ == "__main__":
    main()
