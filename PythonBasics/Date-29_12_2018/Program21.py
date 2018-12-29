class Iphone5s:
    a=10
class Iphone6s:
    a=20
class Iphone7Plus(Iphone5s,Iphone6s):
    b=67

ob=Iphone7Plus()
print(ob.a)


