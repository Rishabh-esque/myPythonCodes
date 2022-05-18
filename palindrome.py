# str = input("enter text : ")
# str2=str[::-1]
# if str==str2:
#     print("yes")
# else:
#     print("No")

##########################################

str = input("enter text : ")
i=0
j=len(str)-1
while i<=j:
    if str[i]!=str[j]:
        print("NO")
        break
    i=i+1
    j=j-1
else:
    print("palindrime")