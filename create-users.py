#!/usr/bin/python3

# INET4031
# Sadaq Abdullahi
# Data Created
# 2025-10-25

# Import necessary modules for system operations, regular expressions, and input handling
import os
import re
import sys

def main():
    # Read each line from standard input (the input file)
    for line in sys.stdin:

        # Check if line starts with '#' to identify comments that should be skipped
        match = re.match("^#", line)

        # Split the line into fields using colon as delimiter and remove whitespace
        fields = line.strip().split(':')

        # Skip processing if line is a comment OR doesn't have exactly 5 fields (invalid format)
        # This prevents errors from malformed input lines
        if match or len(fields) != 5:
            continue

        # Extract user data from fields and format for Linux passwd file GECOS field
        # GECOS field typically contains: Full Name,Room Number,Work Phone,Home Phone,Other
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3], fields[2])  # Format: "Firstname Lastname,,,"

        # Split groups field into list using comma as delimiter for multiple group assignments
        groups = fields[4].split(',')

        # Display progress message for user creation
        print("==> Creating account for %s..." % (username))
        # Build command to create user account with disabled password and GECOS info
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)

        # DRY RUN: Print command instead of executing during testing
        # ACTUAL RUN: Uncomment os.system(cmd) to execute the command
        print(cmd)
        # os.system(cmd)

        # Display progress message for password setting
        print("==> Setting the password for %s..." % (username))
        # Build command to set user password using echo and passwd commands
        # The -ne options prevent newline and enable escape characters
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)

        # DRY RUN: Print command instead of executing during testing
        # ACTUAL RUN: Uncomment os.system(cmd) to execute the command
        print(cmd)
        # os.system(cmd)

        # Process group assignments for the user
        for group in groups:
            # Skip if group is '-' (indicates no group assignment needed)
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username, group))
                # Build command to add user to specified group
                cmd = "/usr/sbin/adduser %s %s" % (username, group)
                # print cmd
                # os.system(cmd)

if __name__ == '__main__':
    main()
