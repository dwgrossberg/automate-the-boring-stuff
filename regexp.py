def isPhoneNumber(text):
    if len(text) != 12:
        return False #not a phone number
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False #no area code
    if text[3] != "-":
        return False #missing dash
    for i in range (4, 7):
        if not text[i].isdecimal():
            return False #no first 3 digits
    if text[7] != "-":
        return False #missing seoncd dash
    for i in range (8, 12):
        if not text[i].isdecimal():
            return False #missing last 4 digits
    return True

print(isPhoneNumber("425-555-1245"))
print(isPhoneNumber("hello"))

message = "call me at 214-242-4422 tomorrow, or at 342-343-0344 tomorrow"
foundNumber = False
for i in range(len(message)):
    chunk = message[i: i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
        foundNumber = True
if not foundNumber:
    print("Could not find any phone numbers")
