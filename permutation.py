def factorial(x):
    fact = 1
    for i in range(1, n+1):  # (n,0,-1)  negetive index
        fact *= i
    return fact

n = int(input("Enter the total items : "))
r = int(input("Enter the number of items to be arrange : "))

fact_n=factorial(n)  # calculate n factorial
print(fact_n)

fact_x=factorial(n-r)  # calculate (n-r) factorial

p = fact_n/fact_x
print("P = ", p)
