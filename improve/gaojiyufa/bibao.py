# 闭包
def line(k, b):
    def create_y(x):
        print(k*x+b)
    return create_y

line6 = line(1, 2)
line6(0)
line6(1)
line6(2)

# 闭包2
x = 400
def test1():
    x = 300
    def test2():
        # nonlocal x
        global x
        print(x)
        x = 200
        print(x)
    return test2

t2 = test1()
t2()
