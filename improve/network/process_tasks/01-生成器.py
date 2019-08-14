# 生成器是特殊的迭代器

# 只要函数里面有yied，那它就是一个生成器

def create_num(all_num):
    a, b = 0, 1
    current_num = 0

    while current_num < all_num:
        # print(a)
        yield a  # 这个函数就是一个生成器的模板
        a, b = b, a+b
        current_num += 1

# 创建生成器对象
obj = create_num(10)
ret = next(obj)
print(ret)
ret = next(obj)
print(ret)
ret = next(obj)
print(ret)