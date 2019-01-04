import itertools as it

List1 = [7889,200,100,599,10]
List2 = []
for n in range(1, len(List1) + 1):
    for i in it.combinations(List1, n):
        if sum(i) == 100:
            List2.append(i)

print(List2)


