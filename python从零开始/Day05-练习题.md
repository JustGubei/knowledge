# ***1. 练习题***
```
1.
numbers=1  
for i in range(0,20):  
    numbers*=2  
print(numbers) 

i=0  numbers=1*2
i=1  numbers=2*2
i=2  numbers=2*2*2
...
i=19 numbers = 2*2*...*2 = 2^20


# for循环中，如果for后面的变量在循环体中不需要，这个变量命名的时候可以使用'_'命名
```
# 统计1-100中能被3或者7整除，但是不能被21整除的数的个数
"""
```
for _ in range(20):
    print('==')

"""
summation=0
num=1
while num<=100:
    if (num%3==0 or num%7==0) and num%21!=0:
        summation += 1
    num+=1
print(summation)

```

# 3.求1到100之间所有数的和、平均值
```
sum1 = 0
for x in range(1,101):
    sum1 += x
print('和:%d 平均值:%.2f' % (sum1, sum1/100))
```

# 4. 计算1-100之间能3整除的数的和
```
sum2 = 0
for x in range(1,101):
    # 判断是否能被3整除
    if x % 3 == 0:
        sum2 += x
print('能被3整除的数的和:',sum2)

num = 1
sum2 = 0
while num <= 100:
    if num % 3 == 0:
        sum2 += num
    num += 1
print('能被3整除的数的和:',sum2)
```

# 5.求斐波那契数列中的第n个数是多少？1 1 2 3 5 8 13 21...

```
n = 3
pre_1 = 1  # 当前数字的前一个数
pre_2 = 1  # 当前数的前二个数
current = 0  # 当前这个数
# x代码的是当前是第几个数
for x in range(1, n+1):
    if x == 1 or x == 2:
        current = 1
        # print(1)
        continue
    # 根据前两个数的和计算当前这个数
    current = pre_1 + pre_2
    # print(current)
    # 更新前一个和前两个的值
    pre_1, pre_2 = pre_2, current

print('第%d个数是%d' % (n, current))
```

# 6.判断101-200之间有多少个素数，并输出所有素数。
# 取出101-200之间的所有的数
```
for number in range(101, 201):
    count = 0
    # 判断取出来的number的值是否是素数
    for x in range(2, number):
        if number % x == 0:
            count += 1
            # print('%d不是素数'% number)
            # 只要在2~number-1之间有一个能够被number整除，那个这个number就确定不是素数
            break  # 循环嵌套的时候，遇到break和continue结束的是包含的最近的那个循环

    # 如果2 ~ number-1 一个能够被number整除的数都没有，number才是素数
    if count == 0:
        print('%d是素数' % number)

"""

number = 101
x=(2-100)
x=2  101%2==0
x=3  101%3==0
x=4  101%4==0
x=5
x=6
x=100 101%100==0

number=102
x=(2,101)
x=2 102%2==0  102不是素数

number=103
x=(2,102)


"""
```
# 7.打印出所有的水仙花数,所谓水仙花数是指一个三位数，其各位数字立方和等于该数本身。
# 例如：153是一个水仙花数,因为153 = 1^3 + 5^3 + 3^3

# 取出所有的三位数:100-999
```
for x in range(100,1000):
    # 个位
    ge_wei = x % 10
    # 十位
    shi_wei = x // 10 % 10
    # 百位
    bai_wei = x // 100
    if x == ge_wei**3 + shi_wei**3 + bai_wei**3:
        print('%d是水仙数' % x)
```

# 9. 有一分数序列：2/1,3/2,5/3,8/5,13/8,21/13...求出这个数列的第20个分数
```
fen_zi = 2
fen_mu = 1
for x in range(1, 21):
    if x == 1:
        # print('%d/%d' % (fen_zi, fen_mu))
        continue
    fen_zi,fen_mu = fen_zi + fen_mu, fen_zi
print('%d/%d' % (fen_zi, fen_mu))
```

# 10.给一个正整数，要求：1、求它是几位数 2.逆序打印出各位数字
```
number = 12657887
str1 = str(number)
print(len(str1))
print(str1[::-1])

```




