password_list=['#$%^&','12345']
def account_login():
    tries=3
    while tries>0:
        password=input('password:')
        passworddui=password==password_list[-1]
        passwordchongzhi=password==password_list[0]

        if passworddui:
            print('登录成功')

        elif passwordchongzhi:
           new_password=input('请输入新密码：')
           password_list.append(new_password)
           print('修改成功')
           account_login()
        else:
            print("无效密码")
            tries=tries-1
            print(tries,'times left')
    else:
        print('gun')

account_login()




