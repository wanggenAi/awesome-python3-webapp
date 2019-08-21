print("******多继承使用super().__init__发生的状态********")
class Parent(object):
    def __init__(self, name, *args, **kwargs):
        print("parent的init开始被调用")
        self.name = name
        print('parent的init结束被调用')



class Son1(Parent):
    def __init__(self, name, age, *args, **kwargs):
        print("Son1的init开始被调用")
        self.age = age
        super().__init__(name, *args, **kwargs)
        print('Son1的init结束被调用')



class Son2(Parent):
    def __init__(self, name, gender, *args, **kwargs):
        print("Son2的init开始被调用")
        self.gender = gender
        super().__init__(gender, *args, **kwargs)
        print('Son2的init结束被调用')



class Grandson(Son1,Son2):
    def __init__(self, name, age, gender):
        print("Grandson的init方法被调用")
        super().__init__(name, age, gender)
        print("Grandson的init结束被调用")

print(Grandson.__mro__)
"""
在Python3中，使用C3算法处理super的调用顺序，保证super方法只会被调用一次
__mro__属性里会有一个元组，放父类方法的执行顺序，super()按照第一个值顺序开始，super(指定类名， self),从指定
的类顺序开始执行父类方法
*args，**kwargs *表示特殊功能
"""
def test2(a, b, *args, **kwargs):
    print("----------")
    print(a)
    print(b)
    print(args)
    print(kwargs)


def test1(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
    test2(a, b, *args, **kwargs) # 相当于test2(11,22,33,44,55,66,name="laowang",age=18)


test1(11, 22, 33, 44, 55, 66, name="laowang", age=18)
"""

"""





