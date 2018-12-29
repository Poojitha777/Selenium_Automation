#WAP to read a list a words and return the length of the longest one
a = int(input("Enter the number of words"))
List = []
ListLength = []
for i in range(a):
    b = input("Enter number")
    List.append(b)
    ListLength.append(len(b))

print(List)
print(ListLength)
print("The length of longest word is:", max(ListLength))

