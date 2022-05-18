y = int(input("Enter Year : "))

if (y % 4 == 0) and (y % 100 != 0):
    print("Yes")                    # year is multiple of 4 and not divisible by 100

elif y % 400 == 0:
    print("yes")                    # year is multiple of 400

else:
    print("No")
