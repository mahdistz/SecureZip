## SecureZip: Create Password-protected Zip Files

SecureZip is a Python program that allows users to create encrypted ZIP archives with password protection from files or folders.

**Features:**

* Supports both individual files and directories.
* Allows you to choose a password or generate a random one.
* Logs the creation of the zip file and password to the console.

**Requirements:**

* Python  >=3.4
* `pyzipper` library

**Setting Up a Virtual Environment:**

It's highly recommended to use a virtual environment to isolate project dependencies and avoid conflicts with other
Python installations on your system. Here's how to set up a virtual environment using `venv` (available in Python 3.3+):

1. Open your terminal or command prompt.
2. Navigate to the directory where you want to create the virtual environment.
3. Run the following command to create a virtual environment named `venv`:

```bash
python -m venv venv
```

4. Activate the virtual environment:

    - **Windows:**
       ```bash
       venv\Scripts\activate
       ```
    - **macOS/Linux:**
       ```bash
       source venv/bin/activate
       ```

**Installing packages:**

Once you have activated the virtual environment, you can install the required dependencies:

1. Ensure you're in the activated virtual environment (check the terminal prompt, which should indicate the virtual
   environment name).
2. Run the following command:

```bash
pip install -r requirements.txt
```

**Usage:**

1. **Run the script:**
    * Navigate to the directory containing the script.
    * Run the script with `python main.py`. Make sure you have activated the virtual environment.

2. **Enter path and password:**
    * The script will prompt you for the file/folder path. Enter the full path to the file or directory you want to zip.
    * You'll then be prompted for a password. Enter your desired password (leave blank for a random one).

3. **Success message:**
    * Upon successful zip creation, the script will display the location of the created zip file and the password.

**Contributing:**
   * Feel free to fork the repository and submit pull requests with improvements or bug fixes.
