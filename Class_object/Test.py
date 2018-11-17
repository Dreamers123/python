import Test1
class A:
    life=3
    def __init__(self,x):
        self.captain=x
    def YAI_captain(self):
        if(self.life<=0):
         self.captain-=1
         print("Captin is still alive " +str(self.captain))
        else:
            print("All dead")


    def attack(self):
        print("Ouch!!!")
        self.life-=1
    def check(self):
        if self.life <=0:
            print("I am dead")
        else:
            print("Life left " +str(self.life))
class B(A):
  pass

Abeer=B(5)
Abeer.attack()
Abeer.check()
Abeer.attack()
Azad=A(5)
Test1
Abeer.YAI_captain()

