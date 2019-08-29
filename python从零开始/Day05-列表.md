#***输入输出函数***
####1.输出函数出：print()
1.默认每一个print函数，输出完内容后会输出一个换行
2.一个print函数输出多个内容的时候，内容之间是用空格隔开的
3.内容后边加end=来设置结束标志(默认是'\n')
4.通过设置sep的值，来设置多个内容之间的间隔符(默认是' ')
"""
```
print('aaa', 100, end='\n', sep=',')
print('bbb')
```
#### 2.输入函数:input()函数
"""
1.input()函数可以接收从控制台输入的内容(以回车为结束标志)
2.input函数会阻塞线程，程序执行到input的时候会停下来，等待用户的输入，输入完成后才会接着执行下面的内容
3.接收到的数据是以字符串的形式返回的 (python2.x中输入的是数字的时候，可能返回int类型或者浮点型数据)
"""
```
value = input('请输入一个整数:')
print('name',value, type(value))
```
### *练习：猜数字游戏*
"""
随机产生一个1-100的整数
输入的数字如果和产生的随机数是一样的，就提示猜对了，并且游戏结束
如果输入的数大于或者小于随机数，就提示输入的数字偏大或者偏小，然后让其重新输入
"""
```
import random
# 产生一个随机数
number = random.randint(1, 100)
count = 0
print('======欢迎进入猜数字高级游戏=====')
while True:
    value = int(input('请输入你猜的数字:'))
    count += 1
    if value == number:
        if count >= 6:
            print('智商欠费，请充值!')
        if count == 1:
            print('开挂的人生不需要解释!')

        print('恭喜你，猜对啦!')
        break

    if value > number:
        print('输入数字大了!')
    else:
        print('输入的数字小了!')
```
#2.列表
1.默认每一个print函数，输出完内容后会输出一个换行
2.一个print函数输出多个内容的时候，内容之间是用空格隔开的
3.内容后边加end=来设置结束标志(默认是'\n')
4.通过设置sep的值，来设置多个内容之间的间隔符(默认是' ')
"""
```
print('aaa', 100, end='\n', sep=',')
print('bbb')
```
#### 2.输入函数:input()函数
"""
1.input()函数可以接收从控制台输入的内容(以回车为结束标志)
2.input函数会阻塞线程，程序执行到input的时候会停下来，等待用户的输入，输入完成后才会接着执行下面的内容
3.接收到的数据是以字符串的形式返回的 (python2.x中输入的是数字的时候，可能返回int类型或者浮点型数据)
"""
```
value = input('请输入一个整数:')
print('name',value, type(value))
```
### *练习：猜数字游戏*
"""
随机产生一个1-100的整数
输入的数字如果和产生的随机数是一样的，就提示猜对了，并且游戏结束
如果输入的数大于或者小于随机数，就提示输入的数字偏大或者偏小，然后让其重新输入
"""

### 产生一个随机数
```
import random
number = random.randint(1, 100)
count = 0
print('======欢迎进入猜数字高级游戏=====')
while True:
    value = int(input('请输入你猜的数字:'))
    count += 1
    if value == number:
        if count >= 6:
            print('智商欠费，请充值!')
        if count == 1:
            print('开挂的人生不需要解释!')
        print('恭喜你，猜对啦!')
        break
    if value > number:
        print('输入数字大了!')
    else:
        print('输入的数字小了!')
```

# 3.列表
列表、字典、元祖、集合都是序列，都是容器类型的数据类型
列表(list)：用来存储多个数据的一种数据类型. 里面存储的单个数据，我们叫元素
特点:1.有序的 2.可变的(可变指定是容器中的内容的个数和值可变) 3.元素可以是任何类型的数据
列表的值:用[]将列表中的元素括起来，多个元素之间用逗号隔开。[] -> 空列表
"""
# 1.怎么声明一个列表
"""1.声明一个变量，赋一个列表值"""
```
list1 = []  # 创建一个空的列表
print(type(list1))

list2 = [1, 12.9, 'abc', True]
print(list2, type(list2))
```
"""2.将其他的数据类型转换成列表"""
```
list3 = list('abc1234')
print(list3)

list4 = list(i*2 for i in range(100))
print(list4)

list5 = list(i for i in range(100) if i % 3 == 0)
print(list5)
```
2. 获取列表元素
列表中的每一个元素都对应的一个下标：0 ~ 列表的长度-1; -1 ~ -列表长度
```
names = ['路飞', '佐罗', '娜美', '鸣人', '佐助']
```
 a.获取单个元素
"""
列表名[下标]
下标不能越界
"""
```
print(names[2])
print(names[-3])
#print(names[5])   # IndexError: list index out of range
```
# b.获取部分元素(切片)
"""
列表名[起始下标:结束下标]: 获取从起始下标开始，到结束下标前的所有的元素。结果是一个列表
列表名[起始下标:结束下标:步进] 从起始下标开始，每次下标值加步进获取下一个元素，知道结束下标前为止
起始下标和结束下标都可以缺省：
        如果步进是正数，起始下标缺省就是从第一个元素开始获取；如果步进是负数就从最后一个元素开始获取
        结束下标缺省，步进是正数，获取到最后一个元素；步进是负数，从后往前获取到第一个元素
"""
```
print(names[1:4])
print(names[-4:-1])
print(names[0:4:2])
print(names[:])  # 获取列表中的所有的元素，从新创建一个新的列表
```
# c.一个一个的获取列表的所有元素(遍历列表)
```
scores = [12, 89, 67, 56, 88, 90, 70]
```
# for循环遍历
```
for item in scores:
    print(item)
```
# while循环
```
index = 0
while index < len(scores):
    print(scores[index])
    index += 1


print('=======')
```
# 3.获取列表的长度(获取列表元素的个数)
"""
len(列表)
"""
```
print(len(scores))
```



# 4.添加列表元素
```
skills = []
print(skills)

#### 1.append函数
"""
```
列表.append(元素)
在列表的末尾添加一个元素
```

skills.append('气体源流')
print(skills)

skills.append('拘灵遣将')
print(skills)
```
#### 2.insert函数
"""
列表.insert(下标,元素)
在列表的指定的下标前插入一个元素

注意:在这儿，下标可以越界，如果越界，就会插入到列表的最前面或者最后面
"""
```
skills.insert(0, '通天箓')  # 在列表的最前面插入一个元素
print(skills)
```
#### 3. +
"""
列表1+列表2
将列表2中的元素和列表1中元素合并后创建一个新的列表
"""
```
new_skills = skills + ['风后奇门', '阿威十八式']
print(new_skills)
```

#### 练习：从控制台输入10个学生的成绩，然后保存在一个列表中
```
scores = []
for _ in range(10):
    score = float(input('>>>'))
    scores.append(score)

print(scores)
```


# 5.删除列表元素
 注意： 不管是添加元素还是删除元素，都会重新分配下标

 删除列表元素
films = ['肖生克的救赎', '阿甘正传', '摔跤吧爸爸', '逃学威龙', '赌神', '赌圣', '英雄本色', '逃学威龙']
print(films)
# 1. del 语句
"""
del可以删除任何数据

del 列表[下标] : 删除列表中指定下标的元素

注意:这儿的下标不能越界
"""
```
del films[1]
print(films)
```

# 2. remove方法
"""
列表.remove(元素): 删除列表中的指定的元素(如果同一个元素有多个，只删除最前面的那一个)

注意：如果要删除的元素不在列表中，会报错
"""
```
films.remove('逃学威龙')
print(films)
```
# 3. pop方法
"""
列表.pop(): 将列表中的最后一个元素取出来
列表.pop(下标): 将列表中指定下标的元素取出来

注意: 这儿的下标不能越界
"""
```
print(films)
film = films.pop()
print(films, film)

film = films.pop(1)
print(films, film)
```

# scores = [23, 45, 45, 78,32,90, 89,1],删除所有小于60分的成绩
scores = [23, 43, 45, 78, 32, 90, 89, 10, 9, 1]

# [23, 43, 45, 78, 32, 90, 89, 10, 9, 1]  23  1
# [43, 45, 78, 32, 90, 89, 10, 9, 1] 45 2
# [43,78, 32, 90, 89, 10, 9, 1]  32 3
# [43,78,90, 89, 10, 9, 1] 89 4
# [43,78,90, 89, 10, 9, 1] 10 5
# [43,78,90, 89, 9, 1]  1 6
# [43,78,90, 89, 9]
"""
```
new_score = score[:]
for item in new_score:

```
"""
```
for item in scores[:]:
    if item < 60:
        scores.remove(item)
        
print(scores)
```
