from collections import Iterable
from collections import Iterator
import time

class Classmate(object):
    def __init__(self):
        self.names = list()
        self.current_num = 0

    def add(self,name):
        self.names.append(name)

    def __iter__(self):
        """如果想要一个对象成为一个 可以迭代的对象 ，就必须实现__iter__方法"""
        return self

    def __next__(self):
        if self.current_num < len(self.names):
            name = self.names[self.current_num]
            self.current_num += 1
            return name
        else:
            raise StopIteration



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

for name in cm:
    print(name)
    time.sleep(1)


