# 1.数据库 #

安装:

	 pip install flask-sqlalchemy

创建对象:

	from flask_sqlalchemy import SQLALChemy
	db = SQLALChemy()

模型定义:

	class User(db.Model):
	# 定义自增的主键id
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	# 定义长度为10的name字段，类型为字符串，唯一且不能为空
	name = db.Column(db.String(10), unique=True, nullable=False)
	# 定义密码password字段
	password = db.Column(db.String(249), nullable=False)

	__tablename__ = 'flask_user'

配置链接:

	flask对象.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:123456@127.0.0.1:2206/flask8'
初始化: 

	db.init_app(flask对象)

模型的映射

	创建: db.create_all()
	删除: db.drop_all()



# 2.session #

思路

	第一次访问任何一个路由地址时,在客户端，将在cookie中存储一个键值对，键为session，值为唯一的uuid类型的参数
	第一次方式的同时，在服务端指定的redis中，也将存储cookie中的uuid值
	如果用户登录成功，则可以像redis中存储的uuid参数中保存信息

2.1 flask自带形式

	存储数据: 将session中存储的键值对内容存放在cookie中
	存储方式: 设置secret_key参数，越复杂越好
	使用方式: 
	
		from flask import session
		session['key'] = value

2.2 使用flask-session第三方库

安装: 

	pip install flask-session

配置存储的数据库:

	flask对象.config['SESSION_TYPE'] = 'redis'
	flask对象.config['SESSION_REDIS'] = redis.Redis(host, port, password)

初始化:

	from flask_session import Session

	第一种:
		 Session(flask对象)

	第二种:
		se = Session()
		se.init_app(flask对象)