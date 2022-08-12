Python 3.6.1 (v3.6.1:69c0db5050, Mar 21 2017, 01:21:04) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> # This program says hello and asks for my name

print('hello world')
print('what is your name?')  # ask for their name
myName = input()
print('it is good to meet you,' + myName)
print('the length of your name is:')
print(len(myName))
print('what is your age')  # ask for their age
myAge = input()
print('you will be ' + str(int(myAge) + 1) + ' in a year')
