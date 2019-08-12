import threading
import time

# 定义一个全局变量
g_num = 0

#创建一个互斥锁，默认是没有上锁的
mutex = threading.Lock()

def test1(num):
    global g_num
    # 上锁，如果之前没有被上锁则上锁成功，如果已经被上锁了那么此时会堵塞这里，知道这个锁被解开为止
    mutex.acquire()
    for i in range(num):
        g_num += 1
    mutex.release()
        # print("-----in test1 g_num=%d" % g_num)

def test2(num):
    global g_num
    mutex.acquire()
    for i in range(num):
        g_num += 1
    mutex.release()
    # print("----in test2 temp=%s" % str(g_num))



def main():
    # args指定传递的参数
    t1 = threading.Thread(target=test1,args=(1000000,))
    t2 = threading.Thread(target=test2,args=(1000000,))
    t1.start()
    t2.start()
    time.sleep(2)
    print("-----in main thread g_num=%d" % g_num)


if __name__ == '__main__':
    main()