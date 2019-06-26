"""
    界面模块
"""
from bll import StudentManagerController
from model import StudentModel


# 界面视图类
class StudentManagerView:
    """
        学生管理器视图
    """

    def __init__(self):
        # 将类实体化
        self.__manager = StudentManagerController()

    def __display_menu(self):
        """
            显示菜单
        """
        print("1>增加学生信息")
        print("2>显示学生信息")
        print("3>删除学生信息")
        print("4>修改学生信息")
        print("5>按成绩低～高显示学生信息")
        print("0>退出管理")

    def __select_menu(self):
        """
            选择菜单项
        """
        i = int(input("please enter menu option:"))
        if i == 0:
            # 让程序中断
            raise ValueError("退出循环")
        elif i == 1:
            self.__input_student()
        elif i == 2:
            self.__output_students(self.__manager.stu_list)
        elif i == 3:
            self.__delete_student()
        elif i == 4:
            self.__modify_student()
        elif i == 5:
            self.__output_student_by_score()

    def main(self):
        """
            入口逻辑
        """
        while True:
            self.__display_menu()
            self.__select_menu()

    def __input_student(self):
        """
            将用户输的信息增加到列表中
        """
        name = input("please enter name:")
        age = int(input("please enter age:"))
        score = int(input("please enter score:"))
        stu = StudentModel(name, age, score)
        self.__manager.add_student(stu)

    def __output_students(self, list_output):
        """
            显示所有学生信息
        :param list_output:用户输入信息存储的列表
        """
        for i in list_output:
            StudentModel.output_student_info(i)

    def __delete_student(self):
        """
            删除学生信息，根据ID
        """
        i = int(input("please enter delete ID:"))
        self.__manager.remove_student(i)

    def __modify_student(self):
        """
            修改学生信息
        """
        id = int(input("please enter delete ID:"))
        name = input("please enter name:")
        age = int(input("please enter age:"))
        score = int(input("please enter score:"))
        stu = StudentModel(name, age, score, id)
        self.__manager.update_student(stu)

    def __output_student_by_score(self):
        """
            升序成绩显示所有
        """
        list_target = self.__manager.order_by_score()
        self.__output_students(list_target)
