#! /usr/bin/env python3

import webbrowser
import sys
import pyperclip

sys.argv  # ['mapit.py', '870', 'Valencia', 'St.']

# check if command line arguments were passed
if len(sys.argv) > 1:
    #['mapit.py', '870', 'Valencia', 'St.']
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()
# https://www.google.co.th/maps/place/<ADDRESS>
webbrowser.open('https://www.google.co.th/maps/place/' + address)
