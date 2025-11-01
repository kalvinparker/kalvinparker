# start or stop Tenable Nessus

Here's a comprehensive guide incorporating the best practices from the provided information:

**Windows:**

- **Services:**
   - Open the Services app.
   - Locate "Tenable Nessus" in the list.
   - Right-click on it and select "Stop" or "Start" as needed.

- **Command-Line:**
   - Open a command prompt.
   - Run `net start "Tenable Nessus"` to start or `net stop "Tenable Nessus"` to stop the service.

**Linux (RedHat, CentOS, Oracle Linux, SUSE, FreeBSD, Debian, Kali, Ubuntu):**

- **Command-Line:**
   - Open a terminal.
   - Use the appropriate command based on your distribution:
     - `systemctl start nessusd` / `systemctl stop nessusd`
     - `service nessusd start` / `service nessusd stop`

**macOS:**

- **System Preferences:**
   - Open System Preferences.
   - Click on the "Security & Privacy" icon.
   - Click the "Firewall" tab.
   - Click the "Lock" icon to make changes.
   - Locate "Tenable Nessus" in the list.
   - Check or uncheck the box next to it to start or stop the service.

- **Command-Line:**
   - Open a terminal.
   - Run `sudo launchctl start com.tenablesecurity.nessusd` to start or `sudo launchctl stop com.tenablesecurity.nessusd` to stop the service.

**Additional Tips:**

- **Root Permissions:** Ensure you have root or administrator privileges to execute the command-line commands.
- **Firewall Rules:** If your firewall is blocking Nessus, configure it to allow necessary network traffic.
- **Service Status:** Use the appropriate command (e.g., `systemctl status nessusd`) to verify the service's status.
- **Troubleshooting:** If you encounter issues, check the Nessus logs for error messages and consult the documentation for troubleshooting guidance.
