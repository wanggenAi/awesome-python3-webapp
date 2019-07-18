class Women:
    def __init__(self,name):
        self.name = name
        self.__age = 18

    def __secret(self):
        #  在对象的方法内部，是可以访问对象的私有属性的
        print("%s 的年龄是 %d" % (self.name,self.__age))

    def prsec(self):
        self.__secret()

xiaofang = Women("小芳")
#  伪私有属性、方法在外界不能被直接访问
#  print(xiaofang.__age)
#  只能使用 _类名__私有方法名
print(xiaofang._Women__age)
xiaofang._Women__secret()

#  验证子类对象能否访问父类对象的私有属性和方法
class A:
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200

    def __test(self):
        print("私有方法 %d %d" % (self.num1,self.__num2))

    def test(self):
        print("父类的共有方法")

class B(A):
    def demo(self):
        print("访问父类私有属性 %d" % self.num1)
        # 2.调用父类的私有方法  报错
        # self.__test()
        pass

# 在外界不能访问私有属性方法，除非用_A__test
b = B()
b.demo()
