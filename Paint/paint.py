#edited:180609
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

#print(mpl.rcParams)
mpl.rcParams['axes.titlesize'] = 20
mpl.rcParams['xtick.labelsize'] = 16
mpl.rcParams['ytick.labelsize'] = 16
mpl.rcParams['axes.labelsize'] = 16
mpl.rcParams['xtick.major.size'] = 0
mpl.rcParams['ytick.major.size'] = 0

#包含了狗，猫，猎豹的最高奔跑速度，还有对应的可视化颜色
speed_map = {'dog':(48,'#7199cf'),'cat':(45,'#4fc4aa'),'cheetah':(125,'#e1a7a2')}

#整体图的标题，fig对象相当于一张画布，即下面可以添加子图
fig = plt.figure('Speed of three animal')

#在整张图上加上一个子图，121表示一个1行2列的子图中的第一张
ax = fig.add_subplot(111)
ax.set_title('Running speed - bar chart')

#生成X轴每个元素的位置
xticks = np.arange(3)

#定义每个柱的宽度(cm)
bar_width = 0.5

#动物名称（列表）
animals = speed_map.keys()

#奔跑速度
speeds = [x[0] for x in speed_map.values()]

#柱子的颜色
colors = [x[1] for x in speed_map.values()]

#画柱状图，横轴是动物标签的位置，纵轴是速度，定义柱的宽度，同时设置柱的边缘为透明
bars = ax.bar(xticks,speeds,width=bar_width,edgecolor = 'none')

#设置Y轴的标题
ax.set_ylabel = ('Speed(km/h)')

# x轴每个标签的具体位置，设置为每个柱的中央
ax.set_xticks(xticks+bar_width/2)

# 设置每个标签的名字
ax.set_xticklabels(animals)

# 设置x轴的范围
ax.set_xlim([bar_width/2-0.5,3-bar_width/2])

# 设置y轴的范围
ax.set_ylim([0,150])

# 给每个Bar分配指定的颜色
for bar,color in zip(bars,colors):
	bar.set_color(color)

##在122位置加入新的图
#ax = fig.add_subplot(122)
#ax.set_title('Running speed - pie chart')
#
##生成同时包含名称和速度的标签
#labels = ['{0}\n{1} km/h'.format(animal,speed) for animal,speed in zip(animals,speeds)]
#
##画饼状图，并制定标签和对应的颜色
#ax.pie(speeds,labels=labels,colors=colors)

#将图保存到本地
plt.savefig('Speed of three animal.png')

#打印图
plt.show()