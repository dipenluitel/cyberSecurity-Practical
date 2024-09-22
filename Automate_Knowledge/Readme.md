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
[✅] Gobuster installed<br />
[✅] Knockpy installed<br />
# Information Gathering:

**Single URL (--url):** You can specify a single URL, and the script will extract the domain and run the subdomain enumeration tools on it.  
Example:  
`python3 run.py --url https://example.com`


**Multiple URLs (--urls):** You can specify multiple URLs, separated by commas, and the script will run the tools on each domain.  
Example:  
`python3 run.py --urls https://example.com,https://test.com`


**File Input (--file):** You can provide a file containing a list of URLs (one URL per line), and the script will enumerate subdomains for each domain listed in the file.  
Example:  
`python3 run.py --file url_file.txt`

<br>

The script extracts the domain from the URL, runs the tools for each domain, and saves the output in the **output** folder with a unique file for each tool and domain (e.g., `amass_example.com.out`, `sublist3r_example.com.out`).


<h1>Subdomain Enumeration Script</h1>

<p>This Python script allows subdomain enumeration using tools like Sublist3r, Amass, and Findomain. It supports input for a single domain, multiple domains, or reading domains from a file.</p>

<h2>Explanation:</h2>

<h3>Input Options:</h3>
<ul>
  <li><code>--url</code>: For a single domain.</li>
  <li><code>--urls</code>: For a comma-separated list of domains.</li>
  <li><code>--file</code>: To read domains from a file.</li>
</ul>

<h3>Subdomain Enumeration Tools:</h3>
<ul>
  <li><strong>Sublist3r</strong>, <strong>Amass</strong>, and <strong>Findomain</strong> are called using <code>subprocess.run()</code>.</li>
</ul>

<h3>Output:</h3>
<ul>
  <li>Results from each tool are saved in separate text files: <code>domain_sublist3r.txt</code>, <code>domain_amass.txt</code>, etc.</li>
  <li>A combined result file is created: <code>domain_combined.txt</code>.</li>
</ul>

<h3>Concurrency:</h3>
<ul>
  <li>The script uses Python's <code>multiprocessing.Pool</code> to process multiple domains simultaneously.</li>
</ul>

<h2>Example Usage:</h2>

<pre><code>python run.py --url example.com
python run.py --urls example.com,example.org,test.com
python run.py --file domains.txt
</code></pre>



# XSS (Cross Site Scripting)
**Usages**
$ python xss.py --url https://example.com/search= --file /path/to/payloads.txt

