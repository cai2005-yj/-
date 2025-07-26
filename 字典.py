code={'BIDU':'baidu','SINA':'sina'}
code['YOKU']='youku'
print(code)
code.update({'FB':'fb','TSLA':'tesla'})
print(code)
del code['FB']
print(code)
print(code['YOKU'])

