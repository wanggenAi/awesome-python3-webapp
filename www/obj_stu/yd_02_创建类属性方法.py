#  不推荐在类的外部创建属性

#  对象应该包含有哪些属性，应该封装在类的内部

#  当使用类名()创建对象时，会自动执行一下操作：
"""
    1.为对象在内存中分配空间 --创建对象
    2.为对象的属性设置初始值--初始化方法（init）
"""
class Cat():
    """这是一个猫类"""
    def __init__(self,new_name):
        print("初始化方法")
        #  猫类的属性
        self.name = new_name
    def eat(self):
        print("%s 爱吃鱼" % self.name)

#  __init__方法是专门用来定义个类有哪些属性
tom = Cat("Tom")
print(tom.name)
tom.eat()

lazy_cat = Cat("大懒猫")
lazy_cat.eat()

