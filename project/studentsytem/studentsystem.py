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

#将学生信息保存到文件
def save(student):
    try:
        students_txt = open(filename,"a")   #以追加模式打开
    except Exception as e:
        students_txt = open(filename,"w")   #文件不存在，创建文件并打开
    for info in student:
        students_txt.write(str(info) + "\n")    #按行存储，添加换行符
    mZ()                    #关闭文件


#录入学生信息
def insert():
    stdentList = []         #奥村学生信息的列表
    mark = True             #是否继续添加
    while mark:
        id = input("请输入ID(如1001) : ")
        if not id:          #ID为空，跳出循环
            break
        name = input("请输入名字：")
        if not name:        #名字为空，跳出循环
            break
        try:
            english = int(input("请输入英语成绩："))
            python = int(input("请输入python成绩："))
            c = int(input("请输入C语言成绩："))
        except:
            print("输入无效,不是整型数值....重新录入信息")
            continue
        #将输入的学生的信息保存到字典
        stdent = {"id":id, "name":name, "english":english, "python":python, "c": c}
        stdentList.append(stdent)
        inputMark = input("是否继续添加?(y/n) :")
        if inputMark == "y":
            mark = True
        else:
            mark = False
        save(stdentList)                #将学生信息保存到文件
        print("学生信息录入完毕!!!")
        
def delete():
    mark = True
    while mark:
        studentId = input("请输入要删除的学生ID：")
        if studentId is not "":
            if os.path.exist(filename):
                with open(filename, 'r') as rfile:
                    student_old = rfile.readlines()
            else:
                student_old = []
            ifdel = False
            if student_old:
                with open(filename, 'w') as wfile:
                    d = {}
                    for list in student_old:
                        d = dict(eval(list))
                        if d['id'] != studentId:
                            wfile.write(str(d) + "\n")
                        else:
                            ifdel = True
                    if ifdel:
                        print("ID为 %s 的学生信息已经被删除..." % studentId)
                    else:
                        print("没有找到ID为 %s 的学生信息..." % studentId)
            else:
                print("无学生信息...")
                break
            show()
            inputMark = input("是否继续删除? (y/n) :")
            if inputMark == "y"
                mark = True
            else:
                mark = False
                  