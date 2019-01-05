**查询**

	filter()方法,查询满足条件的信息: 模型名.objects.filter(条件)
	all()方法: 查询所有
	get()方法: 查询指定的条件
		只能返回唯一的一个对象结果
		条件必须成立
	first()方法: 取出结果中的第一个对象
	exclude()方法: 查询出不满足条件的信息: 模型名.objects.exclude(条件)
	order_by()方法: 升序order_by('id')  降序order_by('-id')
	values()方法: 取查询对象中的字段
	exists(): 判断结果是否存在,存在返回True,否则返回False
	count()方法: 计算结果的条数
	pk: 主键（就是id）
	运算符
		语法:  字段__contains
		contains: 包含
		startswith: 以什么开头
		endswith: 以什么结束
		in: 在某个范围之内
		gt,gte: 大于,大于等于
		lt,lte: 小于,小于等于
	聚合
		from django.db.models import Max, Avg, Min, Sum, Count
		语法: 模型名.objects.all().aggregate(Sum(字段))
	Q
		与1: Q(条件1), Q(条件2)
		与2: Q(条件1) & Q(条件2)
		或: Q(条件1) | Q(条件2)
		非: ~Q(条件1)
	F
		用于比较两个字段,可使用+,-符号
		模型名.objects.filter(wuli__gt=F('math')-10)


代码练习：

1.插入

	def add_stu(request):
	    # 实现插入数据
	    # 实现的第一种方式
	    #Student.objects.create(s_name='小明')
	    # 实现的第二种方式
	    stu = Student()
	    stu.s_name = '小美'
	    stu.s_gender = 1
	    stu.save()
	    return HttpResponse('创建学生成功')

2.删除

	def del_stu(request):
	    #删除数据
	
	    #1.获取删除对象
	    #2.实现删除方法
	    Student.objects.filter(id=3).delete()
	    return HttpResponse('删除学生成功')

3.更新
	
	def up_stu(request):
	    #更新数据
	
	    #1.获取更新的数据，filter（条件）
	
	    #2.实现更新方法，update()
	
	    #Student.objects.filter(id=2).update(s_name='妲己')
	    stu = Student.objects.filter(id=2).first()
	    stu.s_name = '妲己2'
	    stu.save()
	
	    return HttpResponse('更新学生成功')

4.查询


	def sel_stu(request):
	    # 查询学生信息
	    # 查询所有的学生信息
	    stus = Student.objects.all()
	    for stu in stus:
	        print(stu.s_name)
	
	    stu = Student.objects.filter(s_age=20).first()
	    print(stu)
	    #get()取唯一的一个对象
	    stu = Student.objects.get(id=2)
	    print(stu)
	
	    stus = Student.objects.filter(s_gender=1)
	    print(stus)
	    stus = Student.objects.exclude(s_gender=0)
	    print(stus)
	
	    #排序order_by
	    stus = Student.objects.order_by('id')
	    print(stus)
	    #降序
	    stus = Student.objects.order_by('-id')
	    print(stus)
	
	    #取出对象中的某个字段
	    stus = Student.objects.all().values('s_name','s_age')
	    print(stus)
	
	    stus = Student.objects.all().values()
	    print(stus)
	
	
	    #判断查询结果是否存在
	    a = Student.objects.filter(s_name='校长').exists()
	    b = Student.objects.filter(s_gender=1).count()
	    print(b)
	
	    #contains
	    #字段__运算符
	    c = Student.objects.filter(s_name__contains='小明')
	    print(c.values('s_name'))
	
	
	    #like "小%" “明%”
	    #startwith  endwith
	    d = Student.objects.filter(s_name__startswith='小')
	    print(d.values())
	
	    e = Student.objects.filter(s_name__endswith='明')
	    print(e.values())
	
	    #sql where id in (1,2,3,4,5,6,7,8)
	    stus = Student.objects.filter(id__in=[1,2,3,4,5,6,7,8])
	    print(stus)
	    stus = Student.objects.filter(pk__in=[1,2,3,4,5,6,7,8])
	    print(stus)
	
	
	    #gte gt lt lte 大于等于 大于 小于 小于等于
	
	    stus = Student.objects.filter(s_age__gte=18,s_age__lte=20)
	
	    print(stus)
	    stus = Student.objects.filter(s_age__gte=18).filter(s_age__lte=20)
	    print(stus)
	
	    #聚合函数 Avg  Max Min Sum Count
	    age_avg = Student.objects.all().aggregate(Avg('s_age'))
	
	    print(age_avg)
	    age_avg = Student.objects.all().aggregate(Sum('s_age'))
	    print(age_avg)
	
	
	
	    stus = Student.objects.filter(s_age__gte=18, s_age__lt=20)
	    # 查询年龄大于等于18或者小于20,  Q()
	    stus = Student.objects.filter(Q(s_age__gte=18)|Q(s_age__lt=20))#或
	    stus = Student.objects.filter(Q(s_age__gte=18)&Q(s_age__lt=20))#且
	    stus = Student.objects.filter(~Q(s_age__gte=18))#反
	
	    stus = Student.objects.all()
	    for stu in stus:
	        if(stu.physics > stu.math):
	                print(stu.s_name)
	
	    stus = Student.objects.filter(physics__gt= F('math'))
	    print(stus)
	
	
	    return HttpResponse('查询所有学生信息')