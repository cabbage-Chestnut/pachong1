import pandas as pd
from numpy import *
import matplotlib.pyplot as plt

data1 = pd.read_csv('./data.csv',encoding='gbk')
#data
#3．分析总票房和平均票价之间的关系
data=data1
#设置识别中文
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
#设置画布大小
plt.figure(figsize=(12,6))
plt.title('总票房和平均票价的关系',fontsize=20)
plt.xlabel('平均票价')
plt.ylabel('总票房（万）')
plt.scatter(data.price,data.zpf,c='r')
plt.show()
#data