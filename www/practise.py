#  练习格式化输出字符串
name = "小明"
print("我的名字叫%s,请多多指教" % name)

#  整型变量000001
stu_no = 1
print("我的学号是 %06d" % stu_no )

#  浮点类型
price,weight = 8.5,7.5
money = price * weight
print("苹果的单价是%.2f,买了%.2f 斤，总价是：%.2f" % (price,weight,money))

#  定义一个百分比的数字 89.23%
scale = 0.892353
print("百分比数字为 %.2f%%" % (scale * 100))

#  逻辑练习
#  从控制台输出要出的拳头 石头（1）/剪刀（2）/布（3）
import random
quantou = [0,"石头","剪刀","布"]
# while True:
#     player = int(input("输出要出的拳头 石头（1）/剪刀（2）/布（3）："))
#     computer = random.randint(1,3)
#     print("玩家选择的拳头是：%s ，电脑出拳是：%s" % (quantou[player],quantou[computer]))
#     #  比较胜负
#     if ((player==1 and computer==2)
#             or (player==2 and computer==3)
#             or (player==3 and computer==1)):
#
#         print("恭喜你赢了！")
#         res = int(input("还玩吗？1 玩/2 走了"))
#         if res == 2:
#             break
#     elif player == computer:
#         print("平局，再来")
#     else:
#         print("你输了彩笔")
#         res = int(input("还玩吗？1 玩/2 走了："))
#         if res == 2:
#             break

def multiple_table():
    """
    输出九九乘法表
    """
    row = 1
    while row <= 9:
        col = 1
        while col <= row:
            print('%d * %d = %d' % (col,row,col*row),end='\t')
            col += 1
        row += 1
        print()

    row = 1
    while row <= 9:
        print('*' * row)
        row += 1
