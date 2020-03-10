from modules.classes import Classes
from modules.teacher import Teacher
from modules.course import Course
from modules.student import Student


class School():
    # 名称，地址
    def __init__(self, school_name, school_addr):
        self.school_name = school_name
        self.school_addr = school_addr
        self.school_course = {}
        self.school_classes = {}
        self.school_teacher = {}
        # self.school_student={}

    def create_course(self,course_name,course_price,course_period):
        course_obj=Course(course_name,course_price,course_period)
        self.school_course[course_name]=course_obj

    def show_course(self):
        for key in self.school_course:
            course_obj=self.school_course[key]
            print("\33[32;1m课程：%s\t价格：%s\t周期：%s月\33[0m"%(course_obj.course_name,course_obj.course_price,
                                         course_obj.course_period,))

    def create_classes(self,classes_name,course_obj):
        classes_obj=Classes(classes_name,course_obj)
        self.school_classes[classes_name]=classes_obj

    def show_classes(self):
        for key in self.school_classes:
            classes_obj=self.school_classes[key]
            print("\33[32;1m班级：%s\t关联课程：%s\33[0m" % (classes_obj.classes_name, class_obj.classes_courese.course_name))

    def show_classes_course(self):
        for key in self.school_classes:
            classes_obj=self.school_classes[key]
            course_obj=classes_obj.classes_course
            print("\33[32;1m班级：%s\t关联课程：%s\t价格：%s\t周期：%s月\33[0m" % (classes_obj.classes_name, course_obj.course_name,
                                                                    course_obj.course_price, course_obj.course_period))

    def create_teacher(self,teacher_name,teacher_salary,classes_name,classes_obj):
        teacher_obj=Teacher(teacher_name,teacher_salary)
        teacher_obj.teacher_add_classes(classes_name,classes_obj)
        self.school_teacher[teacher_name]=teacher_obj

    def update_teacher(self,teacher_name,classes_name,classes_obj):
        teacher_obj=self.school_teacher[teacher_name]
        teacher_obj.teacher_add_classes(classes_name,classes_obj)

    def show_teacher(self):
        for key in self.school_teacher:
            teacher_obj=self.school_teacher[key]
            classes_list=[]
            for i in teacher_obj.teacher_classes:
                classes_list.append(i)
            print("\33[32;1m讲师：%s\t薪资：%s\t关联班级：%s\33[0m" % (teacher_obj.teacher_name, teacher_obj.teacher_salary,
                                                            classes_list))

    def create_student(self,student_name,student_age,classes_choice):
        student_obj=Student(student_name,student_age)
        classes_obj=self.school_classes[classes_choice]
        classes_obj.classes_student[student_name]=student_obj
        self.school_classes=classes_obj

    def show_teacher_classesinfo(self,teacher_name):
        teacher_obj=self.school_teacher[teacher_name]
        for i in teacher_obj.teacher_classes:
            classes_obj=self.school_classes[i]
            student_list=[]
            for k in classes_obj.classes_student:
                student_list.append(k)
            print("\33[32;1m班级：%s\t关联课程：%s\t学员:%s\33[0m" % (classes_obj.classes_name, classes_obj.classes_courese.course_name,
                                                            student_list))


