def max_num(l):
    largest = l[0]
    for i in range(0, len(l)):
        if largest < l[i]:
            largest = l[i]
    return largest


def second_largest(largest):
    if len(l) <= 1:
        return None
    large = max_num(l)
    slrg = None
    for i in l:
        if i != large:
            if slrg == None:
                slrg = i
            else:
                slrg = max(slrg, i)
    return slrg


l = [2, 5, 6, 1, 7, 8, 9, 2, 4, 3]
largest = max_num(l)
slrg = second_largest(largest)
print(slrg)


# #####################################################

def getSecMax(l):
    if len(l) <= 1:
        return None
    lar = l[0]
    slar = None

    for x in l[1:]:
        if x > lar:
            slar = lar      
            lar = x        
        elif x != lar:
            if slar == None or slar < x:   
                slar = x                    
    return slar


n=int(input())
l=[]
for i in range(n):
    x=int(input())
    l.append(x)
print(getSecMax(l))
