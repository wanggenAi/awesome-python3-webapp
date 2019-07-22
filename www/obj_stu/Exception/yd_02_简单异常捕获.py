# try:
#     num = int(input("请输入一个整数："))
# except:
#     print("请输入正确的整数！")
#
# print("-" * 50)

try:
    num = int(input("请输入一个整数："))
    result = 8 / num
    print(result)
except ZeroDivisionError:
    print("除0错误")
except Exception as e:
    print("未知错误 %s" % e)
else:
    print("尝试成功")
finally:
    print("程序结束")

print("-" * 50)

# 捕获未知错误




