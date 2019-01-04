from functools import partial

def multiplyMethod(one,two):
    return one*two

print(multiplyMethod(4,10))

multi=partial(multiplyMethod,two=9)
print(multi(8))