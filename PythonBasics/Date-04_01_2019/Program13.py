from datetime import date

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def birthday(cls, name, year):
        return cls(name, date.today().year - year)

    @staticmethod
    def isSeniorCitizen(age):
        return age > 50

D1 = Dog('Tessy', 10)
D2 = Dog.birthday('Jacky', 1998)
print(D1.age)
print(D2.age)
print(Dog.isSeniorCitizen(18))
print(Dog.birthday('Tommy',2015))
