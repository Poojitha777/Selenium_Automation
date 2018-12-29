#Constructor
class Builder:
    def __init__(self):
        self.year = 100

    def number(self):
        print(self.year)

a = Builder()
a.number()