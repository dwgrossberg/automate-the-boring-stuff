
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 23, 45, 345, 3453, 67784]

number = int(input("Give me a goddam number bruh: "))

new_list = []

for i in a:
    if i < number:
        new_list.append(i)

for d in new_list:
    print(*str(d))

