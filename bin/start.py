import os
import sys
import platform

# 判断操作系统
if platform.system() == 'Windows':
    BASE_DIR = "\\".join(os.path.abspath(os.path.dirname(__file__)).split("\\")[:-1])
else:
    BASE_DIR = "/".join(os.path.abspath(os.path.dirname(__file__)).split("/")[:-1])

# 把BASE_DIR添加进系统目录
sys.path.insert(0, BASE_DIR)

from core import main  # 导入主文件
from conf import settings  # 导入配置文件

if __name__ == '__main__':
    obj = main.Manage_Center()
    obj.run()

