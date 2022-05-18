s = input("Enter a String:\n")

rev = ""

for i in s:
    rev = i+rev

print(rev)

#################################################

s = input("Enter a String:\n")

print(s[::-1])

#################################################

s = input("Enter a String:\n")
rev = ""
len = len(s)
print(len)
for i in range(len):
    rev = s[i]+rev

print(rev)

##################################################

s = input("Enter a String:\n")
l = len(s)
for i in range(l//2):
    temp = s[i]                                  # error
    s[i] = s[l-i-1]
    s[l-i-1] = temp
print(s)


##################################################


s = 'west'
l = [x for x in s]
# l=list(s)
print(l)
for i in range(len(s)-1):
    s[i], s[i+1] = s[i+1], s[i]
print ("".join(l))