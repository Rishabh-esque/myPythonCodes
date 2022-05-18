def sum(*elements):
    res = 0

    for x in elements:
        res = res + x
    return res


print(sum(10, 20))
print(sum(10, 20, 30))
print(sum(10))
print(sum())
