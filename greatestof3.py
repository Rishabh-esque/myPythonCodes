a = int(input("Enter First Number:\n"))
b = int(input("Enter Second Number:\n"))
c = int(input("Enter Third Number:\n"))

if a >= b and a >= c:
    print("Largest number is:", a)  # a is greater than b and c

if b >= a and b >= c:
    print("Largest number is:", b)  # b is greater than a and c

if c >= a and c >= b:
    print("Largest  number is:", c)  # c is greater than a and b
