
import socket
print("===== DNS LOOKUP TOOL =====")
domain = input("Enter a domain name like google.com : ").strip()
try:
    ip_address = socket.gethostbyname(domain)

    print(f"\nDomain: {domain}")
    print(f"IP Address: {ip_address}")
except socket.gaierror:
    print("\nError: Could not resolve domain!")
