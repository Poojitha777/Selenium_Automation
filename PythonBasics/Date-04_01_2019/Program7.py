
class DefultArg():
    def defaultArg(self,z, List1=[]):
        List1.append(z)
        return List1

p=DefultArg()
print(p.defaultArg(12))
print(p.defaultArg(89))
print(p.defaultArg(67))
print(p.defaultArg(78))

