import multiprocessing

def download_from_web(q):
    # 模拟从网上下载的数据
    data = [11,22,33,44]

    # 向队列中写入数据
    for temp in data:
        q.put(temp)
    print("---下载器已经下载完了数据并存入到队列中---")


def analysis_data(q):
    """数据处理"""
    waitting_analiysis_data = list()
    # 从队列中获取数据，模拟数据处理
    while True:
        if q.empty():
            break
        data = q.get()
        waitting_analiysis_data.append(data)
    print(waitting_analiysis_data)

def main():
    # 创建一个队列
    q = multiprocessing.Queue()
    # 创建多个进程，将队列的引用当做实参进行传递到里面
    p1 = multiprocessing.Process(target=download_from_web, args=(q,))
    p2 = multiprocessing.Process(target=analysis_data, args=(q,))
    p1.start()
    p2.start()


if __name__ == '__main__':
    main()