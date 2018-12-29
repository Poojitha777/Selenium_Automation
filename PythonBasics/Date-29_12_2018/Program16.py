#WAP to check common letters in two input strings

FirstString=input("Enter first string:")
SecondString=input("Enter second string:")
ThirdString=set(set(FirstString)&set(SecondString))
if len(ThirdString)>0:
    print("The Commonly repeated letters present in both strings are", ThirdString)
