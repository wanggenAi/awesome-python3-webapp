stu = [
    {"name":"三1"},
    {"name":"三2"}
]

find_name = "三8"

for s in stu:
    #  print(s)
    if s["name"] == find_name:
        print("%s 在字典中存在" % find_name)
        break
else:
    print("未找到%s" % find_name)