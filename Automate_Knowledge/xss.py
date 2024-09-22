import requests
import argparse

def send_request(url, payload):
    response = requests.get(url + payload)
    # Analyze the response here (e.g., check for specific HTML patterns)
    if "expected_pattern" in response.text:
        print(f"Payload {payload} is working!")

def main():
    parser = argparse.ArgumentParser(description='XSS Brute Force Tool')
    parser.add_argument('--url', help='URL to test (e.g. https://example.com/search=)', required=True)
    parser.add_argument('--file', help='File containing payloads (one per line)', required=True)
    args = parser.parse_args()

    url = args.url
    payload_file = args.file

    try:
        with open(payload_file, 'r') as f:
            payloads = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        print(f"Error: File '{payload_file}' not found.")
        return

    for payload in payloads:
        send_request(url, payload)

if __name__ == '__main__':
    main()
