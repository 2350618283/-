import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
'''number noe'''
df=pd.read_csv('aqi.csv')
# print(type(df))
# pd.set_option( 'display.max_rows', None)#展开dataframe所有列
plt.rcParams['font.sans-serif']=['SimHei'] # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False # 用来正常显示负号
df1=np.array(df['日期'])
for i in range(len(df1)):
    df1[i] = time.mktime(time.strptime(df1[i], '%Y/%m/%d'))
plt.figure(num='质量等级分类',figsize=(13,5),)
plt.scatter(df1,df['质量等级'],s=1,c='red')
'''numbber tow'''
import seaborn as sns
plt.figure('PM2.5浓度与AQI线性回归拟合图')
sns.regplot(data=df, x=df['PM2.5含量（ppm）'], y=df['AQI'])
plt.show()
'''numbber three'''
middle=df[['PM2.5含量（ppm）','AQI']]
regress=middle.values
#求系数a
n=len(regress)
sgm_xy=0;sgm_x=0;sgm_y=0
for i in range(len(regress)):
    sgm_xy+=regress[i,0]*regress[i,1]
    sgm_x+=regress[i,0]
    sgm_y+=regress[i,1]
    behind=sgm_x*sgm_y
molecule=n*sgm_xy-behind
sgm_sqrx=0;sum5=0
for i in range(len(regress)):
    sgm_sqrx+=regress[i,0]**2
denominator=n*sgm_sqrx-sgm_x**2
a=molecule/denominator
#求系数b
b=sgm_y/n-a*(sgm_x/n)
print('一元线性回归方程为：Y=%.4fx+%.4f'%(a,b))