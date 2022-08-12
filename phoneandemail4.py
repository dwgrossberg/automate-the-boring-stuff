import re
import pyperclip

phoneRegex = re.compile(r'''
    (
    ((\d\d\d)|(\(\d\d\d\)))?
    (\s|-)
    \d\d\d
    -
    \d\d\d\d
    (((ext(\.)?\s)|x(\.)?)
    (\d{2,5}))?
    )
    ''', re.VERBOSE)

emailRegex = re.compile(r'''
    [a-zA-Z0-9+_.]+
    @
    [a-zA-Z0-9+_.]+
    ''', re.VERBOSE)

text = pyperclip.paste()

extractedPhone = phoneRegex.findall(text)
extracedEmail = emailRegex.findall(text)

allPhoneNum = []
for phoneNum in extractedPhone:
    allPhoneNum.append(phoneNum[0])

results = '\n'.join(allPhoneNum) + '\n' + '\n'.join(extracedEmail)

pyperclip.copy(results)
