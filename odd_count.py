def findOdd(l):
    res = None
    for x in l:
        count = l.count(x)
        if count % 2 != 0:
            res = x
    return res

l = [int(x) for x in input().split(',')]
print(findOdd(l))

###################################################

def findOdd(l):
    res = 0
    for x in l:
        res = res ^ x
    return res

l = [int(x) for x in input().split(',')]
print(findOdd(l))

