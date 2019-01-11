**1.cookie与session**

	cookie
		产生背景: 由于http无状态协议，导致后端无法知道当前发送请求的人是‘谁’
		用于存储一些不是很重要的内容
		存储: set_cookie(key, value, max_age,expris)
		删除: delete_cookie(key)
	session
		产生背景: 由于cookie中存储空间有限，很容易被截取，因此cookie存重要内容不安全，需要使用session进行数据存储
		向session中存数据: request.session[key]=value
		取session中存的数据: request.session['key']或request.session.get('key')
		删除cookie和session中所有信息: request.session.flush()
		删除user_id键值对: del request.session['user_id']

**2.CSRF**

	产生背景: 在访问网站时，有可能被恶意的注入代码,执行某些请求，造成损失
	防范: 在页面的form表单中添加{% csrf_token %}