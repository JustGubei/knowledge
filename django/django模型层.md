模型层

	概念
		objects: 管理器，默认模型的属性
		ORM(objects relationship mapping): 对象关系映射
	创建
		create()方法: 模型名.objects.create(字段1=值,字段2=值)
		save()方法: 模型对象.save()
	删除
		delete()方法: 模型名.objects.filter(条件).delete()
	修改
		update()方法: 模型名.objects.filter(条件).update(字段1=值,字段2=值)
		save()方法: 模型对象.save()
		update()和save()的区别: 是否更新使用auto_now约束条件的字段
	查询
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