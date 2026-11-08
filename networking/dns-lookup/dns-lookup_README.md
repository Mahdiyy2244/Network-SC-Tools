# 🌐 DNS Lookup Tool

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Networking-0A66C2?style=for-the-badge" alt="Networking" />
  <img src="https://img.shields.io/badge/DNS-Lookup-orange?style=for-the-badge" alt="DNS Lookup" />
</p>

<p align="center">
  A simple Python tool for resolving domain names into IPv4 addresses.
</p>

---

## 📌 About

**DNS Lookup Tool** is a lightweight networking utility developed with Python.

It allows users to enter a domain name and retrieve its corresponding IPv4 address using Python's built-in `socket` library.

This project is part of the **Network & SC Tools** repository.

## ✨ Features

- 🌐 Resolve domain names into IPv4 addresses.
- ⌨️ Accept domain names through user input.
- 🧹 Remove unnecessary spaces from input.
- ⚠️ Handle DNS resolution errors.
- 🐍 Built with Python's standard library.
- 🚀 Simple and beginner-friendly.

## 🛠️ Requirements

- Python 3.x
- Internet connection
- No external libraries required.

## 📂 Project Structure

```text
dns-lookup/
│
├── dns_lookup.py
└── README.md
```

## 🚀 Usage

Clone the main repository:

```bash
git clone https://github.com/Mahdiyy2244/Network-SC-Tools.git
```

Navigate to the DNS Lookup directory:

```bash
cd Network-SC-Tools/networking/dns-lookup
```

Run the script:

```bash
python dns_lookup.py
```

## 💻 Example

**Input:**

```text
===== DNS LOOKUP TOOL =====
Enter a domain name like google.com : google.com
```

**Output:**

```text
Domain: google.com
IP Address: 216.239.x.x
```

*Note: The returned IP address may vary depending on DNS responses and network configuration.*

## ⚙️ How It Works

1. Import the built-in `socket` library.
2. Ask the user to enter a domain name.
3. Remove unnecessary spaces using `strip()`.
4. Resolve the domain using `socket.gethostbyname()`.
5. Display the resulting IPv4 address.
6. Handle resolution errors using `socket.gaierror`.

## 📚 Python Concepts Used

- `socket` module
- `input()`
- `strip()`
- `try / except`
- `f-strings`
- DNS Resolution

## 🔐 Disclaimer

This tool is intended for educational purposes and legitimate network diagnostics.

## 👨‍💻 Part of Network & SC Tools

A collection of networking utilities, cybersecurity tools, Python scripts, and technical resources.

---

<p align="center">
  <b>🌐 Learn Networking. Build Tools. Explore Technology. 🚀</b>
</p>
