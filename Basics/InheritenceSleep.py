import time

class Father :
    def __init__(self):
        print("In Father Class")
    def loopfunc(self,val):
        for i in range(1,5):
            print(i)
            time.sleep(val)



class Son(Father) :
    def __init__(self):
        print("In Son Class")

obj = Father()
obj1 = Son()

obj.loopfunc(3)
obj1.loopfunc(1)