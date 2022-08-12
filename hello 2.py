# This program says hello and asks for my name

print('Hello world!')

print('What is your name')  # ask for their name
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))
print()

print('What is your age?')  # ask for their age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')
print()

print('How big is your dick?')  # ask for dick size
myDick = input()
print('Your dick will be ' + str(int(myDick) + 3) + ' inches in a month')
print('And we at BigDicks think thats pretty damn cool')

for num in [1, 2, 3, 4]:
    print(num)
