import inline
import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import matplotlib.inline

data1 = pd.read_csv('./data.csv',encoding='gbk')
#data

# 2.2 分析十年间 不同类型的票房分冠军
data=data1
data=data.groupby('type').agg({'zpf':['max']}).reset_index()
print(data)