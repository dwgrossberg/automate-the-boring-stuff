#! usr/bin/env python3

import re
import pyperclip

# create a regex for phone numbers
phoneRegex = re.compile(r'''
    (
    ((\d\d\d)|(\(\d\d\d\)))?     #area code optional
    (\s|-)                #first seperator
    \d\d\d                #first 3 digits
    -                #seperator
    \d\d\d\d                #last 4 digits
    (((ext(\.)?\s)|x)
    (\d{2,5}))?
    )                #extension optional
    ''', re.VERBOSE)

# todo: create a regex for emails
emailRegex = re.compile(r'''
    [a-zA-Z0-9_.+]+        #name part
    @        #@symbol
    [a-zA-Z0-9_.+]+        #domain name
    ''', re.VERBOSE)

# todo: get text off clipboard
text = pyperclip.paste()

# todo: extract email and phone nums from text
extractedPhone = phoneRegex.findall(text)
extracedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extracedEmail)
pyperclip.copy(results)

print(results)
