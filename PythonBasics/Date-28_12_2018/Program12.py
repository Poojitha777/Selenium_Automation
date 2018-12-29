a=int(input("Enter 1st no:"))
b=int(input("Enter 2nd no:"))
n=int(input("Enter no of terms:"))
print(a,b,end=" ")
while(n-2):
    c=a+b
    a=b
    b=c
    print(c,end=" ")
    n=n-1