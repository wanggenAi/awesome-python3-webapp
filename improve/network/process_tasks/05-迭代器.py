from collections import Iterable
from collections import Iterator
import time

class Classmate(object):
    def __init__(self):
        self.names = list()

    def add(self,name):
        self.names.append(name)

    def __iter__(self):
        """如果想要一个对象成为一个 可以迭代的对象 ，就必须实现__iter__方法"""
        return ClassIterator(self)

class ClassIterator(object):

    def __init__(self,obj):
        self.obj = obj
        self.iter = iter(obj.names)

    def __iter__(self):
         pass

    def __next__(self):
        # 或者抛出 StopIteration 异常也会告诉for 停止迭代
        return next(self.iter)

'''
for temp in xxx_obj:
    pass
1.判断xxx_obj是否可以迭代
2.第1步成立，调用iter函数得到xxx_obj对象的__iter__方法的返回值
3.__iter__方法的返回值 是一个迭代器
'''
cm = Classmate()
claI = iter(cm)
cm.add("老王")
cm.add("类似")
cm.add("zhangsan")
cm.add("小鬼")
print("判断classmate是否是可以迭代的对象：", isinstance(cm,Iterable))
print("判断claI是否是迭代器对象Iterator：",isinstance(claI,Iterator))

for name in cm:
    print(name)
    time.sleep(1)


