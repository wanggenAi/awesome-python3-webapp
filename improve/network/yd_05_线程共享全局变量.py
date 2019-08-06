import threading
import time
# 在一个函数中 对全局变量进行修改的时候，到底是否需要使用global进行说明
# 要看是否对全局变量的指向进行了修改，如果修改了指向，即让全局变量指向了一个新的地方，那么必须使用
# global，如果仅仅是修改指向的空间的数据，此时不需要使用global


def test1(temp):
    temp.append(33)
    print("-----in test1 temp=%s" % str(temp))


def test2(temp):
    print("----in test2 temp=%s" % str(temp))


g_num = [11,22]

def main():
    # args指定传递的参数
    t1 = threading.Thread(target=test1,args=(g_num,))
    t2 = threading.Thread(target=test2,args=(g_num,))
    t1.start()
    time.sleep(1)
    t2.start()
    time.sleep(1)

    print("-----in main thread g_num=%s" % str(g_num))


if __name__ == '__main__':
    main()