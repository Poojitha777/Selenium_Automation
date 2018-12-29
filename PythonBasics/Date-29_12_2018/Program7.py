#WAP to map two lists in to a dictionary
import operator
List1 = [1,2,3]
List2 = [4,5,6]
Sum = list(map(operator.add, List1, List2))
print((Sum))

