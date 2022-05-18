n = int(input("Enter first number : "))
m = int(input("Enter second number : "))
num = min(m,n)

for x in range(1,num+1):
    if n%x == 0 and  m%x == 0:
        gcd = x

print(gcd)


