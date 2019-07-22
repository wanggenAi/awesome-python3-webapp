class MusicPlayer():
    instance = None
    isFlag = False
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
            return cls.instance
        return cls.instance

    def __init__(self):
        if MusicPlayer.isFlag:
            return
        print("执行初始化")
        MusicPlayer.isFlag = True

p1 = MusicPlayer()
p2 = MusicPlayer()

print(p1)
print(p2)

# 对于单例模式，初始化方法如何只执行一次？
