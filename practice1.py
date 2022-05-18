# program to create a text file and write time taken by factorial and recursion program

from time import *

def factorial(num):
    fact = 1
    if num==1:
        return fact
    else:
        return num*factorial(num-1)
    
    
f = open("practice1.txt","w")

for i in range(5):
    num = int(input("enter a number that you to find factorial : "))
    start_time_recurrsion = time()
    print(factorial(num))
    end_time_recurrsion = time()
    time_recurrsion = end_time_recurrsion - start_time_recurrsion
    
    
    start_time_normal = time()
    fact=1
    for i in range(1,num+1):
        fact = fact*i
        i = i+1
    print(fact)
    end_time_normal = time()
    time_normal = end_time_normal - start_time_normal
        
        
    f.write(str(num))
    f.write("\t")
    f.write(str(time_recurrsion))
    f.write("\t")
    f.write(str(time_normal))
    f.write("\n")

f.close()

    
