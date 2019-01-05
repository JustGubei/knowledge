
1.模型设计

	迁移表名的定义

		指定db_table参数，表示模型迁移时，映射到数据库中的表名称
		如果没指定db_table参数,则数据库中模型映射的表名为: 应用名app_模型名称的小写

	字段类型

		CharField: 字符串类型
		IntegerField: 整型
		ImageField: 字符串类型,用于存图片
		BooleanField: 布尔， True 或者 False
		DateTimeField: 日期, 年月日时分秒
		DateField: 年月日
		TextField: 存储长文本内容, areatext标签
		FloatField: 浮点类型
		DecimalField: 浮点类型，限制最大长度和小数点后的长度

	约束

		unique: 是否唯一
		default: 默认值
		null: 是否可以为空
		primary_key: 主键
		auto_now_add: 创建时，默认赋值为当前时间
		auto_now: 创建或修改时，默认赋值为当前时间
		max_length: 最大长度
		related_name: 反向查询名称
		on_delete: 删除的约束条件
			models.CASCADE 删除主表，从表也会被删
			models.PROTECT 不让删除主表
			models.SET_NULL 删除主表，从表的关联字段设置为空

	一对一，1:1

		存储
			关联字段存储1： stu_info.关联字段 = 关联对象
			关联字段存储2: stu_info.关联字段_id = 主键id值
		查询
			学生模型和学生拓展模型的定义，一对一
			查询1,没设置related_name参数时
				学生对象查询拓展表对象:  学生对象.拓展模型名称的小写
				拓展表对象查询学生对象: 拓展表对象.OneToOneField定义的字段
			查询2, 设置related_name参数时
				学生对象查询拓展表对象: 对象对象.related_name参数
				拓展表对象查询学生对象: 拓展表对象.OneToOneField定义的字段
		定义模型
			OneToOneField: 定义在关联模型的任何一方都可以

	一对多，1:N
		存储
			关联字段的存储1: stu.关系字段 = 关联模型对象
			关联字段的存储2: stu.关系字段_id = 关联表的主键id值
		查询
			查询1: 没有定义related_name参数
				学生查询班级: 多的一方(学生)对象.关联字段
				班级查询学生: 一的一方（班级）.关联模型名的小写_set.filter().all()
			查询2: 设置了related_name参数
				学生查询班级: 多的一方（学生）对象.关联字段
				班级查询学生: 一的一方(班级).related_name参数.filter().all()
		定义模型
			ForeignKey: 定义在多(N)的一方

	多对多, N:M

		存储: 同一对多
		查询
			查询1: 没有设置related_name参数
				课程查询学生: 课程对象.关联字段.filter()
				学生查询课程: 学生对象.关联模型名的小写_set
			查询2: 设置了related_name参数
				课程查询学生: 课程对象.关联字段.filter().all()
				学生查询课程: 学生对象.related_name参数.filter().all()
		定义模型
			ManyToManyField: 定义在模型的任何一方都可以

模板

	解析模板文件的位置
		配置: 在settings.py文件中定义TEMPALTES的目录地址
		os.path.join(BASE_DIR, 'templates')
	后端渲染模板
		使用render()渲染模板
		传递参数给模板, render(request, 模板名, {key1:value1, key2: value2})
	前端渲染数据
		解析变量: {{ 变量 }}
		解析标签: {% 标签 %} {% end标签 %}
			标签: for


代码练习：

1.models模块

    from django.db import models
    
    class Grade(models.Model):
    	g_name = models.CharField(max_length=10,unique=True)
    
    	class Meta:
    		db_table = 'Grade'
    
    class Student(models.Model):
	    s_name = models.CharField(max_length=10,unique=True)
	    s_age = models.IntegerField(default=20)
	    s_gender = models.BooleanField(default=0)
	    #auto_now_add:创建时，默认字段赋值为最新的时间
	    create_time = models.DateTimeField(auto_now_add=True)
	    #auto_now:修改数据时，自动赋值为更新字段时的时间
	    update_time = models.DateTimeField(auto_now=True)
	    
	    math = models.DecimalField(max_digits=3,decimal_places=1,null = True)
	    
	    physics = models.DecimalField(max_digits=3,decimal_places=1,null=True)
	    #一对多的外键定义
	    g = models.ForeignKey(Grade,null=True,on_delete=models.CASCADE,)
    
    
	    class Meta:
	    db_table = 'student'
    
    class StudentInfo(models.Model):
	    s_no = models.CharField(max_length=10,null=False)
	    phone = models.CharField(max_length=11,null=True)
	    name = models.CharField(max_length=10,null=True)
	    #定义一对一的关联关系
	    #models.CASCADE 删除主表，从表也会被删
	    stu = models.OneToOneField(Student,on_delete=models.CASCADE)
	    #models.PROTECT 保护模式 删除主表时 从表不会被删除
	    #models.CASCCADE 删除主表，从表也会被删
	    #models.SET_NULL
	    #related_name = 'info'
    
    
    class Course(models.Model):
	    c_name = models.CharField(max_length=10,unique=True)
	    #ManyToManyField 定义在任何一个模型都可以
	    stu = models.ManyToManyField(Student,null=True)
	    
	    
	    
	    class Meta:
	    db_table = 'course'
    

2.views模块

 
    from django.shortcuts import render
    from django.http import HttpResponse
    # Create your views here.
    
    from app.models import Student, StudentInfo, Grade, Course
    
    
    def add_stu_info(request):
	    #添加小明的紧急联系人的信息，学号
	    stu_info = StudentInfo()
	    stu_info.s_no = '123456'
	    stu_info.phone = '2134567654'
	    stu_info.name = '大明'
	    # stu_info.stu = Student.objects.get(id=1)
	    stu_info.stu_id = 1
	    stu_info.save()
	    
	    return HttpResponse('创建拓展信息成功')
    
    
    def sel_info_by_stu(request):
	    #1.查询学生对象
	    #2.通过学生对象查询拓展表信息
	    
	    stu = Student.objects.filter(s_name='小明').first()
	    # stu_info = StudentInfo.objects.filter(stu=stu).first()
	    stu_info = StudentInfo.objects.filter(stu_id=stu.id).first()
	    phone = stu_info.phone
	    print(phone)
	    
	    return HttpResponse('查询成功')
    
    
    def sel_info_by_stu2(request):
	    #1.查询学生对象
	    stu = Student.objects.filter(s_name='小明').first()
	    stu_info =  stu.studentinfo
	    phone = stu_info.phone
	    print(phone)
	    
	    return HttpResponse('查询成功2')
	    
    
    def sel_stu_by_info(request):
	    #查询拓展表信息
	    stu_info = StudentInfo.objects.filter(s_no='123456').first()
	    #查询学生对象
	    stu = stu_info.stu
	    
	    print(stu)
	    
	    return HttpResponse('查询成功')
    
    def on_delete_stu(request):
	    #删除小明的学生信息
	    #效果：删除主表时，从表是否被删除
	    
	    Student.objects.filter(s_name='小明').delete()
	    return HttpResponse('删除成功')
	    
	    
	    
    def add_grade(request):
	    
    
	    g_name = ['python1802','python1804','java1806']
	    
	    for name in g_name:
	    grade = Grade()
	    grade.g_name = name
	    grade.save()
	    
	    
	    
	    return HttpResponse('添加班级成功')
    
    
    def stu_grade(request):
    
	    # stu = Student.objects.filter(id=4).first()
	    stu = Student.objects.get(id=4)
	    
	    # stu.g = Grade.objects.get(pk=1)
	    stu.g_id = 11
	    
	    stu.save()
	    
	    return HttpResponse('分配学生班级成功')
    
    
    
    def sel_grade_by_stu(request):
    
	    stu = Student.objects.filter(s_name='小美').first()
	    
	    
	    #1.grade是学生的班级对象
	    grade =stu.g
	    print(grade.g_name)
	    
	    
	    
	    return HttpResponse('查询成功')
    
    
    def sel_stu_by_grade(request):
    
	    grade = Grade.objects.get(g_name='java1806')
	    
	    stus = grade.student_set.all()
	    
	    print(stus)
	    
	    return HttpResponse('查询学生成功')
    
    
    
    def add_course(request):
	    c_name = ['大学英语','商务英语','线代','高数']
	    
	    for name in c_name:
	    c = Course()
	    c.c_name = name
	    c.save()
	    
	    return HttpResponse('添加课程信息成功')
	    
    
    def add_s_c(request):
	    #将大学英语分配给李明这个学生
	    #1.查询课程对象
	    cou = Course.objects.filter(c_name='大学英语').first()
	    #2.查询学生对象
	    stu = Student.objects.filter(s_name='李明').first()
	    #添加中间表信息
	    #stu.course_set.add(cou)
	    #cou.stu.add(stu)
	    #删除中间表信息
	    stu.course_set.remove(cou)
	    
	    
	    return HttpResponse('添加中间表信息成功')
	    
    
    def index(request):
	    stus = Student.objects.all()
	    return render(request,'index.html',{'a':stus})

index.html:

	<!DOCTYPE html>
	<html lang="en">
	<head>
	<meta charset="UTF-8">
	<title>Title</title>
	</head>
	<body>
		<p>学无止境</p>
		{{ a }}||||
		<br>
		{% for stu in a %}
		<p>姓名:{{ stu.s_name }} 年龄：{{ stu.s_age }} 班级:{{ stu.g.g_name }}
		选课：
		{% for c in stu.course_set.all  %}
		{{ c.c_name }}
		{% endfor %}
		
		</p>
		{% endfor %}
	
	</body>
	</html>
	






