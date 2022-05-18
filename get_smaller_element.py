l = [2,4,6,8,10,12,14,16,18,20]
ans = []
num=int(input())
for i in l:
    if (i<num):
        ans.append(i)
print(ans)

#########################################

l = [2,4,6,8,10,12,14,16,18,20]
num=int(input())
ans=[x for x in (l) if x<num]
print(ans)