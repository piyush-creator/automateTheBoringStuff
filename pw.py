#! python3
# pw.py -An insecure password locker program.

PASSWORDS = {'email': 'piyush@725664',
             'blog': 'Piyush@725664',
             'luggage': '12345'}

import sys,pyperclip
if len(sys.argv) < 2:
    print('Usage: python pw.py[account] - copy account password')
    sys.exit()

account = sys.argv[1]  # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
