class Iterate(object):
    def __init__(self, fail, passs):
        self.fail = fail
        self.passs = passs

    def __iter__(self):
        return self

    def __next__(self):

        if self.fail > self.passs:
            raise StopIteration
        else:
            self.fail += 1
            return self.fail - 1

N = Iterate(1,10)
for i in N:
    print(i)