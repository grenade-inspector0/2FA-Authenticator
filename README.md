# What is this?
This is a 2FA Authenticator used to add additional security to your online accounts.

# Quick Setup*
1. Install the latest version of [Python](https://python.org)
    - Make sure to enable the "Add Python to PATH" setting when installing Python.
2. Download the [latest release](https://github.com/grenade-inspector0/2FA-Authenticator/archive/refs/heads/main.zip), the unzip the zip archive.
3. Now, open a CMD Prompt window in the same directory as the unzipped folder, which contains all the project files.
4. Run "pip install -r requirements.txt" 
5. Run "python main.py"
##### *Not quick if you don't already have Python already installed.

# FAQ
- **Is this secure?**
    - Short answer, no.
- **If this isn't secure, then why should I use it?**
    - I would only use this with accounts that are temporary, or accounts that you don't care about.
- **How do I use it?**
    1. Follow the instructions outlined in the "Quick Setup" section
    2. Select the option to add an identifier, your identitifer can be anything, but I usually make it the email / username for the account that I'm using it for.
    3. Next, enter the 2FA Key, if you only see a QR Code, and not a 2FA Key, then you might have to click a button that says "Manual Setup" or something along those lines.
    4. Once you enter a valid 2FA Key, you should be back at the main menu, select the "Get 2FA Code" option, and it should display your set identifier and the current 2FA code**.
    5. To be remove the identifier you can either manually open the .json file, or from the main menu you can select the option to remove it using its identifier. 
#### **The 2FA Code updates every 30 seconds, but my script doesn't update when the 2FA Code changes, so you'll have to use the option to regenerate the code(s) if it doesn't work. 
