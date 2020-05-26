class Calc():
    def __init__(self,a):
        self.a = a


    def fun1(self):
        b = self.a*2
        return b

    def fun2(self,c):
        return c*2


class Main():
    def __init__(self):
        self.aa = 1
        self.c1 = 5

    def run(self):

        
        calc1 = Calc(self.aa)
        
        bb = calc1.fun1()
        cc = calc1.fun2(self.c1)
        print('bb:',bb)
        print('cc:',cc)

if __name__ == '__main__':
    test = Main()
    test.run()
    
    
