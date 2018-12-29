#WAP to generate random numbers from 1 to 20 and append them to the list
import random
List = []
for  i in range(3):
    r = random.randint(1,20)
    List.append(r)

print(List)


