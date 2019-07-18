class Cat:

    def __init__(self,new_name):
        self.name = new_name
        print("%s 来了" % self.name)

    #  删除操作
    def __del__(self):
        print("%s 走了" % self.name)

    #  __str__方法,必须返回一个字符串，print打印变量默认是显示所属类，还有16进制的内存地址
    def __str__(self):
        return "我是猫 %s" % self.name


tom = Cat("Tom")
#  del tom
print("-"*50)
print(tom)