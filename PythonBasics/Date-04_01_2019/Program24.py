class PrintOddNumber:
    def __iter__(self):
        self.ele = 1
        return self

    def __next__(self):
        ele = self.ele
        self.ele += 2
        return ele

i=iter(PrintOddNumber())
for p in range(25):
    print(next(i))