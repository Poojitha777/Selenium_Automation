#WAP that displays which letters are in the first string but not in the second

FirstString=input("Enter first string:")
SecondString=input("Enter second string:")
print(set(FirstString)-set(SecondString))