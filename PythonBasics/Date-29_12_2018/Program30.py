#WAP to reverse the words of odd index value in a string
FirstString = "Welcome to the world of Python"
a = FirstString.split()
List = []
for i in range(len(a)):
    if i%2==0:
        b=a[i]
        List.append(b[::-1])
    else:
        List.append(a[i])
print(List)