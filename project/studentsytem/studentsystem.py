def main():
    ctrl = True
    while (ctrl):
        menu()
        option = input("请选择: ")
        """
        re 正则表达式模块
        sub 替换
        \D 表示非0-9的字符
        含义:把非0-9的数字字符用""替换
        请选择:5=>5
        """
        option_str = re.sub("\D", "", option)
        if option_str in ['0', '1', '2', '3', '4', '5', '6', '7']:
            option_int = int(option_str)
            if option_int == 0:
                print('您已退出学生信息管理系统! ')
                ctrl = False
            elif option_int == 1:
                insert()
            elif option_int == 2:
                search()
            elif option_int == 3:
                delete()
            elif option_int == 4:
                modify()
            elif option_int == 5:
                sort()
            elif option_int == 6:
                total()
            elif option_int == 7:
                show()
       # 

def menu():
    #输出菜单:wq
    print('''
    ---------------------学生信息管理系统----------------------

    1.录入学生信息
    2.查找学生信息
    3.删除学生信息
    4.修改学生信息
    5.排序
    6.统计学生总人数
    7.显示所有学生信息
    0.退出系统
    ------------------------------------------------------------
    说明：通过数字或上下方向键选择菜单里的功能
          ''')
