# In case busy
Now a days i am busy in company project, learning c# for our company so, i want to automate my knowledge<br />
<br />
**Tools**
10-12 tecon tools must be there, if installed leave it if not installed install them <br />
checktool.py<br />
[✅] amass installed<br />
[✅] sublist3r installed<br />
[✅] theHarvester installed<br />
[✅] assetfinder installed<br />
[✅] findomain installed<br />
[✅] dnsrecon installed<br />
[✅] dnsenum not installed<br />
[✅] subfinder installed<br />
[✅] curl installed<br />
[✅] massdns installed<br />
<br />
recon.py<br />
Run all the tools and save output in folder name output/{reconName}.py<br />

<p><b3>How It Works:</b3></p>
    <p><b>Single URL (--url):</b> You can specify a single URL, and the script will extract the domain and run the subdomain enumeration tools on it.</p>
    <p>Example: <br /><code>python3 run.py --url https://example.com</code></p>

    <br />

    <p><b>Multiple URLs (--urls):</b> You can specify multiple URLs, separated by commas, and the script will run the tools on each domain.</p>
    <p>Example: <br /><code>python3 run.py --urls https://example.com,https://test.com</code></p>

    <br />

    <p><b>File Input (--file):</b> You can provide a file containing a list of URLs (one URL per line), and the script will enumerate subdomains for each domain listed in the file.</p>
    <p>Example: <br /><code>python3 run.py --file url_file.txt</code></p>

    <br />

    <p>The script extracts the domain from the URL, runs the tools for each domain, and saves the output in the <b>output</b> folder with a unique file for each tool and domain (e.g., <code>amass_example.com.out</code>, <code>sublist3r_example.com.out</code>).</p>

