#1wAP to multiply all the elements inside a list using reduce
import functools
List = [45,23,2,6,34]
exp=functools.reduce(lambda m,n:m*n,List)
print(exp)

