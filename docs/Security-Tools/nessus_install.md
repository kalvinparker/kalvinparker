# Installing and setting up Nessus Vulnerability Scanner with Kali Linux (or any other Linux distribution)

**Prerequisites:**

- **Internet connection:** Nessus requires an internet connection during installation and activation.

**Steps:**

1. **Download Nessus:**

   - Visit the Tenable Nessus downloads page: [https://www.tenable.com/downloads/nessus?loginAttempted=true](https://www.tenable.com/downloads/nessus?loginAttempted=true)
   - Locate the **Linux - Debian - amd64** version (assuming you're using a 64-bit Kali system).
   - Download the `.deb` file.
   - Agree to the License Agreement.
   - Click Checksum next to the download button and copy the SHA256 checksum into `text editor`.

2. **Verify Download Integrity (Optional but Recommended):**

   - Open a terminal window.
   - Navigate to your Downloads directory:
   - 
     ```Bash
     cd ~/Downloads
     ```
     
   - Read the directory with the following command to show the `downloaded_file_name`:
   - 
     ```Bash
     ls
     ```
     
   - Prepare the `SHA256_checksum` and `downloaded_file_name` with `text editor`. This ensures the downloaded file is not corrupted. Use the following command:
   - 
     ```bash
     echo "sha256sum_checksum downloaded_file_name" > sha256sum_nessus
     ```
     
     Replace `[downloaded_file_name]` with the actual filename (e.g., `Nessus-10.6.3-debian10_amd64.deb`). The output should match the checksum provided on the Tenable website.
   - Run the following command:
   - 
     ```bash
     sha256sum -c sha256sum_nessus
     ```
     
     The following message should be returned: `[download_file_name]: OK`

5. **Install Nessus:**

   - Run the following command in the terminal:

     ```bash
     sudo apt install ./[downloaded_file_name]
     ```

     Replace `[downloaded_file_name]` with the actual filename.

   - Enter your password when prompted. This command will download and install Nessus using the package manager.

6. **Start Nessus Service:**

   - Run the following command in the terminal:

     ```bash
     sudo systemctl start nessusd
     ```

7. **Activate Nessus:**

   - Open a web browser and navigate to:

     ```bash
     https://localhost:8834
     ```
     
   - You might encounter a security warning about the SSL certificate. Click "Advanced" and then "Accept the Risk and Continue" if you trust the connection.
   - Select `Register Offline` and click continue.
   - Select `Nessus Expert` and click continue.
   - Copy the `challenge code` and select `Offline Registration`.
   - Generate a license by pasting `challenge code` and `activation code` in the correct boxes and clicking submit.
     To obtain an `activation code*` click the link for a free Nessus Essentials license for personal use from Tenable's website ([https://www.tenable.com/tenable-for-education/nessus-essentials](https://www.tenable.com/tenable-for-education/nessus-essentials)).
   - Bookmark the plugin link so you can obtain the newest Nessus plugins (for offline use); and then
   - Copy/paste `Tenable license` into `Nessus License Key` on the Nessus / Setup page and click continue.
   - Create a `user account` and click submit.
   - Activation and Registration complete.
  
8. **Update components and download plugins - online**

   - Go to settings.
   - Select Software Update.
   - Select `Update all components`, change `Update Frequency` to your own or organisation's preference, and click save.
   - Click `Manual Software Update` and select `Update all components` and click Continue.
   - Keep calm and go make a brew or do something else. This can take a while...
  
9. **Update components and download plugins - offline**

   - Refer to the section: `Active Nessus`, and the page you bookmarked the plugin link.
   - If not done so already, use the `plugin` link to download the latest plugins. (linked to your license)
   - Place the downloaded `plugins` in a location the `Update Server` can find it.
   - Go to settings.
   - Select Software Update.
   - Select `Update all components`, and change `Update Frequency` to your own or organisation's preference.
   - Enter the server location of your `downloaded plugins` in the `Update Server` field and click save.
   - Click `Manual Software Update` and select `Update all components` and click Continue.
   - Keep calm and go make a brew or do something else. This can take a while...

**Additional Notes:**

- If you encounter firewall issues, you may need to adjust your firewall rules to allow Nessus to function properly.
- For further configuration options and advanced usage, refer to the Nessus documentation: [https://docs.tenable.com/](https://docs.tenable.com/)
- Nessus updates are typically available through the Kali package manager. You can update Nessus with `sudo apt update && sudo apt upgrade`. Make sure to stop the Nessus service first 

**Congratulations! You've successfully installed and activated Nessus on your Kali Linux system.** You can now use Nessus to perform vulnerability scans on target systems. Refer to the Nessus documentation for instructions on launching scans and interpreting results.
