class Calc:
    def __init__(self):
        self.ret_val=0
    def hab(self,int_num):
        self.ret_val +=int_num
        return self.ret_val

cc=Calc()
a=int(input())
print(cc.hab(a))
b=int(input())
print(cc.hab(b))