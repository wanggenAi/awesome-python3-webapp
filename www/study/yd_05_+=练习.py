def demo(num,num_list):
    print("函数开始")
    num += num
    print(num)

    #  列表的+=等运算操作，不会做相加再复制的操作，本质上是在调用extend方法
    num_list += num_list
    print(num_list)
    print("函数结束")

gl_num = 9
gl_list = [1,2,3]
demo(gl_num,gl_list)
print(gl_num,gl_list)
