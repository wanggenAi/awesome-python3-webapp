# def demo1():
# #     return  int(input("请输入一个整数"))
# #
# # def demo2():
# #     return demo1()
# #
# # # 利用异常的传递性，在主程序中捕获异常
# # try:
# #     print(demo2())
# # except Exception as e:
# #     print(e)
# #
# # print("-" * 60)

def input_pass():
    pwd = input("请输入密码：")
    if len(pwd) >= 8:
        return pwd
    print("抛出异常")
    ex = Exception("密码长度不够")
    raise ex

try:
    abc = input_pass()
except Exception as e:
    print(e)

