def fun(n):
    if n==0:
        return
    fun(n//2)
    print(n%2,end="")

num = int(input("Enter binary number : "))
fun(num)