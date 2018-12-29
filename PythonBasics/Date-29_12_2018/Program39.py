#WAP for the stop iteration
a = [34,56,78,89,999]
i = iter(a)
print(i)
print(next(i))
print(next(i))
print(next(i))
print(next(i))

try:
    a = [34, 56, 78, 89, 999]
    i = iter(a)
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))
except Exception as q:
    print(type(q))