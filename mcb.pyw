#! /usr/bin/env python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: ./ mcb.pyw save <keyword> - Saves clipboard to keyword.
#        ./ mcb.pyw <keyword> - Loads keyword to clipboard.
#        ./ mcb.pyw list - Loads all keywords to clipboard.

import shelve
import pyperclip
import sys

mcbShelf = shelve.open('mcb')

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
