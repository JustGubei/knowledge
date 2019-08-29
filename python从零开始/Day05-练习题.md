# 1. 求s=a+aa+aaa+aaaa+aa...a的值，其中a是⼀个数字。例如2+22+222+2222+22222(此时共有5个数相加)，⼏个数相加有键盘控制。
```
"""

n = int(input('请输入n的值:'))
a = int(input('请输入a的值:'))
x = 0
y = a
for i in range(n):
    x += y
    y = y*10 + a

print(x)
"""
```
# 2.打印图形1
"""
n = 4 
@ 
@@ 
@@@ 
@@@@ 
n = 5
@ 
@@ 
@@@ 
@@@@ 
@@@@@ 
"""
"""
```
print('-----------')
n = int(input('请输入n的值:'))
a = str(input('请输入你要打印的符号:'))
i = 1  #相当于行数，要打印多少行的指定符号
while i <= n:  # 1  2  3  4  5
    print(a*i)  #第一行打印一个符号a，while循环遍历，直到第n行
    i += 1


print('----------')
"""

"""


print('n=',n)
for i in range(n):
    for j in range(0,i+1):
        print(a,end="")
    print('')
"""
```
# 3. 打印图形2
"""
n = 3 
   @ 
  @@@ 
 @@@@@ 
n == 5 
   @ 
  @@@ 
 @@@@@ 
@@@@@@@ 
"""
#-----------------------方法1------------------------------
```
"""
n = int(input('请输入n的值:'))
a = str(input('请输入你要打印的符号:'))
print('n=',n)
for i in range(n):
    for space in range(n-i):
        print(' ',end='')
    for star in range(2*i-1):
        print(a,end='')
    print('\n',end='')
"""
#-----------------------方法2----------------------------
#while循环
"""
print('======用while循环打印等腰三角形=========')
n = int(input('请输入n的值:'))
a = str(input('请输入你要打印的符号:'))
i = 1 #行数
print('n=',n)
while i <=n:
    print(' '*(n-i),a*(2*i-1))
    i += 1
"""
#---------------------------------------------------------------
#for循环
"""
print('======用for循环打印等腰三角形=========')
n = int(input('请输入n的值:'))
a = str(input('请输入你要打印的符号:'))
print('n=',n)
for i in range(1,n+1):
    print(' '*(n - i),a*(2*i-1))
"""
```
#-----------------------------------------------------------------
# 4.打印图形3
"""
n = 3 
@@@ 
@@ 
@ 
"""


```
print('======用for循环打印倒三角形=========')
n = int(input('请输入n的值:'))
a = str(input('请输入你要打印的符号:'))
print('n=',n)
for i in range(n,0,-1):
    print(a*i)
```

#-----------------------------------------------------------------
# 5. 输⼊两个正整数m和n，求其最⼤公约数和最⼩公倍数。
```
print('======请输入两个正整数m，n=========')
m = int(input('请输入正整数m的值:'))
n = int(input('请输入正整数n的值:'))
def hcf(m,n):
    if m > n:
        smaller = n
    else:
        smaller = m
    for i in range(1,smaller+1):
        if m % i ==0 and n % i == 0 :
            hcf = i

    return hcf


def lcm(m, n):
    #  获取最大的数
    if m > n:
        greater = m
    else:
        greater = n

    while (True):
        if ((greater % m == 0) and (greater % n == 0)):
            lcm = greater
            break
        greater += 1

    return lcm

print('%d和%d的最大公约数是' % (m,n) , hcf(m,n))
print('%d和%d的最小公倍数是' % (m,n) , lcm(m,n))
```

# 6. ⼀个数如果恰好等于它的因⼦之和，这个数就称为 "完数 "。例如6=1＋2＋3.编程 找出1000以内的所有
# 完数
```
n = int(input('请输入正整数n的值:'))
#------------求所有因子-----------
def allFactor(n):
    list1 = []
    i = 1
    while i < n:
        if n%i == 0:
            list1.append(i)
        i += 1
    return list1
print(allFactor(n))  #输出所有因子
```

#-------求1-1000所有完数-----------
```
for i in range(1,1000):
    s=0
    for k in range(1,i):
        if i%k==0:
            s=s+k
    if i==s:
        print(i)
```

#6.输出99乘法表
```
for i in range(1,10):
    for j in range(1,i+1):
        print('%d*%d=%2d' %(i,j,i*j),end=' ')
    for k in range(i, 10):
        print(end="       ")
    print('')
```

#1. ⼀个5位数，判断它是不是回⽂数。即12321是回⽂数，个位与万位相同，⼗位与千位相同。

下标实现
```
s = input('请输入一个字符串：')
a = len(s) #输入的字符串的长度
i = 0      #下标从0开始
count = 1
while i <= (a/2):    #判断是否是回文
    if s[i] == s[a-i-1]:
        count = 1
        i += 1
    else:
        count = 0
        break

if count == 1:
    print('您所输入的字符串是回文')
else:
    print('您所输入的字符串不是回文')
```

#打印菱形
```
print('======用for循环打印菱形=========')
n = int(input('请输入n的值:'))
a = str(input('请输入你要打印的符号:'))
print('n=',n)
for i in range(1,n+1):
    print(' '*(n - i),a*(2*i-1))
for i in range(1,n+1):
    print(' '*(i),a*(2*(n-i-1)+1))  # - -。。。为啥是2*（n-i-1）+1呢

```


# 3. 输⼊⼀⾏字符，分别统计出其中英⽂字⺟、空格、数字和其它字符的个数
```
s = input('请输入一个字符串：')
str_num = 0
spac_num = 0
figue_num = 0

for strs in s:
    if strs.isalpha():
        str_num += 1
    elif strs.isdigit():
        figue_num += 1
    elif strs == ' ':
        spac_num += 1
    else:
        pass
print('英文字母有：%d' % str_num)
print('数字有：%d' % figue_num)
print('空格有：%d' % spac_num)
```
   


