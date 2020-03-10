class Classes():
    def __init__(self, classes_name, course_obj):
        self.classes_name = classes_name
        # 关联课程
        self.classes_course = course_obj
        # 学员字典信息
        self.classes_student = {}       #字典形式学生名：学生实例
