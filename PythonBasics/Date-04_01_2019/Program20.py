class Automation():

    def __init__(self, z):
        self.z = z

    def __call__(self):
        print("start", self.z.__name__)
        self.z()
        print("stop", self.z.__name__)

@Automation
def method1():
    print("calling method1")

@Automation
def method2():
    print("calling method2")

method1()
method2()