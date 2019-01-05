
---

Mysql增删改查

代码练习

---

	-- 如果存在名为srs的数据库就删除它（慎重）
	drop database if exists srs;
	
	-- latin1 - iso-8859-1
	-- ASCII / Unicode
	-- 创建名为srs的数据库并设置默认字符集为utf8
	create database srs default charset utf8;
	
	-- 切换到srs数据库
	use srs;
	
	-- 如果存在名为tb_student的表就删除
	drop table if exists tb_student;
	
	-- 创建学生表tb_student
	create table tb_student
	(
	stuid int not null comment '学号',
	stuname varchar(10) not null comment '姓名',
	stusex bit default 1 comment '性别',
	stubirth date comment '出生日期',
	stuaddr varchar(255) comment '家庭住址',
	primary key (stuid)
	);
	
	-- Error: Duplicated Entry
	-- crash course
	-- best practice
	
	-- 修改学生表添加联系方式列
	alter table tb_student add column stutel char(11);
	
	-- 修改学生表删除联系方式列
	alter table tb_student drop column stutel;
	
	-- 向学生表插入数据
	insert into tb_student values 
	(1001, '李明', 1, '1980-11-28', '北京');
	-- 插入部分字段
	insert into tb_student (stuid, stuname) values 
	(1002, '王大锤');
	-- 插入多条记录
	insert into tb_student values 
	(1003, '白元芳', 1, '1988-5-5', null),
	(1004, '白洁', 0, null, null),
	(1005, '狄仁杰', default, '1992-3-8', '四川成都');
	
	
	-- 截断表
	-- truncate table tb_student;
	
	-- 删除学号为1002的学生
	delete from tb_student where stuid=1002;
	
	-- 删除学号在1003到1005之间的学生
	delete from tb_student where stuid>=1003 and stuid<=1005;
	delete from tb_student where stuid in (1003, 1004, 1005);
	delete from tb_student where stuid between 1003 and 1005;
	
	-- 更新学号为1002和1004的两个学生的生日
	update tb_student set stubirth='1990-1-1' 
	where stuid=1002 or stuid=1004;
	
	-- 更新学号为1002的学生的姓名、性别和家庭住址
	update tb_student set stuname='王小美', stusex=0, stuaddr='四川自贡' where stuid=1002;
	
	-- 更新家庭住址为null的学生的家庭住址
	update tb_student set stuaddr='四川绵阳' 
	where stuaddr is null; 
	
	-- 查询学生表的所有行所有列
	select * from tb_student;
	
	-- 筛选：查询女学生
	select * from tb_student where stusex=0;
	
	-- 投影：查询所有学生的姓名和生日
	select stuname, stubirth from tb_student;
	
	-- 查询女学生的姓名和生日
	select stuname, stubirth from tb_student where stusex=0;