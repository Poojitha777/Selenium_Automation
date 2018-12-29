#2   wap to find the maximum elements from a list using reduce
import functools

List = [67,444,5666,9000,-88,40,-20]
exp=functools.reduce(lambda m,n:m if m>n else n,List)
print(exp)

