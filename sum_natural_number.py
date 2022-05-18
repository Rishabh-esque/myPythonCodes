def sum(n):
    if n <= 0:
        return n
    else: return n+sum(n-1)
    
num = int(input("Enter the number : "))
print("sum = ",sum(num))


