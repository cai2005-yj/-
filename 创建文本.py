def create_wenben():
    name=1
    while name<=10:
        filepath='C:\\Users\\Lenovo\\Desktop\\文本\\'
        fullpath = filepath + str(name) + '.txt'
        file = open(fullpath, 'w')
        name=name+1
        file.close
        print('Done')

create_wenben()
