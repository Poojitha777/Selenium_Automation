#WAP to raise a type error if the input is not an integer
UserInput=input("Please enter a number")
if UserInput.isdigit():
    pass
else:
    print("The number which is entered is not a number")
    raise TypeError