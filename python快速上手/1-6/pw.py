#! python3 /user/bin/env python3
# pw.py - An insecure password locker program.
PASSWORD = {
    'email': '17628048484@163.com',
    'blog': 'VjjjjKDSKdjdsk',
    'luggage': '123456'
}

import sys, pyperclip

if len(sys.argv) < 2:
    print("Usage: python3 pw.py [account] - copy account password")
    sys.exit()
account = sys.argv[1] # first command line arg is the account name

if account in PASSWORD:
    pyperclip.copy(PASSWORD[account])
    print("password for "+account+" copied to clipboard.")
else:
    print("there is no account named "+account)