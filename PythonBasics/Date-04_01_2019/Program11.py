#Magic Method __init__

class car:
    def __init__(self,name,mileage):
        self.name=name
        self.mileage=mileage

class brand(car):
    def __call__(self,name,mileage):
        super().__init__(name,mileage)


p=brand("Fortuner",25)
c=brand("Benz",15)
print(p.name)
print(c.mileage)