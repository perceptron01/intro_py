while True:
    stuff = input("String to capitalize [type q to quit]")
    if stuff == "q":
        break
    print(stuff.capitalize())

num_list = (number for number in range(1,6) if number % 2 == 1)

for n in num_list:
    print(n)

list(num_list)