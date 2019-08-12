from collections import Iterable

class Classmate(object):
    def __init__(self):
        self.names = list()

    def add(self,name):
        self.names.append(name)

    def __iter__(self):
        """如果想要一个对象成为一个 可以迭代的对象 ，就必须实现__iter__方法"""
        return ClassIterator()

class ClassIterator(object):
    def __iter__(self):
         pass

    def __next__(self):
        pass



cm = Classmate()
cm.add("老王")
cm.add("类似")
cm.add("zhangsan")
cm.add("小鬼")

print("判断classmate是否是可以迭代的对象：", isinstance(cm,Iterable))
# for name in cm:
#     print(name)

