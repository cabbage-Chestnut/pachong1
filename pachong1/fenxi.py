import inline
import matplotlib
import pandas as pd#分析数据的xsl
import numpy as np#提供了python对多维数组对象的支持
import matplotlib.pyplot as plt
# import matplotlib.inline
# #内嵌画图

data1 = pd.read_csv('./data.csv',encoding='gbk')
#data

# 1.1 按年统计 不同类型电影的平均票房
data=data1
data = data1.groupby(['type','year']).zpf.mean().unstack()
#没有的补0
data.fillna(0,inplace = True)
data
print(data)

