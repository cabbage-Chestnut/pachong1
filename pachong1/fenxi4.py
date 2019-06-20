import inline
import matplotlib
import pandas as pd#分析数据的xsl
import numpy as np#提供了python对多维数组对象的支持
import matplotlib.pyplot as plt
# import matplotlib.inline
# #内嵌画图

data1 = pd.read_csv('./data.csv',encoding='gbk')
#data

# 2.2 分析十年间 不同类型的票房分冠军
data=data1
data=data.groupby('type').agg({'zpf':['max']}).reset_index()
print(data)
