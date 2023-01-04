import numpy as np
import matplotlib.pyplot as plt

'''Paragraph one'''
ac=np.load('student_grade.npz',allow_pickle=True)
print('npz文件保存的文件包括：', ac.files)
print(type(ac['arr_0']),type(ac['arr_1']))
df = np.concatenate((ac['arr_0'], ac['arr_1']), axis=0)
# print(type(df))
excellent_stu=list()
good_stu=list()
pass_stu=list()
fail_stu=list()
for gread in range(1,len(df)):
    if df[gread,8]>=250:
        excellent_stu.append(df[gread,8])
    elif 200<=df[gread,8]<250:
        good_stu.append(df[gread,8])
    elif 150<=df[gread,8]<200:
        pass_stu.append(df[gread,8])
    else:
        fail_stu.append(df[gread,8])
lable=['优秀','良好','及格','不及格']
Pie=[len(excellent_stu),len(good_stu),len(pass_stu),len(fail_stu)]
# print(type(excellent_stu))
greadz=excellent_stu+good_stu+pass_stu+fail_stu
plt.figure('学生成绩分布')
plt.pie(Pie,labels=lable,autopct='%1.1f%%')
#改变全局字体
plt.rcParams['font.sans-serif']=['SimHei'] # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False # 用来正常显示负号
plt.title('学生成绩分布')

'''Paragraph tow'''
Math=list()
Read=list()
Write=list()
def makearray_box(ary,name,number):
    for i in range(1,len(df)):
        ary.append(df[i,number])
    a1=np.quantile(ary,0.75)
    a2=np.quantile(ary,0.25)
    up=a1+1.5*(a1-a2)
    down=a2-1.5*(a1-a2)
    x= np.sort(ary) # 排序
    shangjie=x[x<up][-1] # 除了异常值外的最大值
    xiajie=x[x>down][0] # 除了异常值外的最小值
    plt.figure(name)
    plt.grid(True)  #显示网格
    y=plt.boxplot(x,
                  notch=True,
                  meanline=True,
                  widths=9, # 指定箱线图的宽度
                  patch_artist=True, # 是否填充箱体的颜色，默认为False
                  sym="r+", # 异常点形状，默认为蓝色的“+”
                  showmeans=True, # 是否显示均值，默认不显示
                  flierprops={"marker":"o","markerfacecolor":"red","markersize":15})
                  # 设置异常点大小、样式、颜色
makearray_box(Math,'数学成绩箱型图',5)
makearray_box(Read,'阅读成绩箱型图',6)
makearray_box(Write,'写作成绩箱型图',7)

'''Paragraph three'''
xng_yes_gread=list()
xng_no_gread=list()
Completion_yes_gread=list()
Completion_no_gread=list()
for i in range(len(df)):
    if str(df[i,3])=='标准':
        xng_yes_gread.append(df[i,8])
    else:
        xng_no_gread.append(df[i, 8])
    if str(df[i,4])=='完成':
        Completion_yes_gread.append(df[i, 8])
    else:
        Completion_no_gread.append(df[i, 8])
# print(len(Completion_yes_gread))
def average(ary):
    sum=0
    for i in range(1,len(ary)):
        sum+=ary[i]
        aver=sum/len(ary)
    return aver
x_data=['效能感yes','效能感no','课程准备完成','课程准备未完成']
y_data=[average(xng_yes_gread),average(xng_no_gread),average(Completion_yes_gread),average(Completion_no_gread)]
plt.figure('特征关系')
plt.bar(x_data,y_data)
plt.show()