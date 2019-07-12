# 判断空白字符
space_str = "\t\r\n"
print(space_str.isspace())

# 判断字符串中是否包含数字
#  num_str = "1.1"
num_str = "(2)"
print(num_str)
print(num_str.isdecimal())
print(num_str.isdigit())
print(num_str.isnumeric())

str_rep = "hello world"
print(str_rep.replace("hello","goodbye"))

poem = ["登黄鹤楼",
        "王之涣",
        "白日依山尽",
        "黄河入海流",
        "欲穷千里目",
        "更上一层楼"
        ]

for pl in poem:
    print("|%s|" % pl.center(10,""))

















