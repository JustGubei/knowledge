**1.虚拟环境**

	安装: pip install virtualenv
	使用: virtualenv --no-site-packages -p D:\python3\python.exe name
		--no-site-packages: 表示创建的虚拟环境为纯净的环境，不安装有其他的库
		-p: 表示虚拟环境中的python版本
	pip使用
		pip list: 插看安装的库
		pip install xxx: 安装
	激活虚拟环境
		Windows: 直接执行activate命令
		Mac/Linux/Ubuntu: 直接执行source activate命令
	退出虚拟环境
		Windows/Mac/Linux/Ubuntu: 直接执行deactivate

**2.Django模式**

	M
		模型层: 定义模型和数据库中的表之间的关联关系
	V
		视图层: 定义业务逻辑
	T
		模板: HTML页面

**3.Django项目**

	创建: django-amdin startproject 项目名称
	启动
		启动命令: python manage.py runserver。默认IP为127.0.0.1  默认端口为8000
		修改启动端口: python manage.py runserver 端口
		修改IP和端口: python manage.py runserver IP:端口
		IP参数: 如果为0.0.0.0表示任何人都可以通过公网IP访问django项目
		端口PORT参数: 如果端口设置为80，表示该端口可以不用写


**4.数据库准备工作**

	settings.py中配置
		USER参数: 访问用户
		PASSWORD参数: 密码
		HOST参数: 访问数据库的地址
		PORT参数: 访问数据库的端口
		NAME参数: 数据库名
		'OPTIONS':{'isolation_level':None}
	安装pymysql
		使用pymysql连接数据库: 因为python3没有MySQLdb驱动，无法直接连接MySQL
		在工程目录的__init__.py文件中定义  pymysql.install_as_MySQLdb()
	迁移
		第一次迁移: python manege.py migrate
		除开第一次迁移
			生成迁移文件: python manage.py makemigrations
			执行迁移文件: python manage.py migrate
	插入管理员账号
		python manage.py createsuperuser