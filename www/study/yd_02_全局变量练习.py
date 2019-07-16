num = 0

def demo1():
    #  希望修改全局变量的值 - 使用 global 声明一下变量即可
    #  就不会创建局部变量
    #  global num

    num = 2
    print("demo1 => %d" % num)

def demo2():
    print("demo2全局变量num => %d" % num)

demo1()
demo2()