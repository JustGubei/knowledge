import os

# 获取当前工作路径
os.getcwd()

# 检验给出的路径是否是一个文件
os.path.isfile(path='')

# 检验给出的路径是否是一个目录
os.path.isdir(path='')

# 判断路径是否存在
os.path.exists(path='')

# 创建多级目录
os.makedirs(r"c:\python\test")

# 创建单个目录
os.mkdir('test')
