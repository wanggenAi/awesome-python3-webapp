class A:

    def test(self):
        print("test 方法")


class B:

    def test(self):
        print("demo 方法")


class C(B,A):
    def child(self):
        super().test()
        super().test()

c = C()
c.child()

#  多继承的使用注意事项  MRO （method resolution order）方法搜索顺序
print(C.__mro__)

