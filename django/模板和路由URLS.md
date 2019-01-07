**模板**

	解析模板文件的位置
		配置: 在settings.py文件中定义TEMPALTES的目录地址
		os.path.join(BASE_DIR, 'templates')
	后端渲染模板
		使用render()渲染模板
		传递参数给模板, render(request, 模板名, {key1:value1, key2: value2})
	前端渲染数据
		解析变量: {{ 变量 }}
			标签for中自带的变量forloop
				从1开始: {{ forloop.counter }}
				从0开始: {{ forloop.counter0 }}
				倒序1结束: {{ forloop.revcounter }}
				倒序0结束: {{ forloop.revcounter0 }}
				判断循环第一次: {{ forloop.first }}, 返回布尔值
				判断循环最后一次: {{ forloop.last }}, 返回布尔值
		解析标签: {% 标签 %} {% end标签 %}
			标签: for
				{% for i in xxx %} {% empty %}  {% endfor %}
			标签: if
				{% if name %} {% else %} {% endif %}
			标签: ifequal
				{% ifeuqal forloop.counter 值 %}  {% endifequal %}
		注解
			web形式注解: <!--  注解内容-->, 需注意不能定义错误的标签语法
			django框架中的单行注解: {# 注解内容 #}
			django框架中的多行注解: {% comment %}  {% endcomment %}
	引入静态文件
		第一种: <link rel="stylesheet" href="/static/css/style.css">
		第二种: {% load static %}    <link rel="stylesheet" href="{% static 'css/style.css' %}">
	过滤器
		语法: {{ a | 过滤器 }}
		safe: 解析变量中的样式
		upper/lower: 变量的大小写转换
		default: 默认值
		first/last: 取出变量中的首/尾元素
		length: 计算变量的长度
	继承
		父模板(挖坑)
			概念: 定义好可以被子模板动态填充内容的block块
			定义block块的名字不能重复
		子模板(填坑)
			概念: 继承于父模板，并实现填充block块的内容
			定义的block块的名字一定要存在于父模板中
			继承: {% extends '父模板' %}
			动态填充block块的内容: {% block 名称 %} {% endblock %}
			获取父模板中坑之前定义好的内容: {{ block.super }}


---

**路由URLS**

	配置路由分发
		path('app/', include('app.urls')),
		path('app/', include(('app.urls', 'app')))
	接收参数
		path
			接收整型:<int:id> 其中id参数为int类型
			接收字符串: <str: name> 其中name参数为str类型
			接收uuid类型: <uuid: uid> 其中uid参数为uuid类型的值
			接收path路径: <path: path> 其中path参数为路径
			注意: 接收参数的方法中，需要指定接收参数的变量名
		re_path
			re_path: /index/(\d+)/其中路由匹配的值为int类型
			re_path('params/(\d+)/(\d+)/(\d+)/', views.params): 注意方法中接收参数的定义顺序和路由中定义的正则表达式的顺序一致
			re_path('params/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/', views.params): 定义路由中接收参数的名字，分别为year，month，day