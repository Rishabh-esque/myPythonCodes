def max_num(l):
    largest = l[0]
    for i in range(0,len(l)):
        if largest<l[i]:
            largest = l[i]
    return largest


l=[2,5,6,1,7,8,9,2,4,3]
largest=max_num(l)
print(largest)