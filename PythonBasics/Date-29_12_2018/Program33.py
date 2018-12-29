#Destructor
class A:
    def __init__(self):
        print("Its Constructor")
    def __del__(self):
        print("Its destructor")
ob=A()
del ob
print(ob)