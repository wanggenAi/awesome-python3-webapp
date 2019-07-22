# __new__方法：在内存中创建对象的空间，并把对象地址引用传递给__init__方法

class MusicPlayer(object):

    def __new__(cls, *args, **kwargs):
        # 创建对象时，new方法会被自动调用
        print("创建对象，分配空间")
        # 分配空间
        instance = super().__new__(cls)
        # 返回引用
        return instance

    def __init__(self):
        print("播放器初始化")


player = MusicPlayer()
print(player)

# 单例类测试使用
player1 = MusicPlayer()
print(player1)
player2 = MusicPlayer()
print(player2)

