# INET4031 User Management Automation Script

## Program Description

This Python script automates the process of creating multiple user accounts and managing group assignments on Linux systems. Instead of manually executing individual commands for each user, system administrators can use this script to batch process user creation from a simple input file.

Normally, to create a user manually, we would need to run several commands:
- `adduser username` to create the account
- `passwd username` to set the password
- `adduser username groupname` to assign group memberships

This script automates all these steps by reading user data from an input file and executing the same Linux commands programmatically. It handles the entire user provisioning workflow, including account creation, password setting, and group assignments, saving significant time and reducing human error when managing multiple users.

## Program User Operation

This script processes an input file containing user information and automatically executes the necessary Linux commands to create user accounts, set passwords, and assign group memberships. The program reads each line from the input file, validates the format, and then executes the appropriate system commands to provision each user account according to the specifications.

### Input File Format

Each line in the input file must follow this colon-separated format:
username:password:lastname:firstname:group1,group2,group3


**Field Descriptions:**
- **username**: The login name for the user account
- **password**: The initial password for the user account
- **lastname**: The user's last name for the GECOS field
- **firstname**: The user's first name for the GECOS field
- **groups**: Comma-separated list of groups the user should belong to

**Special Cases:**
- To **skip a line** in the input file, start the line with `#` (comment character)
- To **exclude a user from groups**, use `-` in the groups field
- Each line must contain exactly 5 fields separated by colons

**Example Input:**
john_doe:password123:Doe:John:admins,developers
jane_smith:secret456:Smith:Jane:developers
#skip_me:password:Last:First:group1
test_user:testpass:User:Test:-


### Command Execution

To run the script:

1. **Make the script executable:**
   ```bash
   chmod +x create-users.py

2. **Run the script with input redirection:**
   sudo ./create-users.py < create-users.input
4. **Alternative execution method**
   sudo python3 create-users.py < create-users.input
## Requirements

- Must run with `sudo` privileges to create users and modify groups
- Input file must follow the specified format
- Python 3 must be installed on the system

## "Dry Run" Mode

The enhanced version of this script (`create-users2.py`) includes an interactive dry-run feature:

**When prompted**, choose `Y` for dry-run mode or `N` for normal execution

**In dry-run mode:**
- The script displays all commands that WOULD be executed
- No actual changes are made to the system
- Error messages are shown for invalid input lines
- Skip notifications are displayed for commented lines
- Perfect for testing and validation before making actual changes

**In normal mode:**
- Commands are executed to create users and groups
- Minimal output is displayed
- Actual system changes are made

Dry-run mode is recommended for first-time use to verify the input file format and understand what actions the script will perform.
   


