import inline
import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import matplotlib.inline

data1 = pd.read_csv('./data.csv',encoding='gbk')
#data

# 1.2 按年统计 不同国家及地区电影在前25排名中的占比
data=data1
data.mark = data.mark/25
data = data.groupby(['area','year']).mark.sum().unstack()
data.fillna(0,inplace = True)
print(data)