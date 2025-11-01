# CVE-Extraction-Tool
A tool to extract CVE IDs from a webpage, and lists the results as a list. Also generates a report which states, total CVE IDs found, lists duplicates and unique IDs.

1. As a Python script, I want to be able to extract CVE IDs from a report, so that I can import the data into a spreadsheet column and give each CVE ID its own row.

2. As a Python script, I want to be able to identify CVE IDs in a report regardless of case sensitivity, so that I can accurately capture all potential CVE matches.

3. As a Python script, I want to capitalise all CVE IDs, so that they adhere to the correct formatting standard.

4. As a Python script, I want to identify and remove duplicate CVE IDs from a list, so that I can accurately analyse CVE data and avoid redundant information.

5. As a Python script, I want to calculate the number of duplicate CVE IDs found, so that I can assess the data quality and identify potential issues.

6. As a Python script, I want to generate a summary report of unique CVE counts vs duplicates and total them all up, so that I can analyse the CVE data effectively.

## Running the Application:

Save the code as app.py and templates/index.html in the same directory.
Open a terminal in that directory and run python app.py.
Access http://localhost:5000/ in your web browser.
Paste your CVE data into the text area and click "Analyze".
The application will display the analysis report and list of unique CVEs.

1. app.py:

* Imports necessary libraries (Flask, re, Counter).
* Defines the process_cve_data function (unchanged from your script).
* Creates a Flask app instance.
* Defines a route (/) for the homepage.
** If the request method is POST (form submission), it retrieves the pasted text from the form.
** Calls process_cve_data to analyze the text and stores the results.
* Renders the index.html template, passing the retrieved text, report, and unique CVE list.
templates/index.html:

2. Basic HTML structure for the webpage.
* A form with a text area for pasting CVE data.
* Conditional rendering based on the existence of a report:
** Displays the report in a preformatted block.
** Lists unique CVEs in an unordered list.
