#***1. if语句***
```
1.if 条件语句：
	代码块

其他语句
执行过程:先判断条件语句是否为True，如果是就执行代码块1，执行完代码块再执行其他语句。
		 如果是Flase，直接执行其他语句

# 2.if--else
if 条件语句：
	代码块1
else：
	代码块2

其他语句

3.if-elif-elif-...-else
if 条件语句1：
	代码块1
elif 条件语句2：
	代码块2
elif 条件语句3：
	代码块3
else：
	代码块4

其他语句

4.if语句可以嵌套使用
if 条件语句1：
	if 条件语句2：
		执行语句块2
	else:
		执行语句块3
else：
	执行语句块4


#5. 判断数据的类型
# isinstance(值，类型名) -->判断指定的值是否是指定的类型
#，如果是返回True，否则返回False

print(isinstance(10,int))
print(isinstance(10,float))  #判断10是否是int类型

if isinstance(num,int):
	if num % 2:
		print('奇数')
	else:
		print('偶数')
		if not (num%4):
			print('是4的倍数')
print('======')

```
![判断一个数是偶数还是奇数](https://upload-images.jianshu.io/upload_images/13183695-1396c2a5b7336bb7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

#***2. 数据类型的转换***
##### 2.1 其他的数据类型转换成整型:int()
```
浮点型:只保留整数部分
布尔类型：True --> 1 False --> 0
字符串:去掉引号以后本身还是一个整数，就可以转换成整型数据
"""
print(int(12.4))
print(int(True))
print(int(''))
```
##### 2.2 其他的数据类型转换成浮点型：float()
```
"""
整型：在正式后面加一个'.0'
布尔类型：True ->1.0 False ->0.0
字符串：去掉字符串的引号后，剩下的部分本身就是一个整型或者浮点型数据的字符串才能转换成浮点型

"""
print(float(123))
print(float(False))
print(float('100.23'))
```
##### 2.3 其他类型的数据转换成布尔类型：bool()
```
"""
不管什么类型的数据都可以转换成布尔值
整数中除了0会转换成False，其他的都会转换成True
总结：所有为0为空的值都会转换成False，其他的值都是True
"""
print(bool(0))
print(bool(0.0))
print(bool(''))   #-->转换成False



print(bool('123'))

```
##### 2.4 其他类型的数据转换成字符串：str()
```
"""
不管什么类型的数都可以转换成字符串
其他数据类型转换成字符串的时候，就是直接在数据的外层加引号
"""
```
![判断一个字符串是否是空串](https://upload-images.jianshu.io/upload_images/13183695-09325ad32914569b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![判断一个数是否是0](https://upload-images.jianshu.io/upload_images/13183695-9d4858e2656a1553.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
#***3. 循环***
pthon中的循环有  for循环和while循环
#####3.1  for循环：
```
"""
for 变量名 in 序列：
	循环体

for:关键字
变量名：和声明变量时的变量名要求一样，功能是存储值
in：关键字，在。。。里的意思
序列：容器类型的数据，字符串、列表、字典、元组、集合等
循环体:需要重复执行的代码块

执行过程：使用变量去序列中取数据，一个一个的取，
取完为止，每取一个值，执行一次循环体

"""

for char in 'abcd123':
	print(char)

输出结果
a
b
c
d
1
2
3
[Finished in 1.0s]

# 打印20次'abc'
"""
xrange是python2.x中的函数，在pyhton3.x使用range函数代替了

range功能产生指定范围的数字序列。一般用在for循环中，控制循环次数，
或者产生索引值

range（n）:产生0~n-1的整数序列
range(m,n)产生m~n-1的整数序列
range(m,n,step):产生m-n-1，每次加step产生下一个数字，直到n前面一个为止。

"""

#range(10):产生数字0,1,2,3,4,5,6,7,8,9 
for x in range(10):
	print(x)

print('-------')
#range(1-10):产生数字1,2,3,4,5,6,7,8,9
for x in range(1,10):
	print(x)

print('-------')
#range(1-10):产生数字1,3,5,7,9
for x in range(1,10,2):
	print(x)

结果：
1
2
3
0
1
2
3
4
5
6
7
8
9
-------
1
2
3
4
5
6
7
8
9
-------
1
3
5
7
9
[Finished in 0.2s]

#练习：计算1-100累加和
sum1 = 0
for x in range(1,101):
	sum1 += x
print(sum1)
```

#####3.2 while循环：
```
while 条件语句
	循环体
其他语句


while:关键字
条件语句:结果是True，或者False
循环体：重复执行的代码段

执行过程:判断条件语句是否为True，如果为True就执行循环体。
		执行完循环体，再判断条件语句是否为True，如果为True就在执行循环体。。。
		知道条件语句的值为False，循环结束，直接执行while循环后面的语句
注意：如果条件语句的结果一直都是True，就会造成死循环。所以在循环体要有让循环可以结束的操作


python中没有do-while循环

# while True:
# 	print('aaa')
# 	flag = False

#使用while循环计算1+2+3+..+100
num = 1 #保存数字1-100
sum = 0	#保存和
while num <= 100:
	print(num)
	sum += num
	num += 1
	
print(sum)

#联系 ：2+4+5+..+100
num1 = 2 #保存数字2-100
sum1 = 0 #保存和
while num1 <= 100:
	print(num1)
	sum1 +=num1
	num1 +=2
print(sum1)
```
#***4.continue和break***
```
"""
break和continue两个字，都是作用域循环当中，用来结束循环的。

cotinue：关键字，在循环体中遇到continue，就结束当次循环，直接进入下次循环的判断
（如果是fo循环就让变量去取下一个值，如果是while循环就去判断while后面的条件语句是否为True）


"""

for x in range(10):
	print(x)
	continue  #不执行continue后面的语句，直接让x取下一个值
	print('===')


# 一般情况下这样用
for x in range(10):
	if x % 2:
		continue
	print(x)

"""
break：关键字，在循环体中遇到break，就直接结束整个循环。直接执行循环后面的其他语句
"""

for x in range(10):
	print(x)
	break
	print('=====')
print('1111')

# 练习：找出100-1000以内第一个能被3整除同时能被17整除的数
x = 100
for x in range(100,1001):
	if x % 3 ==0 and x % 17 == 0:
		print(x)
		break

```
#***4.for和while的选择***
```
"""
for循环的循环次数是确定的，while循环的次数可以不确定

1.循环次数不确定的时候，选择while循环。确定一般使用for循环
2.通过循环遍历一个序列中的值，使用for循环
"""

#input()
"""
input():接受从控制台输入数据的数据（输入的数据以回车结束）
程序中遇到input()函数，程序会阻塞，等待用户输入完成后，才会接着执行后面的代码
"""
#使用value去保存从控制台输入的数据
# value =input()

# print('=====')

#3.产生随机数
#python中有一个内置模块，可以产生随机数：random
"""
randint(m,n):产生一个0~n的随机数（整数）
"""
#导入随机数模块
import random

number = random.randint(1,100)
print(number)
```
Day04 作业：
读程序，总结程序的功能
1.
```
.numbers=1 
for i in range(0,20): 
 numbers*=2 
print(numbers)
``` 
计算2的20次方
2.
```
summation=0
num=1
while num<=100:
 if (num%3==0 or num%7==0) and num%21!=0:
 summation += 1
 num+=1
print(summation)
```
打印1-100中所有能被3或7整除并且能被21整除的数


1.求1到100之间所有数的和平均值
```
for：

num = 0
sum = 0
for num in range(1,101):
	sum += num
	num += 1
print(sum)
print(sum/100)

While：
num = 1
sum = 0
while num<=100:
	sum += num
	num +=1
print(sum)
print(sum/100)
```
2.输出1-100之间能被3整除或者能被7整除的  并且不能被21整除的数字
```
sum = 0
for x in range(1,101):
	if x%3 ==0:
		sum += x
print(sum)

While：
sum = 0
num = 1
while 1 <= num <=100:
	if  num % 3 == 0:
		sum += num
	num += 1	
	
print(sum)

```
3.计算1-100之间不能被7整除的数的和
```
num = 1
sum1 = 0
for num in range(1,101):
	if num % 7 != 0:
		sum1 +=num
print(sum1)


While：
sum = 0
num = 1
while num<100:
	if num % 7 != 0:
		sum +=num
	num +=1
print(sum)
```
