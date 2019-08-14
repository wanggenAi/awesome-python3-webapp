import gevent
import urllib.request
from gevent import monkey

monkey.patch_all()


def f(img_name, img_url):
    req = urllib.request.urlopen(img_url)
    img_content = req.read()
    with open(img_name, 'wb') as f:
        f.write(img_content)


def main():
    gevent.joinall([
        gevent.spawn(f, "./picture/1.jpg", "https://rpic.douyucdn.cn/asrpic/190813/6082718_7357631_10da0_2_1119.jpg/dy1"),
        gevent.spawn(f, "./picture/2.jpg", "https://rpic.douyucdn.cn/live-cover/appCovers/2019/08/05/7148355_20190805205052_small.jpg/dy1"),
    ])


if __name__ == '__main__':
    main()