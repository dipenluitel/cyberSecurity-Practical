#!/usr/bin/python3
import os
import subprocess
import threading
import argparse
import requests
import json

# Function to load the VirusTotal API key from the JSON file
def load_api_key():
    try:
        with open("apiKey.json", "r") as f:
            data = json.load(f)
            return data.get("virustotal_api_key", None)
    except FileNotFoundError:
        print("Error: API key file 'apiKey.txt' not found.")
        return None
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in 'apiKey.txt'.")
        return None

# Load the VirusTotal API key
VIRUSTOTAL_API_KEY = load_api_key()
if VIRUSTOTAL_API_KEY is None:
    print("Error: VirusTotal API key is missing.")
    exit(1)

# Create output folder if it doesn't exist
output_folder = 'output'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Function to run a command for each tool
def run_tool(tool_name, command):
    try:
        print(f"Running {tool_name}...")
        subprocess.run(command, shell=True, check=True)
        print(f"{tool_name} completed.")
    except subprocess.CalledProcessError as e:
        print(f"Error running {tool_name}: {e}")

# Function to check domain reputation using VirusTotal
def check_virustotal(domain):
    url = f"https://www.virustotal.com/vtapi/v2/domain/report"
    params = {
        'apikey': VIRUSTOTAL_API_KEY,
        'domain': domain
    }

    print(f"Checking {domain} reputation on VirusTotal...")
    
    response = requests.get(url, params=params)
    if response.status_code == 200:
        result = response.json()
        output_file = os.path.join(output_folder, f"virustotal_{domain}.json")
        with open(output_file, 'w') as f:
            f.write(response.text)
        print(f"VirusTotal report for {domain} saved to {output_file}")
    else:
        print(f"Failed to retrieve VirusTotal report for {domain}. Status code: {response.status_code}")

# Function to handle domain input
def handle_domains(domains):
    # Define the tools and their respective commands for subdomain enumeration
    tools = {
        "amass": lambda domain: f"amass enum -d {domain} -o {output_folder}/amass_{domain}.out",
        "sublist3r": lambda domain: f"sublist3r -d {domain} -o {output_folder}/sublist3r_{domain}.out",
        "theHarvester": lambda domain: f"theHarvester -d {domain} -b all -f {output_folder}/theHarvester_{domain}.out",
        "assetfinder": lambda domain: f"assetfinder --subs-only {domain} > {output_folder}/assetfinder_{domain}.out",
        "findomain": lambda domain: f"findomain --output --target {domain}",
        "dnsrecon": lambda domain: f"dnsrecon -d {domain} -t brt > {output_folder}/dnsrecon_{domain}.out",
        "dnsenum": lambda domain: f"dnsenum {domain} > {output_folder}/dnsenum_{domain}.out",
        "subfinder": lambda domain: f"subfinder -d {domain} -o {output_folder}/subfinder_{domain}.out",
        "crtsh": lambda domain: f"curl -s https://crt.sh/?q=%25.{domain} | grep {domain} > {output_folder}/crtsh_{domain}.out",
        "massdns": lambda domain: write_massdns_input(domain)
    }

    # Run tools for each domain concurrently using threading
    threads = []

    for domain in domains:
        print(f"Starting enumeration for domain: {domain}")
        # Add VirusTotal check for each domain
        vt_thread = threading.Thread(target=check_virustotal, args=(domain,))
        threads.append(vt_thread)
        vt_thread.start()

        for tool_name, command in tools.items():
            cmd = command(domain)
            thread = threading.Thread(target=run_tool, args=(tool_name, cmd))
            threads.append(thread)
            thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    print("All subdomain enumeration tasks completed.")

# Write domain to a file for MassDNS
def write_massdns_input(domain):
    domain_file = f"{output_folder}/domains_{domain}.txt"
    with open(domain_file, "w") as f:
        f.write(f"{domain}\n")
    return f"massdns -r resolvers.txt -t A -o S {domain_file} > {output_folder}/massdns_{domain}.out"

# Function to parse arguments
def parse_args():
    parser = argparse.ArgumentParser(description="Run subdomain enumeration on one or multiple domains.")
    parser.add_argument('--url', help="Single URL (e.g. https://example.com)")
    parser.add_argument('--urls', help="Comma-separated URLs (e.g. https://example.com,http://test.com)")
    parser.add_argument('--file', help="File containing list of URLs (one per line)")
    return parser.parse_args()

# Main function
def main():
    args = parse_args()
    domains = []

    # Handle --url
    if args.url:
        domains.append(args.url.split("//")[-1].strip("/"))  # Extract domain from URL
    
    # Handle --urls
    if args.urls:
        for url in args.urls.split(","):
            domains.append(url.split("//")[-1].strip("/"))  # Extract domain from URL

    # Handle --file
    if args.file:
        try:
            with open(args.file, 'r') as file:
                for line in file:
                    domains.append(line.strip().split("//")[-1].strip("/"))  # Extract domain from URL
        except FileNotFoundError:
            print(f"Error: File '{args.file}' not found.")
            return

    # Check if any domains were provided
    if not domains:
        print("No domains provided. Please use --url, --urls, or --file to specify domains.")
        return

    # Run subdomain enumeration for the provided domains
    handle_domains(domains)

if __name__ == "__main__":
    main()
