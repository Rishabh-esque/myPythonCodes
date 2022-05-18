"""
s = input("Enter a String:\n")

rev = ""

for i in s:
    rev = i+rev

print(rev)
"""


"""
s = input("Enter a String:\n")
rev = ""
len = len(s)
print(len)
for i in range(len):
    rev = s[i]+rev

print(rev)
"""

s = input("Enter a String:\n")
s=list(s)
l = len(s)
for i in range(l//2):
    temp = s[i]
    s[i] = s[l-i-1]
    s[l-i-1] = temp
print(''.join(s))
