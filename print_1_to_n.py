def print_n(n):
    if n<=0:
        return
    else:
        print_n(n-1)
        print(n)

num = int(input("Enter the number : "))
print_n(num)
