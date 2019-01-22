# 1.flask-login #

1.1 注册

	加密: generate_password_hash()
	解密: check_password_hash()

1.2 登录

安装: 

	pip install flask-login
	
初始化: 

	from flask_login import LoginManager
	lm = LoginManager()
	lm.init_app(flask对象)

登录用户: 

	login_user(登录系统用户对象)
退出用户:

	 logout_user()

登录校验:

	 login_required

在模板中可使用`{{ current_user.name }}`渲染登录系统的用户名信息
重点: 用户的模型中需继承`UserMixin`，或者自定义相关的属性与方法
必须定义回调`user_loader`，用于返回登录系统的用户对象


---


代码练习：

views.py:

	from flask_login import login_user, logout_user, login_required, LoginManager

	login_manage = LoginManager()

	blue = Blueprint('first',__name__)


	#注册
	@blue.route('/my_register/',methods=['GET','POST'])
	def my_register():
    if request.method == 'GET':
        return render_template('register.html')

    if request.method == 'POST':
        # 获取参数
        username = request.form.get('username')
        pwd = request.form.get('pwd')
        cpwd = request.form.get('cpwd')

        # 验证
        if username and pwd and cpwd:
            #用户名是否已经注册
            user = User.query.filter(User.name==username).first()
            if user:

                return render_template('register.html',
                                       error_name='用户名已存在',)
            if pwd!=cpwd:
                return render_template('register.html',
                                       error_pwd='密码和确认密码不一致')
            u = User()
            u.name = username
            u.password = generate_password_hash(pwd)


            db.session.add(u)
            db.session.commit()
            return redirect(url_for('first.my_login'))
        else:
            #传递的参数有为空的情况
            return render_template('register.html')




	#登陆
	@blue.route('/my_login/',methods=['GET','POST'])
	def my_login():
    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('pwd')
        #获取登陆的用户对象
        user = User.query.filter(User.name==username).first()
        if user:
            #校验密码是否一致
            if check_password_hash(user.password,password):
                # 使用flask-login实现登陆操作
                # 向session中存键值对，键为user_id，值为id值
                login_user(user)
                return redirect(url_for('first.my_index'))
            else:
                return render_template('login.html',
                                       error_pwd='密码错误')
    else:
        return render_template('login.html',
                               error_name='用户没有注册，请注册')

	
	#回调user_loader，用于返回登陆系统的用户对象
	@login_manage.user_loader
	def load_user(user_id):
	    #定义被login_manage装饰的回调
	    #返回的事当前登陆系统的用户对象
	    return User.query.filter(User.id==user_id).first()
	


	#退出系统
	@blue.route("/logout/")
	def logout():
	    logout_user()
	    return redirect(url_for('first.my_login'))


manage.py:
	
	from flask import Flask
	from flask_script import Manager
	import redis
	from flask_session import Session
	
	from app.models import db
	from app.views import blue, login_manage
	
	app =  Flask(__name__)
	#第二步，注册蓝图对象
	app.register_blueprint(blueprint=blue,url_prefix='/app')


	#配置flask_session库，存储数据在redis中
	app.config['SESSION_TYPE'] = 'redis'
	app.config['SESSION_REDIS'] = redis.Redis(host='127.0.0.1',port=6379)

	# 初始化配置信息
	# 第一种方式
	# Session(app)
	# 第二种方式
	se = Session()
	se.init_app(app)

	# 配置数据库
	#mysql+pymysql://root:123456@127.0.0.1:3306/flask8
	app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/flask8'
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	#初始化数据库的连接信息
	db.init_app(app)


	#初始化flask-login
	login_manage.init_app(app)
	
	#管理flask应用对象
	manage = Manager(app)

	if __name__ == '__main__':
		manage.run()



    #app.run()

    #启动命令为: python manage.py runserver -h 0.0.0.0 -p 80 -d
    # -h 表示ip地址
    # -p 表示端口
    # -d 表示debug模式

   		
