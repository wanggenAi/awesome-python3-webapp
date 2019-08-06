import threading
import time

def test1():
    for i in range(5):
        print("-----test1----%d" % i)
        time.sleep(1)
        # 如果创建thread时执行的函数运行结束，意味着 这个子线程结束了....

def test2():
    for i in range(10):
        print("-----test2----%d" % i)
        time.sleep(1)

def main():
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)
    t1.start()
    t2.start()
    while True:
        print(threading.enumerate())
        if len(threading.enumerate()) <= 1:
            break
        time.sleep(1)

# 当调用Thread的时候，不会创建线程，当调用Thread创建出来的实例对象的start 方法的时候才会运行线程，和创建线程



if __name__ == '__main__':
    main()