<!-- Imported from https://github.com/kalvinparker/CET.git
Commit: f71793d
Author: kalvinparker <106995826+kalvinparker@users.noreply.github.com>
License-Name: 
License-Text: 

Imported-on: 2025-11-01T22:21:08.9070186+00:00 -->

<!DOCTYPE html>
<html>
<head>
  <title>CVE Analyzer</title>
</head>
<body>
  <h1>CVE Analyzer</h1>
  <form method="POST">
    <label for="cve_data">Paste your CVE data here:</label>
    <textarea id="cve_data" name="cve_data" rows="10" cols="50">{{ cve_text }}</textarea>
    <br>
    <input type="submit" value="Generate Report">
  </form>
  {% if report %}
    <h2>Report</h2>
    <pre>{{ report }}</pre>
    <h2>Unique CVEs</h2>
    <ul>
      {% for cve in unique_cves %}
        <li>{{ cve }}</li>
      {% endfor %}
    </ul>
  {% endif %}
</body>
</html>

