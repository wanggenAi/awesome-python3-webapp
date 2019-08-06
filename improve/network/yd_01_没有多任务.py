import time


def main():
    sting()
    dance()


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