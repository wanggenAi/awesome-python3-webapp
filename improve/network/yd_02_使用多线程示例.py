import time
import threading

def main():
    t1 = threading.Thread(target=sting)
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()


def sting():
    for i in range(5):
        print("唱........ge..."+str(i))
        time.sleep(1)


def dance():
    for i in range(5):
        print("跳。。。。。。。五")
        time.sleep(1)

if __name__ == '__main__':
    main()