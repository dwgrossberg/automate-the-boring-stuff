#! /usr/bin/env python3
# bulletPointAdder.py- Adds Wikipedia bullet points to the start of each item in a list of text on the clipboard

import pyperclip

text = pyperclip.paste()
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]
text = '\n'.join(lines)
pyperclip.copy(text)
