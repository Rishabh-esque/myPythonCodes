a=int(input("enter a number "))
b=a
count=1
for i in range(a,(a*10)+1,a):
    print(b ,"X" , count ,"=",i)
    count=count+1



n=int(input("enter a number : "))
m=n*10
count=1
for i in range (n,m+1,n):
    print("{} * {} =  {}".format(n,count,i))
    count = count + 1