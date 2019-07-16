#  在使用面向对象开发前，应该首先分析需求，确定一下需要有哪些类

#  变量、数据、函数 都是对象

#  dir函数，可以查看对象所有的属性和方法
def demo():
    """这是一个测试文档"""
    print("hello py")

print(dir(demo))

print(demo.__doc__)

#  定义类练习
class Cat:
    def eat(self):
        print("猫吃鱼")

    def drink(self):
        print("猫喝水")

#  创建猫对象
tom = Cat()
tom.name = "heihei"
tom.eat()
tom.drink()

print(tom)
addr = id(tom)
print('%x' % addr)

tom2 = tom

tom.name = "heihei"

print(tom2.name)
