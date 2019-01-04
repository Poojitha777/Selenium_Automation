class Fruit:
    def orange(self):
        return 'instance method called', self

    @classmethod
    def orangeclassmethod(cls):
        return 'class method called', cls

    @staticmethod
    def orangestaticmethod():
        return 'static method called'

p=Fruit()
print(p.orange())
print(p.orangeclassmethod())
print(Fruit.orangeclassmethod())
print(p.orangestaticmethod())
print(Fruit.orangestaticmethod())