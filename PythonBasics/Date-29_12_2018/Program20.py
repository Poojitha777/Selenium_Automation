class Laptop:
    def __init__(self):
        self.name = 'Sony'
        self.version = 'windows10'

    def getName(self):
        return self.name


class Tablet:
    def __init__(self):
        self.name = 'Dell'
        self.id = '32'

    def getName(self):
        return self.name


class Mobile(Laptop, Tablet):
    def __init__(self):
        Laptop.__init__(self)
        Tablet.__init__(self)

    def getName(self):
        return self.name


mobile = Mobile()
print(mobile.getName())