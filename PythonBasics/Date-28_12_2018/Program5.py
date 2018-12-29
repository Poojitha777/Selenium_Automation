import itertools

L=[1,2,3,4]
L2=[2,3,4,5]
a= sorted([i for i in itertools.chain(L,L2)])
print(a)


L.extend(L2)
print(sorted(L))

a=L.__add__(L2)
b = sorted(a)
print(b)






