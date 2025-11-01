# 1. As a Python script, I want to be able to extract CVE IDs from a report, so that I can import the data into a spreadsheet column and give each CVE ID its own row.
# 2. As a Python script, I want to be able to identify CVE IDs in a report regardless of case sensitivity, so that I can accurately capture all potential CVE matches.
# 3. As a Python script, I want to capitalise all CVE IDs, so that they adhere to the correct formatting standard.
# 4. As a Python script, I want to identify and remove duplicate CVE IDs from a list, so that I can accurately analyse CVE data and avoid redundant information.
# 5. As a Python script, I want to calculate the number of duplicate CVE IDs found, so that I can assess the data quality and identify potential issues.
# 6. As a Python script, I want to generate a summary report of unique CVE counts vs duplicates and total them all up, so that I can analyse the CVE data effectively.

import re
from collections import Counter

def process_cve_data(text):
  """Processes CVE data from text, removes duplicates, and generates a summary report.

  Args:
    text: The input text containing CVE IDs.

  Returns:
    A tuple containing a list of unique CVE IDs and a summary report.
  """

  # 1. Regular expression pattern, should find CVE-XXXX-XXXX (4) and CVE-XXXX-XXXXX (5)  
  cve_pattern = r"CVE-\d+-\d+"

  # 2. Find all matches no matter the Case-sensitive pattern; just incase of typos  
  cve_list = re.findall(cve_pattern, text, re.IGNORECASE)

  # 3. Capitalise lowercase CVE IDs  
  capitalized_cve_list = [cve.upper() for cve in cve_list]

  # 4. Remove duplicates using set and convert back to list
  unique_cves = list(set(capitalized_cve_list))

  # 5. Calculate duplicate counts
  cve_counts = Counter(capitalized_cve_list)
  duplicate_cves = [cve for cve, count in cve_counts.items() if count > 1]

  # 6. Generate summary report
  summary_report = f"Total CVEs: {len(capitalized_cve_list)}\n"
  summary_report += f"Unique CVEs: {len(unique_cves)}\n"
  summary_report += f"Duplicate CVEs: {len(duplicate_cves)}\n"
  summary_report += "\nDuplicate CVE IDs:\n"
  summary_report += "\n".join(duplicate_cves)

  return unique_cves, summary_report

# Copy/paste below the word 'text =' but between """ and """:
text = """

"""

unique_cves, report = process_cve_data(text)

print(report)
print("\nUnique CVEs:")
for cve in unique_cves:
  print(cve)
