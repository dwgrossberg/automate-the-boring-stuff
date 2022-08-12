import re

phoneRegex = re.compile(r'''
    (\d\d\d-)|
    (\(\d\d\d\))
    \d\d\d
    -
    \d\d\d\d
    \sx\d{2,4}''', re.VERBOSE | re.DOTALL | re.I)

print(phoneRegex.findall())
