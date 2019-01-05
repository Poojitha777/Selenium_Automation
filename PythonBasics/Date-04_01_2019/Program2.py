import itertools as it
List1= [89,998,566]
List2=[7665,7,7]

result = sorted([i for i in it.chain(List1,List2)])
print(result)


