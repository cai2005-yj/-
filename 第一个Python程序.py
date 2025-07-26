import math


def zhuanhuan(g):
    kg=g/1000
    return str(kg)+'kg'
s=zhuanhuan(8000)
print(s)
def xieban(a,b):
    c=math.sqrt(a*a+b*b)
    return 'the right third sides length is '+str(c)
s=xieban(3,4)
print(s)

def text_create(name,msg):
    desktop='C:/Users/Lenovo/Desktop/'
    fullpath=desktop+name+'.txt'
    file=open(fullpath,'w')
    file.write(msg)
    file.close
    print('Done')
text_create('hello','hello world')

def text_filter(word,censored_word='lame',changed_word='awesome'):
    return word.replace(censored_word,changed_word)
text_filter('Python is lame')

def hanshu(name,msg):
    clean_msg=text_filter(msg)
    text_create(name,clean_msg)
hanshu('Try','lame,lame,lame')

