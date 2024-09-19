# cyberSecurity
# Cyber Security

This repository contains several tools and writeups focused on **information gathering**, **reconnaissance**, and **security testing**. The structure is divided into automated tools, individual security writeups, and various utility tools for domain scanning, port scanning, and more.

## Automated Tool

The **Automated Tool** folder is where a tool for information gathering and recon is being developed. This tool aims to automate the process of security reconnaissance by gathering data about domains, subdomains, and other crucial information needed for security testing.

<ul>
  <li>Subdomain Enumeration</li>
  <li>Port Scanning</li>
  <li>Header Analysis</li>
</ul>

## Writeups

The **Writeups** folder contains research and analysis on various security topics. It currently includes a detailed topic on **Cross-Site Scripting (XSS)**, which explores different types of XSS vulnerabilities, exploitation techniques, and prevention strategies.

<ul>
  <li>Topics on XSS</li>
</ul>

## Tools

The **Tools** folder contains several scripts and utilities developed for scanning, enumeration, and security testing:

### Host Scanner

The **Host Scanner** folder contains tools for scanning domains and gathering subdomains. It is primarily focused on enumerating subdomains for security testing purposes.

<ul>
  <li>Domain Scanning</li>
  <li>Subdomain Enumeration</li>
</ul>

### Multi Scan X

The **Multi Scan X** folder includes utilities for scanning HTTP headers and open ports on target systems. This tool helps gather critical data related to web server configuration and network-level information.

<ul>
  <li>HTTP Header Scanning</li>
  <li>Port Scanning</li>
</ul>

### Open Redirect Tester

The **Open Redirect Tester** folder contains scripts designed to identify open redirect vulnerabilities in websites. This vulnerability can be exploited to redirect users to malicious websites.

<ul>
  <li>Open Redirect Testing</li>
</ul>

### Lazy Recon

The **Lazy Recon** folder automates the following tasks:

<ul>
  <li>**Subdomain Enumeration**</li>
  <li>**Certificate Checker** - Checks SSL/TLS certificates for a domain.</li>
  <li>**Github Dorking** - Uses GitHub search queries to find sensitive information.</li>
  <li>**Google Dorking** - Leverages Google search queries to find hidden or sensitive data on websites.</li>
</ul>

### WordPress

The **WordPress** folder includes tools to scan WordPress websites and detect security issues such as vulnerabilities in plugins, themes, and the `xmlrpc.php` file.

<ul>
  <li>WordPress Site Scanning</li>
  <li>XML-RPC Vulnerability Testing</li>
</ul>
