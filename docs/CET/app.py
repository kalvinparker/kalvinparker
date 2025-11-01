from flask import Flask, render_template, request
from collections import Counter
import re

app = Flask(__name__)

def process_cve_data(text):
  """Processes CVE data from text, removes duplicates, and generates a summary report.

  Args:
    text: The input text containing CVE IDs.

  Returns:
    A tuple containing a list of unique CVE IDs and a summary report.
  """

  # Same logic as your existing process_cve_data function...

  return unique_cves, report

@app.route("/", methods=["GET", "POST"])
def cve_analyzer():
  cve_text = ""
  report = ""
  unique_cves = []
  if request.method == "POST":
    cve_text = request.form["cve_data"]
    unique_cves, report = process_cve_data(cve_text)
  return render_template("index.html", cve_text=cve_text, report=report, unique_cves=unique_cves)

if __name__ == "__main__":
  app.run(debug=True)
