class HouseItem:
    def __init__(self,name,area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s] 占地 %.2f" % (self.name,self.area)


class House:
    def __init__(self,house_type,area):
        self.house_type = house_type
        self.area = area

        #  剩余面积
        self.free_area = area
        #  家具列表
        self.item_list = []
    def __str__(self):
        return ("户型是：%s \n总面积：%.2f\n剩余面积：%.2f\n家具：%s"
                % (self.house_type,self.area,
                   self.free_area,self.item_list))

    def add_item(self,item):
        print("要添加 %s" % item)
        #  1.判断家具的面积
        if item.area > self.free_area:
            print("%s 的面积太大了，无法添加" % item.name)
            return

        #  2.将家具的名称添加到
        self.item_list.append(item.name)
        #  3.计算剩余面积
        self.free_area-=item.area
#  创建家具
#  床
bed = HouseItem("席梦思",4)
print(bed)
#  衣柜
chest = HouseItem("衣柜",2)
print(chest)
#  餐桌
table = HouseItem("餐桌",1.5)
print(table)

house = House("三室一厅",78)
print(house)

house.add_item(bed)
print(house)