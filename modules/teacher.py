class Teacher():
    def __init__(self, teacher_name, teacher_salary):
        self.teacher_name = teacher_name
        self.teacher_salary = teacher_salary
        self.teacher_classes = []  # 老师所授班级列表，对象为实例

    def teacher_add_classes(self, classes_name, classes_obj):
        # 通过老师添加班级
        self.teacher_name[classes_name] = classes_obj
