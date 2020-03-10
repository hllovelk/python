import os
import sys
import platform

if platform.system()=='Windows':
    BASE_DIR='\\'.join(os.path.abspath(os.path.dirname(__file__)).split('\\')[:-1])
    print(BASE_DIR)
    database_path=os.path.join(BASE_DIR,"database")         #数据库目录
else:
    BASE_DIR='/'.join(os.path.abspath(os.path.dirname(__file__)).split('/')[:-1])
    database_path=os.path.join(BASE_DIR,"database")

school_db_file=os.path.join(BASE_DIR,'school')          #学校目录
