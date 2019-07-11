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


