from functools import partial

def findPowerMethod(a,b):
    return a**b

print(findPowerMethod(3,3))

cubenum=partial(findPowerMethod,b=4)
print(cubenum(4))

square=partial(findPowerMethod,b=3)
print(square(8))