from collections import Counter

from matplotlib import pyplot as plt
plt.rcParams["font.family"] = ["SimHei"]
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
#线形图gdp
years=[1950,1960,1970,1980,1990,2000,2010]
gdp=[300.2,543.3,1075.9,2862.5,5979.6,10289.7,14958.3]
plt.plot(years,gdp,color='green',marker='o',linestyle='solid')
plt.title("名义gdp")
plt.ylabel("十亿美元")
plt.show()
#条形图奥斯卡电影
movies=['Annie Hall','Ben-Hur','Casablanca','Gandhi','West Side Story']
numers_oscars=[5,11,3,8,10]

xs=[i+0.1 for i,_ in enumerate(movies)]
plt.bar(xs,numers_oscars)
plt.ylabel('所获奥斯卡金像奖数量')
plt.title("我最喜欢的电影")
plt.xticks([i+0.1 for i,_ in enumerate(movies)],movies)
plt.show()
#学生成绩图
grades=[83,95,91,87,70,0,85,82,100,67,73,77,0]
decile=lambda grade: grade//10*10
histogram=Counter(decile(grade) for grade in grades)
plt.bar([x for x in histogram.keys()],histogram.values(),8)
plt.axis([-5,105,0,5])
plt.xticks([10*i for i in range(11)])
plt.xlabel("十分相")
plt.ylabel("学生数")
plt.title("考试成绩分布图")
plt.show()
#线图
variance=[1,2,4,8,16,32,64,128,256]
bias_squared=[256,128,64,32,16,8,4,2,1]
total_error=[x+y for x,y in zip(variance,bias_squared)]
xs=[i for i,_ in enumerate(variance)]
plt.plot(xs,variance,'g-',label='variance')
plt.plot(xs,bias_squared,'r-',label='bias_squared')
plt.plot(xs,total_error,'b:',label='total_error')
plt.legend(loc=9)
plt.xlabel("模型复杂度")
plt.title("偏差-方差权衡图")
plt.show()
#散点图
test_1_grades=[99,90,85,97,80]
test_2_grades=[100,85,60,90,70]
plt.axis('equal')
plt.scatter(test_1_grades,test_2_grades)
plt.title("测试分数比较")
plt.xlabel("测验一的分数")
plt.ylabel("测验二的分数")
plt.show()
