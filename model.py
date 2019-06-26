"""
    数据模块
"""


# 数据模型类
class StudentModel:
    """
        学生模型
    """

    # 类中不需增加其他实例
    __slots__ = ("id", "name", "age", "score")

    def __init__(self, name=None, age=None, score=None, id=0):
        """
            创建学生对象
        :param id:编号(该学生对象的唯一标识)
        :param name:姓名,str类型.
        :param age:年龄,int类型
        :param score:成绩,float类型
        """
        self.name = name
        self.age = age
        self.score = score
        self.id = id

    def output_student_info(self):
        print("{}\t{}\t{}\t{}".format(self.id, self.name, self.age, self.score))
