def fun():
    a = 10
    b = 20
    print(a, b, c, d) # c and d from outside of function, Global variable

c = 30
d = 40
fun()
print(c, d)
