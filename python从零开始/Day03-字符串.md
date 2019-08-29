#***1.1 认识字符串***
##### 1.1什么是字符串
```
a.使用单引号或者双引号括起来的字符串的字符集就是字符串.

b.引号中单独的符号、数字、字母等都叫字符

c.转义字符：可以用来表示一些有特殊功能或者是特殊意义的字符（通过在固定的字符前加反斜杠（\）)

\' ->'
\\ ->\
\n ->换行
\t ->制表符
转义字符在计算字符串长度的时候，代表一个字符

```
##### 1.2 阻止转义
```
# 可以通过在字符串前面加r或者R，来阻止转义字符转义
str1 = r'\\'    
print(str1)

```
##### 1.3 python中字符串中的字符是Unicode编码
```
# Unicode编码使用16位对一个字符进行编码，编码的目的是让字符可以存储到在计算机中
# Unicode码包含了ASSCII码，可以表示世界上所有的语言和符号
# a.获取一个字符的Unicode码
ord1= ord('我')
ord2= ord('很')
ord3 =ord('酷')
print(hex(ord1),hex(ord2),hex(ord3))
# b.将Unicode码转换成字符
print(chr(0X4eef))

# 字符串比较大小的时候，从字符开始一次往后比较每个字符的大小，知道遇到字符不一样为止。
# 比较字符大小的时候，实质比的是他们的编码的大小
print('abc'>'aa')
print(ord('a'))
```
#***2. 获取字符串中的字符***
##### 2.1 python的字符串，实质是一个有序的字符序列
```
# 获取字符串长度：（长度指的是字符串中字符的个数）
# len是获取序列长度的内置函数
# 转义字符长度是1
count =len('abc\n123')
print(count)
```
##### 2.2 通过下标记获取字符串中的某一个字符
```
# 字符串中每个字符都对应一个下标（索引），可以通过索引值去获取固定的字符。
# 'abc' -->a:0, b:1,c:2
str1 = 'abc'
print(str1[2])   #c

str2 = 'good good study\nday day up'
print(str2[-1])

# 下标的范围：0 ~ 字符串的长度-1 ；  -1 ~ -字符串长度
#获取字符的时候，索引值不能操作索引的范围，否则报IndexError

# index 下标，索引

#print(str1[3])   #IndexError: string index out of range 索引超出范围
```
##### 2.3 获取字符串中的部分字符(切片)
```
字符串[开始下标:结束下标] --->获取字符串中从开始下标到结束下标的字符（包含开始但不包含结束下标）
字符串[开始下标：结束下标：步进]

# a.开始下标和结束下标都有值：开始下标对应的字符，要在结束下标的字符前面

str3 = 'Hello Python'
print(str3[6:12])
print(str3[-6:12])

#b.开始下标省略：从字符串的最前面取到结束下标前
print(str3[:5]) 

# 结束下标省略：从开始位置获取到字符串结束
print(str3[6:])

# e.两个都省略:获取两个字符串的内容
print(str3[:])

#f:（了解）当步进是负数的时候，开始下标和结束下标的性质相反
print(str3[::2])
print(str3[3:1:-1])

print(str3[::-1])
```
#***3. 字符串中的运算符***
##### 3.1 字符串拼接
```
# 字符串1+字符串2
str1 = 'hello' + ' ' + 'Python'
print(str1)

# 注意：+号两边要么都是数字，要么都是字符串，不能一个数字一个字符串
```
##### 3.2 字符串重复
```
# 字符串*整数
str2 = 'abc'*3
print(str2)
```
##### 3.3 in
```
# 字符串1 in 字符串2：  判断字符串1是否在字符串2中  -->在就是True，不在就是False
result = 'aa' in 'abaaac'
print(result)
```
##### 3.4 not in
```
#字符串1 not in 字符串2：判断字符串1是否不再字符串2中 -->不在就是True，在就是False
```
##### 3.5 格式字符串
```
# 格式：'占位符1占位符2'%（值1，值2）
str1 = 'abc%s123' % ('>>>')
print(str1)

#  %s  -->字符串占位符（格式符）
#  %d  -->整数占位符（格式符）
#  %f  -->浮点占位符
#  %c  -->长度是1的字符串占位符（字符占位符）,可以给字符的值，也可以给字符的编码值
#  %.nf :使用n值限制小数点后面的小数的位数，默认六位小数
# 如果后面没有加%，那么这个字符串就只是一个普通的字符串

str3 = '金额:%.2f元' % (100)
print(str3)

# %x和%X -->十六进制数据占位符
number = 100
#XXX的十六进制是XXXXX
str4 = '%d的十六进制是0X%x' % (number,number)
print(str4)
```

##### 3.6 格式化输出
```
name = 'HCH'
age =20
# XX今年XX岁
print('%s今年%d岁' % (name,age))

str5 = '小明考了%u分' % (100)
print(str5)

str6 = '%d的八进制是0o%o' % (number,number)
print(str6)
```
#***4.字符串相关方法***
```
# 字符串相关方法的通用格式: 字符串.函数()

# 1.capitalize:将字符串的首字母转换成大写字母，并且创建一个新的字符串返回
str1 = 'abc'
new_str = str1.capitalize()
print(str1, new_str)


# 2.center(width, fillchar): 将原字符串变成指定的长度并且内容居中，剩下的部分使用指定的字符填充
new_str = str1.center(7, '!')
print(str1, new_str)


# 3.rjust(width, fillchar)： 右对齐
new_str = str1.rjust(7,'*')
print(new_str)



# 产生学号
number = 19  # py1805009
# str(数据)： 将任何其他的数据转换成字符串 
num_str = str(number)
print(num_str, type(num_str))
# 让字符串变成宽度为3，内容右对齐，剩下部分使用‘0’填充
new_str = num_str.rjust(3, '0')
print(new_str)

new_str = 'py1805'+new_str
print(new_str)

# 4.ljust(width, fillchar): 左对齐


# "123.56" '-120'

# 5.字符串1.join(字符串2): 在字符串2中的每个字符之间插入一个字符串1
new_str = '123'.join('bbb')
print(new_str)


# 6.
print(max('abcZ'))
```
#***5.if**
```
# if语句
"""
结构:
1.
if 条件语句:
	条件语句结果为True执行的代码块

执行过程:先判断条件语句是否为True,如果为True就执行if语句后:后面对应的一个缩进的所有的代码。
为False,就不执行冒号后面一个缩进中的代码块，直接执行后续的其他语句

条件语句：可以是任何有值的表达式，但是一般是布尔值

if：关键字

"""

if False:
	print('代码1')
	print('代码2')
	print('代码3')

print('代码4')


# 练习:用一个变量保存时间(50米短跑),如果时间小于8秒，打印及格
time = 7

if time < 8:
	print('及格')  # 只有条件成立的时候才会执行

print(time)  # 不管if语句的条件是否，这个语句都会执行


"""
2.
if 条件语句:
	语句块1
else:
	语句块2

执行过程:先判断条件语句是否为True,如果为True就执行语句块1，否则执行语句块2
"""
# 练习:用一个变量保存成绩,如果成绩大于等于60，打印及格，否则打印不及格
score = 40

if score >= 60:
	print('及格')
else:
	print('不及格')
```

Day03作业：

 2-3 个性化消息: 将用户的姓名存到一个变量中，并向该用户显示一条消息。显示的消息应非常简单，如“Hello Eric, would you like to learn some Python today?”。
```
name = 'Eric'
str1= 'Hello %s, would you like to learn some Python today?' % (name)
print(str1)
```
![结果.png](https://upload-images.jianshu.io/upload_images/13183695-e4ce87f5d169afeb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
2-4 调整名字的大小写: 将一个人名存储到一个变量中，再以小写、大写和首字母大写的方式显示这个人名。
```
name='Eric'
print(name.lower())
print(name.upper())
print(name.capitalize())
```
![结果.png](https://upload-images.jianshu.io/upload_images/13183695-b7681a6b8f1bf9aa.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
2-5 名言: 找一句你钦佩的名人说的名言，将这个名人的姓名和他的名言打印出来。输出应类似于下面这样(包括引号):Albert Einstein once said, “A person who never made a mistake never tried anything new.”
```
print('Albert Einstein once said, “A person who never made a mistake never tried anything new.”')
```
![结果.png](https://upload-images.jianshu.io/upload_images/13183695-e126f602fedd0dd0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
2-6 名言2: 重复练习2-5，但将名人的姓名存储在变量famous_person 中，再创建要显示的消息，并将其存储在变量message 中，然后打印这条消息。
```
famous_person = 'Albert Einstein'
message = '%s once said, “A person who never made a mistake never tried anything new.”' % (famous_person)
print(message)
```
![结果.png](https://upload-images.jianshu.io/upload_images/13183695-f338f03fd5524d15.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
2-7 剔除人名中的空白: 存储一个人名，并在其开头和末尾都包含一些空白字符。务必至少使用字符组合"\t" 和"\n" 各一次。 打印这个人名，以显示其开头和末尾的空白。然后，分别使用剔除函数lstrip() 、rstrip() 和strip() 对人名进行处理，并将结果打印出来。 
```
name = '\t\nEinstein\n'
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())
```
![结果.png](https://upload-images.jianshu.io/upload_images/13183695-3a802193be9ef794.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)





