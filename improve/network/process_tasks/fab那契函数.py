from collections import Iterable
from collections import Iterator
import time

class Fibonacci(object):
    def __init__(self,all_num):
        self.all_num = self.all_num
        self.current_num = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        """如果想要一个对象成为一个 可以迭代的对象 ，就必须实现__iter__方法"""
        return self

    def __next__(self):
        if self.current_num <= self.all_num:
            ret = self.a
            self.a, self.b = self.b, self.a + self.b
            self.current_num += 1
            return ret
        else:
            raise StopIteration



'''
for temp in xxx_obj:
    pass
1.判断xxx_obj是否可以迭代
2.第1步成立，调用iter函数得到xxx_obj对象的__iter__方法的返回值
3.__iter__方法的返回值 是一个迭代器
'''
cm = Fibonacci()


for name in cm:
    print(name)
    time.sleep(1)


