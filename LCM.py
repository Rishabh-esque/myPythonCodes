n = int(input("Enter first number : "))
m = int(input("Enter second number : "))
num = max(m,n)

while num<=n*m:
    if num%n == 0 and  num%m == 0:
        break
    num+=1

print("LCM is ",num)

