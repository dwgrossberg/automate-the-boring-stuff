import re


phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phoneNumRegex.findall("call me at 214-242-4422 tomorrow, or at 342-343-0344 tomorrow"))

 
