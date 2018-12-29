#2 WAP to print the even no
class Even:
    def evenMethod(self):
        List=[1,2,3,4,5,6,7,8,9]
        Filter=filter(lambda List:List%2==0,List)
        print(list(Filter))
a=Even()
a.evenMethod()