import argparse
import subprocess
import os
from multiprocessing import Pool

# Define a function to run the selected tool (sublist3r, amass, etc.) for subdomain enumeration
def run_sublist3r(domain):
    print(f"[+] Running Sublist3r on {domain}")
    subprocess.run(['sublist3r', '-d', domain, '-o', f'{domain}_sublist3r.txt'])
    print(f"[-] Sublist3r results saved to {domain}_sublist3r.txt")

def run_amass(domain):
    print(f"[+] Running Amass on {domain}")
    subprocess.run(['amass', 'enum', '-d', domain, '-o', f'{domain}_amass.txt'])
    print(f"[-] Amass results saved to {domain}_amass.txt")

def run_findomain(domain):
    print(f"[+] Running Findomain on {domain}")
    subprocess.run(['findomain', '-t', domain, '-o'])
    print(f"[-] Findomain results saved to {domain}.txt")

# Combine the results into one file
def combine_results(domain):
    print(f"[+] Combining results for {domain}")
    with open(f'{domain}_combined.txt', 'w') as outfile:
        for tool_output in [f'{domain}_sublist3r.txt', f'{domain}_amass.txt', f'{domain}.txt']:
            if os.path.exists(tool_output):
                with open(tool_output) as infile:
                    outfile.write(infile.read())
    print(f"[-] Combined results saved to {domain}_combined.txt")

# Function to process a single domain
def process_domain(domain):
    run_sublist3r(domain)
    run_amass(domain)
    run_findomain(domain)
    combine_results(domain)

# Main function to parse input and manage execution
def main():
    parser = argparse.ArgumentParser(description="Subdomain Enumeration Tool")
    parser.add_argument('--url', type=str, help='Single domain to enumerate')
    parser.add_argument('--urls', type=str, help='Comma-separated list of domains to enumerate')
    parser.add_argument('--file', type=str, help='File containing domains to enumerate')
    
    args = parser.parse_args()

    domains = []

    # Process single domain
    if args.url:
        domains.append(args.url)
    
    # Process multiple domains
    if args.urls:
        domains += [url.strip() for url in args.urls.split(',')]
    
    # Process file input
    if args.file:
        with open(args.file, 'r') as f:
            domains += [line.strip() for line in f]

    if not domains:
        print("Please provide a domain using --url, --urls, or --file.")
        return

    # Use multiprocessing to handle multiple domains concurrently
    with Pool(processes=os.cpu_count()) as pool:
        pool.map(process_domain, domains)

if __name__ == "__main__":
    main()
