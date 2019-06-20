import pandas as pd
from numpy import *
import matplotlib.pyplot as plt

data1 = pd.read_csv('./data.csv',encoding='gbk')
#data

# 2.5 分析十年间 探究是否有一种或多种类型的电影在十年间票房震荡非常厉害
data=data1
data = data.groupby(['type','year']).zpf.sum().unstack()
data.fillna(0,inplace = True)
#设置识别中文
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
#设置画布大小
plt.figure(figsize=(12,6))
plt.title('电影类型在十年间总票房变化',fontsize=20)
plt.xlabel('年份')
plt.ylabel('总票房（万）')
plt.plot(data.T)
data.T.plot()
plt.show()
#data