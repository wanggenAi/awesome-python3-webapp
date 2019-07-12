
#  将多个字典放入到一个列表中，再进行遍历
card_list = [{
    "name":"张三",
    "qq":"123123",
    "phone":"412412"
},{
    "name": "李四",
    "qq": "5436",
    "phone": "3756859"
}]

for card_info in card_list:
    print('-'*50)
    for k in card_info:
        print('%s - %s' % (k,card_info[k]))
    print('-'*50)
