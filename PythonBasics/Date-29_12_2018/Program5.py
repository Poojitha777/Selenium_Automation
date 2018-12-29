#WAP to find all the numbers in a range which are perfect squares and sum of all
#digits in the number are less than 100
import math

for i in range(20):
    a = int(math.sqrt(i))
    if i == a*a:
        print(i, "is a perfect square")
    else:
        print(i,"is not a perfect square")