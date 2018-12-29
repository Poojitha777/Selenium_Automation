#WAP to raise the stop the iteration using raise
class StopIteration(Exception):
    pass

class StopIterProgram():
    UserInput=int(input("Should throw an exception if number is less than 4999"))
    for i in range(0,500):
        if i>UserInput:
            raise StopIteration
        else:
            print(i)

a=StopIterProgram
