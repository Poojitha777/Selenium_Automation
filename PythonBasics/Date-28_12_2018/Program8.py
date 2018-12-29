#Firstmethod
List=[9,7,6,5,9,4,7,4,6,5]
print(set(List))
#Secondmethod
List2=[]
for i in List:
    if i not in List2:
        List2.append(i)
print(List2)
#Thirdmethod
a = dict.fromkeys(List).keys()
print(a)
#Fourthmethod
[List2.append(i) for i in List if i not in List2]
print(List2)


