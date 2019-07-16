def measure():
    """测量温度和湿度"""
    print("测量开始")
    temp = 39
    wetness = 50
    print("测量结束...")

    #  元组-可以包含多个数据 ，因此可以使用元组让函数一次性返回多个值
    #  返回值为元组，小括号可以省略
    return temp,wetness

result = measure()
print("温度：%d" % result[0])
print("湿度：%d" % result[1])

#  变量交换
a,b = 10,5
a,b = b,a
print(a)
print(b)
