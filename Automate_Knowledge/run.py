#!/usr/bin/python3
import os
import subprocess
import threading
import argparse

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

# Function to handle domain input
def handle_domains(domains):
    # Define the tools and their respective commands for subdomain enumeration
    tools = {
        "amass": lambda domain: f"amass enum -d {domain} -o {output_folder}/amass_{domain}.out",
        "sublist3r": lambda domain: f"sublist3r -d {domain} -o {output_folder}/sublist3r_{domain}.out",
        "theHarvester": lambda domain: f"theHarvester -d {domain} -b all -f {output_folder}/theHarvester_{domain}.out",
        "assetfinder": lambda domain: f"assetfinder --subs-only {domain} > {output_folder}/assetfinder_{domain}.out",
        "findomain": lambda domain: f"findomain -t {domain} -o {output_folder}/findomain_{domain}.out",
        "dnsrecon": lambda domain: f"dnsrecon -d {domain} -t brt > {output_folder}/dnsrecon_{domain}.out",
        "dnsenum": lambda domain: f"dnsenum {domain} > {output_folder}/dnsenum_{domain}.out",
        "subfinder": lambda domain: f"subfinder -d {domain} -o {output_folder}/subfinder_{domain}.out",
        "crtsh": lambda domain: f"curl -s https://crt.sh/?q=%25.{domain} | grep {domain} > {output_folder}/crtsh_{domain}.out",
        "massdns": lambda domain: f"massdns -r resolvers.txt -t A -o S {domain} > {output_folder}/massdns_{domain}.out"
    }

    # Run tools for each domain concurrently using threading
    threads = []

    for domain in domains:
        print(f"Starting enumeration for domain: {domain}")
        for tool_name, command in tools.items():
            cmd = command(domain)
            thread = threading.Thread(target=run_tool, args=(tool_name, cmd))
            threads.append(thread)
            thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    print("All subdomain enumeration tasks completed.")

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

