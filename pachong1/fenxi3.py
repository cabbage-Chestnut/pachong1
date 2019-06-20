import inline
import matplotlib
import pandas as pd#分析数据的xsl
import numpy as np#提供了python对多维数组对象的支持
import matplotlib.pyplot as plt
# import matplotlib.inline
# #内嵌画图
data1 = pd.read_csv('./data.csv',encoding='gbk')
#data
# 2.1 分析十年间 每年票房冠军的票房走势，并找出十年票房总冠军
data=data1
df_empty = pd.DataFrame()
i=0
while i<len(data.index):
    df_empty=df_empty.append(data.loc[data.index == i],ignore_index=True)
    i=i+25
#按总票数排序
df_empty=df_empty.loc[np.argsort(df_empty.zpf,axis=1)]
print(df_empty)
