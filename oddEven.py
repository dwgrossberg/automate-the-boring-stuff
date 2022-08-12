
number = int(input("May I have a number please? "))
oddEven = number / 2 
if oddEven != int(oddEven):
    print("Your number is odd!")
else:
    print("Your number is even!")
mod = number % 2
if mod > 0:
    print("Your number is odd!")
else:
    print("Your number is even!")
four = number % 4
if four == 0:
    print("And it's divisible by 4!")
    
