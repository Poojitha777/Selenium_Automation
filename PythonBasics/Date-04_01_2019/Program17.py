from functools import partial

def multiplyMethod(one, two):
    return one * two

List1 = []
for i in range (1, 20):
    function = partial(multiplyMethod, i)
    List1.append(function)

print(List1[0](5))
print(List1[1](8))