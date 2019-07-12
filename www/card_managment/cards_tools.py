#  定义全局列表变量
card_list = []


def show_menu():
    """显示菜单"""
    print("*" * 50)
    print("欢迎使用【名片管理系统】V 1.0")
    print()
    print("1. 新增名片")
    print("2. 显示全部")
    print("3. 搜索名片")
    print()
    print("0. 退出系统")
    print("*" * 50)

def new_card():
    """新增名片"""
    print('-'*50)
    print("新增名片")

    # 提示输入
    name_str = input("请输入姓名：")
    phone_str = input("请输入电话：")
    qq_str = input("请输入QQ号：")
    email_str = input("请输入邮箱：")

    card_dict = {
        "name":name_str,
        "phone":phone_str,
        "qq":qq_str,
        "email":email_str
    }
    card_list.append(card_dict)
    print(card_list)
    print("添加 %s 的名片成功" % name_str)

def show_all():
    """显示所有名片"""
    print('-'*50)
    print("显示所有名片")

    #  判断是否存在名片记录，如果没有，提示用户并且返回
    if len(card_list) == 0:
        print("当前没有任何名片记录，请使用新增功能添加名片！")
        return

    #  打印表头
    for col in ['姓名','电话','QQ','邮箱']:
        print(col,end="\t\t\t")
    print()
    #  打印分割线
    print("="*50)
    for cd in card_list:
            print("%s\t\t%s\t\t%s\t\t%s" % (cd["name"],cd["phone"],cd["qq"],cd["email"]))

def search_card():
    """搜索名片"""
    print('-'*50)
    print("搜索名片")

    # 提示搜索姓名信息：
    name_str = input("请输入要搜索的姓名：")
    #  遍历名片列表看有没有这个人
    for per in card_list:
        if name_str == per["name"]:
            #  打印表头
            for col in ['姓名', '电话', 'QQ', '邮箱']:
                print(col, end="\t\t\t")
            print()
            #  打印分割线
            print("=" * 50)
            for cd in card_list:
                print("%s\t\t%s\t\t%s\t\t%s" % (cd["name"], cd["phone"], cd["qq"], cd["email"]))

            #  针对找到的名片信息修改和删除的操作
            deal_card(cd)

            break
    else:
        print("抱歉！查无此人")


def deal_card(find_dict):
    """处理找到的名片
    :rtype: object
    """
    #  print(find_dict)
    action_str = input("请选择要执行的操作："
                       "[1] 修改 [2] 删除 [0] 返回上级菜单 ")
    if action_str == "1":
        print("修改名片")
        find_dict["name"] = input("姓名：[回车不修改]") or find_dict["name"]
        find_dict["phone"] = input("电话：[回车不修改]") or find_dict["phone"]
        find_dict["qq"] = input("QQ：[回车不修改]") or find_dict["qq"]
        find_dict["email"] = input("邮箱：[回车不修改]") or find_dict["email"]
        print("修改 %s 的名片成功！" % find_dict["name"])
    elif action_str == "2":
        print("删除名片")
        card_list.remove(find_dict)
        print("删除 %s 的名片成功" % find_dict["name"])