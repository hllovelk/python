import os
import sys
import shelve
from modules.school import School
from conf import settings


class Manage_Center(object):
    def __init__(self):
        pass

    def run(self):
        while True:
            print('\n欢迎进入选课系统\n'
                  '1 学生视图\n'
                  '2 教师视图\n'
                  '3 管理中心\n'
                  'q 退出选课系统\n')
            user_choice = input('\33[34;0m请输入您要登录的视图：\33[0m')
            if user_choice == '1':
                Manage_Student()
            elif user_choice == '2':
                Manage_Teacher()
            elif user_choice == '3':
                Manage_School()
            elif user_choice == 'q':
                print('\33[34;0m感谢您的访问!\33[0m')
                break
            else:
                print('\33[34;m您的输入有误，请重新输入！\33[0m')


class Manage_School():
    # 学校管理视图
    def __init__(self):
        if os.path.exists(settings.school_db_file + '.dat'):  # 文件是否存在，shelve会生成.dat文件
            self.school_db = shelve.open(settings.school_db_file)  # 打开学校数据库文件
            self.run_manage()  # 运行管理视图
            self.school_db.close()
        else:
            print('\33[31;0m系统信息：正在初始化\33[0m')
            self.initialize()
            self.run_manage()

    def initialize(self):
        # 实例化两个校区北京上海
        self.school_db = shelve.open(settings.school_db_file)
        self.school_db['北京'] = School('北京', '中国北京')
        self.school_db['上海'] = School('上海', '中国上海')

    def run_manage(self):
        # 运行学校管理视图
        while True:
            # 显示学校校区
            for key in self.school_db.keys():
                print('学校名称：%s' % key)
            choice_school = input('\33[34;0m请输入要管理的学校名称：\33[0m').strip()
            if choice_school in self.school_db:
                self.choice_school = choice_school
                self.school_obj = self.school_db[choice_school]
                while True:
                    print('\n欢迎光临%s校区\n'
                          '添加课程 add_course\n'
                          '增加班级 add_classes\n'
                          '招聘老师 add_teacher\n'
                          '查看课程 check_course\n'
                          '查看班级 check_classes\n'
                          '查询老师 check_teacher\n'
                          '退出程序 exit' % self.school_obj.school_name
                          )
                    user_func = input('\33[34;0m请输入操作命令：\33[0m').strip()
                    if hasattr(self, user_func):
                        getattr(self, user_func)()
                    # if hasattr(self.school_obj,user_func):
                    #     getattr(self.school_obj,user_func)()
            else:
                print('\33[34;0m输入有误，请重新输入！\33[0m')

    def add_course(self):
        course_name = input('\33[34;0m请输入课程的名字：\33[0m').strip()
        course_price = input('\33[34;0m请输入课程的价格：\33[0m').strip()
        course_peroid = input('\33[34;0m请输入课程的周期：\33[0m').strip()
        if course_name in self.school_obj.school_course:
            pinrt('\33[34;0m该课程已存在！33[0m')
            self.school_obj.screate_course(course_name, course_price, course_peroid)
            print('\33[34;0m数据更新完成！\33[0m')
        else:
            self.school_obj.create_course(course_name, course_price, course_peroid)
            print('\33[34;0m新课程添加完成！\33[0m')
        self.school_db.update({self.choice_school: self.school_obj})

    def add_classes(self):
        classes_name = input('\33[34;0m请输入要添加班级的名称：\33[0m').strip()
        course_name = input('\33[34;0m请输入关联的课程名\33[0m').strip()
        if classes_name not in self.school_obj.school_classes:  # 判断学校类里是否有该班级
            if course_name in self.school_obj.school_course:  # 判断关联课程是否在学校类
                course_obj = self.school_obj.school_course[course_name]
                self.school_obj.create_classes(classes_name, course_obj)
                self.school_db.update({self.choice_school: self.school_obj})
                print('\33[34;0m班级创建成功！\33[0m')
            else:
                print('\33[34;0m系统错误，输入课程不存在！\33[0m]')
        else:
            print('\33[34;0m系统错误，班级已存在！\33[0m')

    def add_teacher(self):
        teacher_name = input('\33[34;0m请输入教师的名字：\33[0m').strip()
        teacher_salary = input('\33[34;0m请输入教师的工资：\33[0m').strip()
        teacher_classes = input('\33[34;0m请输入关联的班级：\33[0m').strip()
        if teacher_classes in self.school_obj.school_classes:
            classes_obj = self.school_obj.school_classes[teacher_classes]
            if teacher_name not in self.school_obj.school_teacher:
                self.school_obj.create_teacher(teacher_name, teacher_salary, teacher_classes, classes_obj)
                # self.school_db.update({self.choice_school:self.school_obj})
                print('\33[34;0m教师创建成功！\33[0m')
            else:
                print('\33[34;0m教师已存在，更新已完成！\33[0m]')
            self.school_db.update({self.choice_school: self.school_obj})
        else:
            print('\33[34;0m系统错误，关联的班级不存在！\33[0m')

    def check_course(self):
        self.school_obj.show_course()

    def check_classes(self):
        self.school_obj.show_classes()

    def check_teacher(self):
        self.school_obj.show_teacher()

    def exit(self):
        self.school_db.close()
        print('\33[34;0m欢迎下次使用选课系统！\33[0m')


class Manage_Student():
    """学生视图"""

    def __init__(self):
        if os.path.exists(settings.school_db_file + '.dat'):
            self.school_db = shelve.open(settings.school_db_file)  # 打开学校数据库
            self.run_manage()
            self.school_db.close()
        else:
            print('\33[34;0m数据库学校不存在，先创建学校！\33[0m')
            exit()

    def run_manage(self):
        print('\n欢迎进入学员视图')
        for key in self.school_db:
            print('学校名称：', key)
        choice_school = input('\33[34;0m请选择注册学校名称：\33[0m').strip()
        if choice_school in self.school_db:
            self.choice_shcool = choice_school
            self.school_obj = self.school_db[choice_school]
            student_name = input('\33[34;0m请输入您的姓名：\33[0m').strip()
            student_age = input('\33[34;0m请输入您的年龄：\33[0m').strip()
            self.school_obj.show_classes_course()
            classes_choice = input('\33[34;0m请输入您上课的班级：\33[0m').strip()
            if classes_choice in self.school_obj.school_classes:
                self.school_obj.create_student(student_name, student_age, classes_choice)
                self.school_db.update({self.choice_shcool: self.school_obj})
                print('\33[34;0m学生创建成功！\33[0m')
            else:
                print('\33[34;0m系统错误，输入班级不存在！\33[0m')
        else:
            print('\33[34;0m系统错误，输入学校不存在！\33[0m')


class Manage_Teacher():
    """老师视图"""

    def __init__(self):
        if os.path.exists(settings.school_db_file + '.dat'):
            self.school_db = shelve.open(settings.school_db_file)  # 打开学校数据库
            self.run_manage()
            self.school_db.close()
        else:
            print('\33[34;0m数据库学校不存在，先创建学校！\33[0m')
            exit()

    def run_manage(self):
        print('\n欢迎进入教师视图')
        for key in self.school_db:
            print('学校名称：', key)
        choice_school = input('\33[34;0m请输入学校名称：\33[0m').strip()
        if choice_school in self.school_db:
            self.choice_school = choice_school
            self.school_obj = self.school_db[choice_school]
            teacher_name = input('\33[34;0m请输入登录教师姓名：\33[0m').strip()
            while True:
                if teacher_name in self.school_obj.school_teacher:
                    print('\n欢迎 %s 教师进入系统！\n'
                          '查看班级 check_classes\n'
                          '退出程序 exit' % teacher_name)
                    user_func = input('\33[34;0m请输入要操作命令：\33[0m').strip()
                    if hasattr(self, user_func):  # 感觉有问题！！！
                        getattr(self, user_func)(teacher_name)
                else:
                    print('\33[34;0m输入教师不存在！\33[0m')

    def check_classes(self, teacher_name):
        self.school_obj.show_teacher_classesinfo(teacher_name)

    def exit(self):
        self.school_db.close()
        sys.exit('欢迎下次光临选课系统！')
