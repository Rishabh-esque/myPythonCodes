str = input("enter your string : ")
ptn = input("enter pattern : ")

pos = str.find(ptn)
while (pos >= 0):
    print(pos)
    pos = str.find(ptn,pos+1)
