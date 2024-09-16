<h1><b>XSS Testing Guide</b></h1>
<p>This guide provides step-by-step instructions to manually test for XSS vulnerabilities in web applications. XSS vulnerabilities allow attackers to inject malicious scripts into web pages viewed by other users. Use this guide to test whitelisted or blacklisted elements, character encoding, and potential bypass vectors.</p>
<br />

<h3><b>Prerequisites</b></h3>
<p>Before testing, ensure you have:</p>
<ul>
    <li>Access to the web application you want to test</li>
    <li>Basic knowledge of web technologies such as HTML, JavaScript, and URL encoding</li>
    <li>Appropriate permissions to perform security testing on the target website (legal or authorized engagement)</li>
</ul>
<br />

<h1><b>Basics for Testing XSS Vulnerabilities</b></h1>

<h4><b>1. Identify Whitelisted or Blacklisted Characters</b></h4>
<p>Begin by identifying if the application uses a whitelist or blacklist to filter specific characters. This will give you an idea of what input is allowed or blocked.</p>
<br />

<h4><b>2. Test Basic HTML Characters</b></h4>
<p>Check if basic HTML characters such as < and > are allowed or encoded. These characters are essential for creating HTML elements.</p>
<ul>
    <li><code>&lt;</code></li>
    <li><code>&gt;</code></li>
    <li><code>&amp;lt;</code> <!-- HTML entity for < --></li>
    <li><code>&amp;gt;</code> <!-- HTML entity for > --></li>
</ul>
<p><b>Example Test Payloads:</b></p>
<code>&lt;script&gt;alert(1)&lt;/script&gt;</code><br />
<code>&lt;script&gtalert(1)&lt;/script&gt</code><br />
<br />

<h4><b>3. Test URL-Encoded Characters</b></h4>
<p>Many web applications automatically encode special characters in URLs. Try common URL-encoded representations to see if they are accepted or blocked.</p>
<ul>
    <li><code>%3c</code> <!-- URL encoding for < --></li>
    <li><code>%3e</code> <!-- URL encoding for > --></li>
</ul>
<p><b>Example Test Payloads:</b></p>
<code>%3cscript%3ealert(1)%3c/script%3e</code><br />
<br />

<h4><b>4. Test javascript: URI Scheme</b></h4>
<p>The <code>javascript:</code> URI scheme is commonly used in XSS attacks. Check if this scheme is blacklisted or if the application allows it in href or src attributes.</p>
<ul>
    <li><code>javascript:</code></li>
    <li><code>JAVASCRIPT:</code> <!-- Test for case-insensitivity --></li>
</ul>
<p><b>Example Test Payloads:</b></p>
<code>&lt;a href="javascript:alert(1)"&gt;Click me&lt;/a&gt;</code><br />
<br />

<h4><b>5. Test Octal Encoded Characters</b></h4>
<p>Test octal representations of characters like < and > to see if the application interprets them correctly or allows them through.</p>
<ul>
    <li><code>\74</code> <!-- Octal encoding for < --></li>
    <li><code>\76</code> <!-- Octal encoding for > --></li>
</ul>
<p><b>Example Test Payload:</b></p>
<code>\74script\76alert(1)\74/script\76</code><br />
<br />

<h4><b>6. Test Mixed Encodings</b></h4>
<p>Test mixed encodings to see if the filter can catch them. Attackers often use mixed encoding methods to bypass simple filters.</p>
<ul>
    <li><code>%3cSCRipt%3e</code> <!-- Mixed encoding with capital letters --></li>
</ul>
<p><b>Example Test Payloads:</b></p>
<code>%3cSCRipt%3ealert(1)%3c/SCRipt%3e</code><br />
<br />

<h4><b>7. Test SVG Injection</b></h4>
<p>SVG elements can be a source of XSS, particularly in modern web applications. Test encoded versions of SVG elements to see if they trigger XSS.</p>
<ul>
    <li><code>&lt;%3cSVg%3e&gt;</code> <!-- Encoded SVG elements --></li>
</ul>
<p><b>Example Test Payload:</b></p>
<code>&lt;svg&gt;&lt;script&gt;alert(1)&lt;/script&gt;&lt;/svg&gt;</code><br />
<br />

<h4><b>8. Continue Testing with Various Encodings</b></h4>
<p>Extend your testing by experimenting with various encodings, bypass methods, and payloads that combine different attack vectors.</p>
<br />

<p><b>Other Example Test Payloads:</b></p>
<ul>
    <li><code>data:text/html,&lt;script&gt;alert(1)&lt;/script&gt;</code></li>
    <li><code>&lt;img src=x onerror=alert(1)&gt;</code></li>
    <li><code>&lt;iframe src="javascript:alert(1)"&gt;&lt;/iframe&gt;</code></li>
</ul>
<br />

<h4><b>Notes:</b></h4>
<ul>
    <li>Always perform XSS testing in a safe, controlled environment.</li>
    <li>Never test live systems without proper authorization.</li>
    <li>Some payloads might behave differently based on the browser's built-in security features (e.g., CSP or XSS filters).</li>
</ul>
<p>By following these steps, you can identify potential XSS vulnerabilities and understand how web applications handle whitelisted or blacklisted characters and encodings. Remember to document your findings and share your results responsibly with the application owner.</p>


<h3><b>Steps for Testing XSS Vulnerabilities</b></h3>

<p>Testing for Cross-Site Scripting (XSS) vulnerabilities is a crucial part of web application security assessments. Below are the key steps to follow when testing for XSS in a web application:</p>

<h4><b>Step 1: Identify Input Fields</b></h4>
<p>The first step in testing for XSS vulnerabilities is to identify all areas of the web application that accept user input. This includes:</p>
<ul>
    <li>Form fields (text inputs, search bars, comment sections, etc.)</li>
    <li>URL parameters</li>
    <li>Cookies and headers</li>
    <li>DOM elements that can be manipulated</li>
</ul>

<h4><b>Step 2: Inject Malicious Payloads</b></h4>
<p>Once you've identified input fields, the next step is to inject common XSS payloads into those fields to see if the application properly handles or executes the injected script. Some basic XSS payloads include:</p>
<ul>
    <li><code>&lt;script&gt;alert('XSS')&lt;/script&gt;</code></li>
    <li><code>&lt;img src=x onerror=alert(1)&gt;</code></li>
    <li><code>&lt;svg/onload=alert(1)&gt;</code></li>
    <li><code>"&gt;&lt;svg/onload=alert(1)&gt;</code></li>
</ul>
<p>Inject these payloads in form fields, query strings, and other input points to check if they are executed by the browser.</p>

<h4><b>Step 3: Observe the Output</b></h4>
<p>After injecting the payload, carefully observe the output of the web application. Look for signs that the injected script has been executed, such as a JavaScript alert box popping up, or any manipulation of the HTML or behavior of the page.</p>
<p>If the application is vulnerable to XSS, the browser will execute the malicious script. For example, you may see an alert box generated by the <code>alert(1)</code> function, indicating that the attack was successful.</p>

<h4><b>Step 4: Test Different Contexts</b></h4>
<p>XSS vulnerabilities can occur in various contexts within a web page. Be sure to test different types of inputs and output contexts, such as:</p>
<ul>
    <li>Within HTML content: <code>&lt;p&gt;&lt;script&gt;alert(1)&lt;/script&gt;&lt;/p&gt;</code></li>
    <li>Inside HTML attributes: <code>&lt;input type="text" value="&lt;svg/onload=alert(1)&gt;"&gt;</code></li>
    <li>In URL parameters: <code>example.com?name=&lt;script&gt;alert(1)&lt;/script&gt;</code></li>
    <li>Inside JavaScript code: <code>&lt;script&gt;var x = '&lt;svg/onload=alert(1)&gt;';&lt;/script&gt;</code></li>
</ul>

<h4><b>Step 5: Check Input Validation and Encoding</b></h4>
<p>To confirm whether the application has proper protections against XSS, check whether it validates or sanitizes input. Ensure the following:</p>
<ul>
    <li>Is user input properly escaped or encoded before being reflected in the HTML?</li>
    <li>Are special characters (like <code>&lt;</code>, <code>&gt;</code>, <code>'</code>, and <code>"</code>) encoded to prevent them from being executed as part of a script?</li>
</ul>

<h4><b>Step 6: Try Different Variants of XSS</b></h4>
<p>Depending on the structure of the application, different types of XSS may be exploitable. Be sure to test for:</p>
<ul>
    <li><b>Stored XSS:</b> Inject scripts into locations where the data is stored (e.g., comments, profile descriptions) and check if the payload is executed when other users access the page.</li>
    <li><b>Reflected XSS:</b> Test URL-based inputs where the payload is reflected immediately after submission (e.g., error messages, search results).</li>
    <li><b>DOM-based XSS:</b> Look for XSS vulnerabilities within the Document Object Model (DOM). This type of XSS does not require server interaction but can still be harmful.</li>
</ul>

<h4><b>Step 7: Use Automated Tools</b></h4>
<p>In addition to manual testing, there are several automated tools that can help you detect XSS vulnerabilities. These tools scan your web application for potential vulnerabilities and try various payloads. Some popular tools include:</p>
<ul>
    <li>OWASP ZAP (Zed Attack Proxy)</li>
    <li>Burp Suite</li>
    <li>Acunetix</li>
    <li>Browser Exploit Framework (BeEF)</li>
</ul>

<h4><b>Step 8: Verify Protection Mechanisms</b></h4>
<p>Finally, test the protection mechanisms like Content Security Policy (CSP), input sanitization, and encoding to ensure they are working correctly. CSPs should block inline scripts and unauthorized resources, while sanitization should strip harmful code from inputs.</p>

<h4><b>Conclusion</b></h4>
<p>Testing for XSS vulnerabilities is essential to ensure that your web application is secure. By following these steps, including manual testing, payload injection, checking different input/output contexts, and using automated tools, you can identify and remediate XSS vulnerabilities. Protecting your application against XSS attacks helps safeguard users’ data and maintain the integrity of your web application.</p>

