# from www.study.module_exec.yd_01_模块1 import say_hello as mo1
# from www.study.module_exec.yd_01_模块2 import say_hello
#
# mo1()
# say_hello()
# 在导入模块时，会将模块内的所有没有缩进的代码全部执行一遍
import random

# print(random.__file__)
print("-" * 50)

import www.study.yd_mssage as yd_mssage
yd_mssage.send_message.send("你好，哈哈")

