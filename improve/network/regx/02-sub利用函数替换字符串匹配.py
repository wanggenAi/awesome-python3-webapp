import re

def num(temp):
    reg_num = temp.group()
    newnum = int(reg_num) + 1
    return str(newnum)


newstr = re.sub("\d+", num, "python = 666")
print(newstr)
