name_list = ["zhangsan","lisi","wangwu"]

#  1. 取值和取索引
print(name_list[0])
#  使用index方法需要注意，如果数据不在列表中，程序会报错！
print(name_list.index("lisi"))
#  2. 修改
name_list[2] = "嘿嘿"
temp_list = ["小黑","xiaohua","不嗔"]
name_list.insert(2,"wanggen")
name_list.extend(temp_list)
print(name_list)
#  3. 添加
#  4. 删除
name_list.insert(2,"zhangsan")
name_list.insert(3,"zhangsan")
name_list.insert(4,"zhangsan")
name_list.remove("zhangsan")
print(len(name_list))
print(name_list)
