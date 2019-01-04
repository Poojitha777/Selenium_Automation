class IterateProgram:
    def __init__(self,size , maxNumber):
        self.size = size
        self.maxNumber= maxNumber
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.maxNumber:
            raise StopIteration
        self.count += 1
        return self.size

result = IterateProgram('wassup',10)
for i in result:
    print(i)