class Animal:
    def eat(self):
        print("吃")
    def drink(self):
        print("喝")
    def run(self):
        print("跑")
    def sleep(self):
        print("睡")

class Dog(Animal):
    def bark(self):
        print("汪汪")

class XiaoTianQuan(Dog):
    def fly(self):
        print("飞飞飞")
    def bark(self):
        # 1.针对子类特有的需求
        print("神叫")
        # 2.使用super(). 调用原本在父类中封装的方法
        super().bark()



#  类的继承具有传递性
xtq = XiaoTianQuan()
# xtq.eat()
# xtq.run()
# xtq.sleep()
xtq.bark()
# xtq.fly()