import time

weekday=['Monday','Tuesday','wednesday','Thursday','Friday']
print(weekday[0])
fruit=['apple','pear']
fruit.insert(1,'grape')
print(fruit)
fruit[0:0]=['orange']
print(fruit)
fruit.remove('grape')
print(fruit)
fruit[0]='grapefruit'
print(fruit)
del fruit[0:2]
print(fruit)
yuansu=['H','He','Li','Be','B','C','N','O','F','Ne']
print(yuansu[0])
print(yuansu[0:3])
print(yuansu[-10:-7])
print(yuansu[-10:])
print(yuansu[:9])

numlist=[6,2,7,4,1,3,5]
print(sorted(numlist))
print(sorted(numlist,reverse=True))
numlist2=[8,9,11,13,10,12]
a=[]

for i in range(1,11):
    a.append(i)
print(a)

b=[i for i in range(1,11)]
print(b)
