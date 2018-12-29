#Garbage Collection
import gc
i = 0
def round():
    x = {}
    x[i + 1] = x
    print(x)
collected = gc.collect()
print("Garbage collector: collected %d objects" % (collected))
for i in range(10):
    round()
collected = gc.collect()
print("Garbage collector: collected %d objects" % (collected))