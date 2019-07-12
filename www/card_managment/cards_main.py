import www.card_managment.cards_tools as cards_tools

while True:
    #   显示功能菜单
    cards_tools.show_menu()
    action_str = input("请选择希望执行的操作：")
    print("您选择的操作是【%s】" % action_str)
    if action_str in ["1","2","3"]:
        #  1. 新增名片
        if action_str == "1":
            cards_tools.new_card()
        #  2. 显示全部
        elif action_str == "2":
            cards_tools.show_all()
        #  3. 查询名片
        elif action_str == "3":
            cards_tools.search_card()
        pass
    elif action_str == "0":
        # 退出系统
        print("欢迎下次再来使用【名片管理系统】，再见")
        break
    else:
        print("您的输入不正确，请重新输入")
