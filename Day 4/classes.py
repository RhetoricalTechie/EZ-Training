class A:
    x = 10
    __y = 30
    def s(self):
        print(self.x)
    def work(self,x):
        self.x = x



class B(A):
    pass



obj = B()
print(obj.x)
obj.s()
obj.work(20)
obj.s()

