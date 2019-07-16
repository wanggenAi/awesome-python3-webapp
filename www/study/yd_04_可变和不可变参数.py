def demo(num):
    print("函数内部的代码")

    #  在函数内部，针对参数使用复制语句
    num = 100
    print(num)
    print("函数执行完成")

gl_num = 99
demo(gl_num)
print(gl_num)


#  如果使用可变变量，使用方法改变就会改变全局变量，但是赋值语句不会改变内容
def demo2(num_list):
    print("demo2内部函数")
    num_list = [1,2,3]
    print("内部函数：", num_list)
    print("函数执行完成")


gl_list = [4,6,7]
demo2(gl_list)
print(gl_list)

#  使用方法来改变可变参数的内容
def demo3(num_list):
    num_list.append(9)
    print(num_list)

gl_kebian = [1,2,3]
demo3(gl_kebian)
print(gl_kebian)