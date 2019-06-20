import pandas as pd
from numpy import *
import matplotlib.pyplot as plt

data1 = pd.read_csv('./data.csv',encoding='gbk')
#data

# 2.3 分析十年间 同一类型电影平均票房走势，分别找出上升、下降最厉害的两种类型
data=data1
data = data.groupby(['type','year']).zpf.mean().unstack()
data.fillna(0,inplace = True)
#设置识别中文
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
#设置画布大小
plt.figure(figsize=(12,6))
plt.title('同一类型电影平均票房走势',fontsize=20)
plt.xlabel('年份')
plt.ylabel('平均票房(万)')
plt.plot(data.T)
data.T.plot()
plt.show()