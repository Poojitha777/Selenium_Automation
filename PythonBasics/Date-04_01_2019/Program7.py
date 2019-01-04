# def func(a, l=[]):
#     l.append(a)
#     return l
#
#
# print(func(1))
# print(func(2))
# print(func(3))
# print(func('a'))
# print(func('b'))
#
#
#
# def func(l=[]):
#     print(l)
#
# func()
class DefultArg():
    def defaultArg(self,z, List1=[]):
        List1.append(z)
        return List1

p=DefultArg()
print(p.defaultArg(12))
print(p.defaultArg(89))
print(p.defaultArg(67))
print(p.defaultArg(78))

