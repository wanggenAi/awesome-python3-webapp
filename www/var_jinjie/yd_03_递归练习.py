#  求1到n数字的和
def sum_num(num):
    if num == 1:
        return 1
    else:
        return num + sum_num(num-1)


print(sum_num(5))