#WAP to raise an exception if the given input is below zero
class NumberZeroDivision(Exception):
    pass
class UserException():
    UserInput=int(input("Please enter a number"))
    if UserInput<0:
        raise NumberZeroDivision
    else:
        print(UserInput)


a = UserException()