#!/usr/bin/python3

# INET4031 User Management Automation Script
# Enhanced version with dry-run feature

import os
import re
import sys

def main():
    # Prompt user for dry-run mode selection
    dry_run_input = input("Run in dry-run mode? (Y/N): ").strip().upper()
    dry_run = dry_run_input == 'Y'
    
    if dry_run:
        print("=== DRY RUN MODE - No changes will be made to the system ===")

    # Read each line from standard input (the input file)
    for line in sys.stdin:
        # Check if line starts with '#' to identify comments that should be skipped
        match = re.match("^#", line)

        # Split the line into fields using colon as delimiter and remove whitespace
        fields = line.strip().split(':')

        # Skip processing if line is a comment OR doesn't have exactly 5 fields (invalid format)
        if match:
            if dry_run:
                print(f"=== SKIPPING COMMENTED LINE: {line.strip()} ===")
            continue
            
        if len(fields) != 5:
            if dry_run:
                print(f"=== SKIPPING INVALID LINE (wrong field count): {line.strip()} ===")
            continue

        # Extract user data from fields
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3], fields[2])

        # Split groups field into list
        groups = fields[4].split(',')

        # Create user account
        print("==> Creating account for %s..." % (username))
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)

        if dry_run:
            print(f"DRY RUN: Would execute: {cmd}")
        else:
            os.system(cmd)

        # Set user password
        print("==> Setting the password for %s..." % (username))
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)

        if dry_run:
            print(f"DRY RUN: Would execute: {cmd}")
        else:
            os.system(cmd)

        # Process group assignments
        for group in groups:
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username, group))
                cmd = "/usr/sbin/adduser %s %s" % (username, group)
                
                if dry_run:
                    print(f"DRY RUN: Would execute: {cmd}")
                else:
                    os.system(cmd)

if __name__ == '__main__':
    main()
