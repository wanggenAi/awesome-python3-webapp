class Tool(object):

    # 使用赋值语句定义类属性，记录所有工具对象的数量
    count = 0

    @classmethod
    def show_tool_count(cls):
        print("工具对象的数量 %d " % cls.count)

    def __init__(self,name):
        self.name = name
        # 让类属性的值+1
        Tool.count += 1


tool1 = Tool("tool1")
tool2 = Tool("tool2")
Tool.show_tool_count()
