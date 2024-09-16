<h3>1. <b>Broken Access Control</b></h3>
<p>Access control vulnerabilities arise when users are allowed to access resources or perform actions they shouldn't be able to. This can occur when proper authorization mechanisms aren't implemented or enforced.</p>
<ul>
  <li><b>Examples:</b> 
    <ul>
      <li>Elevation of privilege: A normal user can perform administrative actions.</li>
      <li>Accessing another user's sensitive data by manipulating URLs or parameters.</li>
    </ul>
  </li>
  <li><b>Prevention:</b> Implement strict role-based access controls, regularly test for unauthorized access, and enforce least privilege.</li>
</ul>

<h3>2. <b>Cryptographic Failures</b></h3>
<p>This vulnerability involves weaknesses in how sensitive data (such as passwords, credit card numbers, and health information) is stored or transmitted. Cryptographic failures occur when proper encryption methods aren’t used to protect data at rest or in transit.</p>
<ul>
  <li><b>Examples:</b>
    <ul>
      <li>Data transmitted without encryption (e.g., HTTP instead of HTTPS).</li>
      <li>Use of outdated or weak encryption algorithms.</li>
    </ul>
  </li>
  <li><b>Prevention:</b> Use strong encryption algorithms like AES and TLS, enforce secure connections (HTTPS), and securely store encryption keys.</li>
</ul>

<h3>3. <b>Injection</b></h3>
<p>Injection vulnerabilities, such as SQL injection or NoSQL injection, occur when untrusted data is sent to an interpreter as part of a command or query. Attackers can execute malicious commands, often leading to data breaches or application compromise.</p>
<ul>
  <li><b>Examples:</b> 
    <ul>
      <li>SQL Injection: <code>SELECT * FROM users WHERE username='admin' --</code> bypassing login authentication.</li>
      <li>Command Injection: Injecting system commands via user inputs.</li>
    </ul>
  </li>
  <li><b>Prevention:</b> Use parameterized queries (prepared statements), input validation, and escaping special characters.</li>
</ul>

<h3>4. <b>Insecure Design</b></h3>
<p>Insecure design focuses on the lack of security considerations in the application’s architecture and design. It refers to weak or missing controls that leave systems vulnerable.</p>
<ul>
  <li><b>Examples:</b>
    <ul>
      <li>Not including security measures in the application design phase.</li>
      <li>Inadequate threat modeling or failure to consider potential attack vectors.</li>
    </ul>
  </li>
  <li><b>Prevention:</b> Implement secure development practices like threat modeling, security reviews, and defensive design principles early in the SDLC (Software Development Lifecycle).</li>
</ul>

<h3>5. <b>Security Misconfiguration</b></h3>
<p>Security misconfigurations occur when applications, servers, or databases are not properly configured, leaving vulnerabilities exposed. This is one of the most common issues leading to data breaches.</p>
<ul>
  <li><b>Examples:</b> 
    <ul>
      <li>Leaving default passwords or settings in production systems.</li>
      <li>Exposing unnecessary services or features (e.g., directory listings, verbose error messages).</li>
    </ul>
  </li>
  <li><b>Prevention:</b> Regularly update systems, perform security audits, and implement a hardening process that disables unnecessary features.</li>
</ul>

<h3>6. <b>Vulnerable and Outdated Components</b></h3>
<p>This vulnerability exists when applications use libraries, frameworks, or software that have known vulnerabilities. Attackers can exploit these outdated components to compromise a system.</p>
<ul>
  <li><b>Examples:</b>
    <ul>
      <li>Using an outdated version of a library that has known vulnerabilities.</li>
      <li>Failing to update plugins, dependencies, or frameworks.</li>
    </ul>
  </li>
  <li><b>Prevention:</b> Maintain an updated inventory of all components, regularly apply patches and updates, and use tools to monitor for known vulnerabilities.</li>
</ul>

<h3>7. <b>Identification and Authentication Failures</b></h3>
<p>This occurs when authentication mechanisms are improperly implemented or broken, allowing attackers to compromise user credentials or session data.</p>
<ul>
  <li><b>Examples:</b>
    <ul>
      <li>Poor password policies, such as allowing weak passwords.</li>
      <li>Insecure session management, allowing session hijacking or fixation.</li>
    </ul>
  </li>
  <li><b>Prevention:</b> Implement multi-factor authentication (MFA), secure session management, and enforce strong password policies.</li>
</ul>

<h3>8. <b>Software and Data Integrity Failures</b></h3>
<p>This vulnerability occurs when software updates, critical data, or CI/CD (Continuous Integration/Continuous Deployment) pipelines lack integrity checks, allowing attackers to insert malicious code.</p>
<ul>
  <li><b>Examples:</b> 
    <ul>
      <li>Not verifying digital signatures on software packages.</li>
      <li>Compromising software supply chains to insert malicious code.</li>
    </ul>
  </li>
  <li><b>Prevention:</b> Implement integrity checks, use code-signing techniques, and ensure secure CI/CD pipelines.</li>
</ul>

<h3>9. <b>Security Logging and Monitoring Failures</b></h3>
<p>The lack of proper logging and monitoring allows attackers to exploit vulnerabilities without being detected. Many breaches go unnoticed for extended periods because of poor logging practices.</p>
<ul>
  <li><b>Examples:</b>
    <ul>
      <li>Lack of logging critical security events (e.g., login attempts, privilege escalations).</li>
      <li>Not integrating logs with alerting and monitoring systems.</li>
    </ul>
  </li>
  <li><b>Prevention:</b> Ensure comprehensive logging of security-relevant actions, integrate logs with monitoring systems, and create actionable alerts for suspicious activities.</li>
</ul>

<h3>10. <b>Server-Side Request Forgery (SSRF)</b></h3>
<p>SSRF vulnerabilities allow attackers to manipulate server-side requests, forcing the server to make HTTP requests to unintended locations, such as internal systems or external endpoints.</p>
<ul>
  <li><b>Examples:</b> 
    <ul>
      <li>Accessing internal infrastructure by sending a crafted request to <code>localhost</code> or internal IPs.</li>
      <li>Fetching sensitive data from remote systems using SSRF payloads.</li>
    </ul>
  </li>
  <li><b>Prevention:</b> Validate and sanitize all user inputs, disable unnecessary services (such as internal network exposure), and enforce firewall rules to block unauthorized requests.</li>
</ul>
