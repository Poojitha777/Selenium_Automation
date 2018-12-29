#1WAP to print the odd no
class Odd:
    def OddMethod(self):
        List = [33,12,24,55,2,8,66]
        Filter=filter(lambda List:List%2!=0,List)
        print(list(Filter))
ob=Odd()
ob.OddMethod()