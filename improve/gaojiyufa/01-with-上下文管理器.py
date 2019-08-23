from contextlib import contextmanager

class File():

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print("entering")
        self.f = open(self.filename, self.mode)
        return  self.f

    def __exit__(self, *args):
        print("will exit")
        self.f.close()


with File('out.txt', 'w') as f:
    print("waiting")
    f.write('hello,python')

@contextmanager
def my_open(path, mode):
    f = open(path, mode)
    yield f
    f.close()

with my_open("out.txt", "w") as f:
    f.write("装饰器的上下文调用方法")