import itertools as p
input1 =int(input("enter the number of elements"))
List1 = []
for i in range(input1):
    a = int(input("enter digit"))
    List1.append(a)
m = list(p.permutations(List1))
for i in list(m):
    print(i)


