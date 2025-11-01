#### Workaround
```
https://support.microsoft.com/en-gb/topic/-we-couldn-t-update-system-reserved-partition-error-installing-windows-10-46865f3f-37bb-4c51-c69f-07271b6672ac
```
#### Permanant solution
```
https://www.winhelponline.com/blog/resize-efi-system-partition/
```
### Note: I did this to update my Windows 10 installation to meet requirements before upgrading to Windows 11. Then again to update to Windows 11, version 24H2.

# Works with Windows 10 & 11 with GPT partitition:

**Troubleshooting Guide: Resolving "We couldn't update system reserved partition" Error**

**Problem:** You are encountering the error "We couldn't update system reserved partition" during a Windows 10 or Windows 11 update, preventing the update from completing. This is often due to insufficient space on the EFI System Partition (ESP).

**Solution:** This guide will walk you through freeing up space by deleting font files within the ESP.

**Prerequisites:**

* You are logged in with an administrator account.
* Your system uses a GPT partition scheme (common for modern systems).

**Steps:**

1.  **Open Command Prompt as Administrator:**
    * Search for "cmd" in the Windows search bar.
    * Right-click on "Command Prompt" in the search results.
    * Select "Run as administrator."
    * Click "Yes" if prompted by User Account Control (UAC).

2.  **Mount the EFI System Partition (ESP):**
    * In the Command Prompt window, type the following command and press Enter:
        ```
        mountvol y: /s
        ```
        * This command assigns the drive letter "Y:" to the ESP, allowing you to access it. Note that any other drive letter can be used if Y: is already in use.

3.  **Navigate to the Fonts Folder:**
    * Switch to the Y: drive by typing the following command and pressing Enter:
        ```
        Y:
        ```
    * Navigate to the Fonts directory within the EFI folder by typing the following command and pressing Enter:
        ```
        cd EFI\Microsoft\Boot\Fonts
        ```

4.  **Delete Font Files:**
    * Delete all files within the Fonts folder by typing the following command and pressing Enter:
        ```
        del *.*
        ```

5.  **Confirm Deletion (if prompted):**
    * If the system asks for confirmation before deleting the files, type "Y" and press Enter.

6.  **Unmount the EFI System Partition (Optional but recommended):**
    * To remove the drive letter from the EFI system partition, and return the system to normal, type the following command and press enter.
        ```
        mountvol y: /d
        ```

7.  **Retry Windows Update:**
    * Close the Command Prompt window.
    * Go to Windows Update (Settings > Update & Security > Windows Update or Settings > Windows Update).
    * Click "Check for updates" and attempt to install the update again.

**Important Notes:**

* **Caution:** Be extremely careful when working with the EFI System Partition. Incorrect modifications can prevent your system from booting.
* **Alternative Drive Letters:** If "Y:" is already in use, choose a different unused drive letter.
* **GPT Partition:** This solution is specifically for systems with GPT partitions. If your system uses MBR, the steps may differ.
* **Backups:** Consider backing up important data before making any changes to system partitions.
* **About the Fonts Folder:**
    * The `EFI\Microsoft\Boot\Fonts` folder contains fonts used during the early stages of the Windows boot process, primarily for displaying text before Windows fully loads.
    * While these fonts contribute to the visual presentation of the boot environment, they are *not* essential for Windows to function once it has booted.
    * It is generally safe to delete the contents of this folder to free up space, especially when encountering the "We couldn't update system reserved partition" error due to a full EFI partition. Windows will use default system fonts if needed.
* **EFI Partition Full Issue:** The primary reason for performing these steps is to alleviate a full EFI system partition. This is a common cause of Windows update failures.

By adding the explanation about the fonts folder, users will have a better understanding of why this solution is both effective and safe.
