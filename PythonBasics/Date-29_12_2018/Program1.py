#WAP to put even and odd numbers in a list in to two different lists
List = [1,2,3,4,5,6,7,8,9,10]
evenNumbers = []
oddNumbers = []

for i in List:
    if i%2==0:
        evenNumbers.append(i)
    else:
        oddNumbers.append(i)

print(evenNumbers)
print(oddNumbers)

