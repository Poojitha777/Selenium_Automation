# Magic Method to add

def addNumbers(one,two):
    return one.__add__(two)

print(addNumbers(89,1))