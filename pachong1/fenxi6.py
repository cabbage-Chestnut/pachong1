import pandas as pd
from numpy import *
import matplotlib.pyplot as plt

data1 = pd.read_csv('./data.csv',encoding='gbk')
#data

# 2.4 分析十年间 同一地区在前25排名中占比的变化趋势，分别找出占比上升、下降最厉害的两个地区
data=data1
#mark设置为1/25，方便后边算比例
data.mark=0.04
data = data.groupby(['area','year']).mark.sum().unstack()
data.fillna(0,inplace = True)
#设置识别中文
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
#设置画布大小
plt.figure(figsize=(12,6))
plt.title('同一地区在前25排名中占比的变化趋势',fontsize=20)
plt.xlabel('年份')
plt.ylabel('占比')
plt.plot(data.T)
data.T.plot()
plt.show()