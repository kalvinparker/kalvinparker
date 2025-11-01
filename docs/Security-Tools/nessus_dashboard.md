# Create your own Nessus Dashboard

## Generating a Nessus CSV File from a Basic Scan

**Understanding Nessus CSV Files**

Nessus CSV files are a convenient way to export vulnerability scan results into a spreadsheet format. These files can be easily analyzed, filtered, and shared.

**Steps to Generate a Nessus CSV File:**

1. **Launch Nessus:**
   * Open your Nessus application.

2. **Create a New Scan:**
   * If you haven't already, create a new scan.
   * Choose your target systems or networks.
   * Configure scan policies as needed.

3. **Start the Scan:**
   * Begin the scan.

4. **View Scan Results:**
   * Once the scan is complete, review the results in the Nessus interface.

5. **Export as CSV:**
   * Locate the "Export" or "Download" option within the scan results.
   * Choose "CSV" as the export format.
   * Specify a location and filename for the CSV file.
   * Click "Export" or "Download".

**Additional Tips:**

* **Customize Export Options:** Some Nessus versions may allow you to customize the CSV export, such as selecting specific columns or filtering results.
* **Use a CSV Viewer:** For better readability and analysis, consider using a dedicated CSV viewer or spreadsheet software like Microsoft Excel or Google Sheets.
* **Import into Other Tools:** CSV files can be imported into various security tools and databases for further analysis and reporting.

**Example CSV Header:**

| Plugin ID | Plugin Name | Host | Port | Risk | CVSS | Summary |
|---|---|---|---|---|---|---|
| 19506 | SSH Server Banner | 192.168.1.100 | 22 | Low | 3.9 | The SSH server banner is missing a version string. |

**Note:** The specific columns and content in your CSV file may vary depending on the scan policy and Nessus version.

By following these steps, you can effectively generate a Nessus CSV file from your basic scans and leverage its data for further analysis and reporting.

## Combining Multiple CSV Files into One Excel Workbook

### Step-by-Step Guide

1. **Organize CSV Files:**
   * Create a new folder on your computer.
   * Move all the CSV files you want to combine into this folder. **Ensure there are no other files in this folder.**

2. **Open Power Query:**
   * Open your Excel workbook.
   * Go to the **Data** tab.
   * In the **Get & Transform Data** group, click **Get Data** > **From File** > **From Folder**.

3. **Select Folder:**
   * Navigate to the folder containing your CSV files.
   * Select the folder and click **Open**.

4. **Combine Data:**
   * In the **Combine** drop-down menu, choose one of the following options based on your needs:
     * **Combine & Transform Data:** Provides the most flexibility for data manipulation in Power Query Editor.
     * **Combine & Load:** Loads the combined data directly into a new worksheet.
     * **Combine & Load To...:** Allows you to specify where to load the data (existing or new worksheet) and in what format (table, PivotTable, chart, connection).

5. **Transform Data (Optional):**
   * If you chose **Combine & Transform Data**, you can now modify the data in Power Query Editor.
   * Perform tasks like:
     * Changing data types for columns
     * Filtering out unwanted rows
     * Removing duplicates
     * Renaming columns

6. **Load Data:**
   * Once you're satisfied with the data, click **Close & Load** to load the combined data into your Excel workbook.

### Renaming a Table

1. **Select Table:**
   * Click on the table in your Excel workbook.

2. **Access Table Properties:**
   * Go to **Table Tools** > **Design** > **Properties** > **Table Name**.
   * **On a Mac:** Go to the **Table** tab > **Table Name**.

3. **Enter New Name:**
   * Highlight the existing table name.
   * Type in the new name you want to give the table.
   * Press **Enter**.
