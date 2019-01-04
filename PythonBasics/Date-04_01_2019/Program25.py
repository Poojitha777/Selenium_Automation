class PrintOdd:
    def __next__(self,number):
        self.number=number
        self.number += 2
        return self.number

p=PrintOdd()
for i in range(3):
    print(p.__next__(i))