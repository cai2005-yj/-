from bs4 import BeautifulSoup
class cocacola:
    formula=['caffeine','sugar','water','soda']
    def __init__(self,logo_name):
        self.local_logo=logo_name
    def drink(self):
     print("energy!")
coke=cocacola('可口可乐')

print(coke.local_logo)

class TestA:
    attr=1
    def __init__(self):
        self.attr=42
obj_a=TestA()
print(obj_a.attr)

obj1=1
obj2='string'
obj3=[]
obj4={}
print(type(obj1),type(obj2),type(obj3),type(obj4))

soup=BeautifulSoup
