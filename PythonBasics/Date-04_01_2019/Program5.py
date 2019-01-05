

def defaultArg(z, List1=None):
    if List1 is None:
        List1= []
    List1.append(z)
    return List1


print(defaultArg('poo'))
print(defaultArg('pooj'))
print(defaultArg('pooji'))
print(defaultArg('poojitha'))


