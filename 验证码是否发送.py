CN_mobile = [134,135,136,137,138,139,150,151,152,157,158,159,182,183,184,
187,188,147,178,1705]
CN_union = [130,131,132,155,156,185,186,145,176,1709]
CN_telecom = [133,153,180,181,189,177,1700]

while True:
    haoma = input("请输入电话号码：")
    if len(haoma) != 11:
        print("电话号码需要11位")
        continue
    else:
        if int(haoma[0:3]) in CN_mobile or int(haoma[0:4]) in CN_mobile:
            print("这是一个移动号码")
            print("将发送验证码到" + haoma)
            break
        elif int(haoma[0:3]) in CN_union or int(haoma[0:4]) in CN_union:
            print("这是一个联通号码")
            print("将发送验证码到" + haoma)
            break
        elif int(haoma[0:3]) in CN_telecom or int(haoma[0:4]) in CN_telecom:
            print("这是一个电信号码")
            print("将发送验证码到" + haoma)
            break