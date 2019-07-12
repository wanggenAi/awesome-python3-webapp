xiaoming_dict = {"name":"xiaoming"}
# 1. 取值
print(xiaoming_dict["name"])
#  print(xiaoming_dict["name123"])

#  2. 增加/修改
#  如果key不存在，会新增键值对，如果key存在，会修改已经存在的键值对
xiaoming_dict["age"] = 18
xiaoming_dict["name"] = '小小明'
#  3. 删除
#  xiaoming_dict.pop("name123")
#  xiaoming_dict.pop("name")

#  统计键值对的数量
print(len(xiaoming_dict))

#  2. 合并字典
#  如果被合并的字典中包含已经存在的键值对，会覆盖原有的键值对
temp_dict = {"height":1.75,"age":20}
xiaoming_dict.update(temp_dict)

#  3. 清空字典
xiaoming_dict.clear()


print(xiaoming_dict)