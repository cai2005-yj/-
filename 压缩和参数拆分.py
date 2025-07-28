def add(a,b):
    return a+b
a=add(1,2)
c=add(*[1,2])
print(a)
print(c)


def magic(x,y,z):
    return x+y+z
x_y_list=[1,2]
z_dict={"z":3}
print(magic(*x_y_list,**z_dict))

