#WAP for the zerodivision

UserInput=int(input("Enter the number"))
output=UserInput/0
print(output)

try :
    UserInput = int(input("Please,enter a number"))
    output = UserInput / 0
    print(output)
except Exception as q:
    print(type(q))