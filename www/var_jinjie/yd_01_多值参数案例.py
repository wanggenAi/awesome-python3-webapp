def sum_numbers(*args):
    num = 0
    print(args)
    #  循环遍历
    for i in args:
        num += i
    return num

result = sum_numbers(1,2,3,4)
print(result)