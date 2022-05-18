# Bank system 

f = open("append_mode.txt","a+")
f.write("\n")
num = int(input("How many customers do u want to add : "))
for i in range(num):
    name = input("Enter customer name : ")
    balance = input("Enter customer balance : ")
    f.write(name)
    f.write("\t\t\t")
    f.write(balance)
    f.write("\n")
    print(f.read())
f.close()



from turtle import *
color("red")
begin_fill() 
pensize(3)
left(50)
forward(133)
circle(50,200)
right(140)
circle(50,200)
forward(133)
end_fill()