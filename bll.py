"""
    业务逻辑模块
"""

# 逻辑控制类
class StudentManagerController:
    """
        学生管理控制器，负责业务逻辑处理
    """
    # 类变量　初始ID
    __init_id = 1000

    def __init__(self):
        self.__stu_list = []

    @property
    def stu_list(self):
        """
            学生列表
        :return: 存储学生对象的列表
        """
        return self.__stu_list

    def add_student(self, stu_info):
        """
            添加一个新学生
        :param stu_info: 没有编号的学生信息
        """
        # 让id等于产生的那个新的ｉｄ
        stu_info.id = self.__generate_id()
        self.__stu_list.append(stu_info)

    def __generate_id(self):
        """
            产生一个新的ＩＤ，依次递增
        :return:新的ＩＤ
        """
        StudentManagerController.__init_id += 1
        return StudentManagerController.__init_id

    def remove_student(self, stu_id):
        """
            根据学生ｉｄ删除指定学生信息
        :param stu_id: 学生ｉｄ
        :return: True #表示移除成功    False #表示移除失败
        """
        for i in self.__stu_list:
            if i.id == stu_id:
                self.__stu_list.remove(i)
                return True
        return False

    def update_student(self, stu_info):
        """
            修改学生信息
        :param stu_info: 学生信息
        :return: True：修改成功  False：修改失败
        """
        for i in self.__stu_list:
            if i.id == stu_info.id:
                i.name = stu_info.name
                i.age = stu_info.age
                i.score = stu_info.score
                return True
        return False

    def order_by_score(self):
        """
            升序成绩显示所有
        :return: 新列表
        """
        # 为了不影响原列表．复制一份列表
        new_list = self.__stu_list[:]
        for i in range(len(new_list) - 1):
            for j in range(i + 1, len(new_list)):
                if new_list[i].score > new_list[j].score:
                    new_list[i], new_list[j] = new_list[j], new_list[i]
        return new_list