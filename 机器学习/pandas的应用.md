1. 安装及引用：

> pip install pandas
> import pandas as pd

2. 读取csv：
    
csv_pd = pd.read__csv(file_name, encoding='gbk') #此处文件包含中文字符，所以指定编码格式

csv_pd2 = pd.read___csv(log_path, header=None, usecols=[0, 1, 2, 3, 4, 5, 6, 7, 8] #不包含列名，指定要使用的列

3. 删除无列名的列：

csv_pd = csv_pd.loc[:, ~csv_pd.columns.str.contains('^Unnamed')] #文件中每行的末尾有一个多余的逗号，所以会产生一个无列名的列
4. 删除指定列：

csv_pd.drop(['a'], axis=1, inplace=True) #删除a列并实时修改
5. 获取所有列名的数组：

csv_columns = csv_pd.columns.tolist() #获取列名，转成数组
6. 设置某一列的值：

csv_pd['b'] = 1 #b列都赋值1
7. 合并两个DataFrame（匹配合并）：

csv_pd = csv_pd1.append(csv_pd2) #合并csv_pd1和csv_pd2，二者列名一致
8. 将DataFrame写入csv文件：

csv_pd.to_csv(csv_path, sep=',', header=True, index=False) #逗号分隔，写列名，不写索引
9. DataFrame的连接（简单合并）：

csv_concat = pd.concat([csv_pd1, csv_pd2], axis=0, join='inner') #使用axis=0进行纵向合并，join='inner'表示只保留两个数据组都有的列
10. 去除重复的行：

csv_unique = csv_concat.drop_duplicates(keep=False) #keep=False表示删除存在重复行的数据，只保留没有重复的行
11. 是否为空：

csv_pd.empty
13. 通过ExcelWriter写入excel：

writer = pd.ExcelWriter('a.xlsx')
csv_pd.to_excel(writer, 'Sheet1') #可以写入多个sheet后再保存
writer.save() 
14. 直接写入excel:

csv_pd.to_excel('a.xlsx', 'Sheet1')
15. 读取excel文件：

df = pd.read_excel('data.xlsx',sheet_name= 'Sheet1')
 16. 列赋值：

df_result['a'] = df_result[0].map(lambda x: x.split()[0]) #用第一列给a列赋值
17. 获取列数据：

data = df_result['a'].astype('int') #将a列转为int格式
data.values #获取数据
18. 数据透视表：

复制代码
import numpy as np
import pandas as pd

df_count = pd.pivot_table(df_result, 
　　　　　　　　　　　　　　　　index=["a"],     
                           values["b"],
                           aggfunc=[len, np.max, np.min, np.mean],
                           fill_value=0, 
                           margins=True,
                           margins_name='All'
                           )