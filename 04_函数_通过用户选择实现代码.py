def registeer():
    print('注册')
    
def login():
    print('登录')
    
def user_info():
    print('用户信息')

mapping = {
    '1': registeer,
    '2': login,
    '3': user_info
}

print('1.注册 2.登录 3.用户信息')
choice = input('选择：')
func = mapping.get(choice)
if func:
    func()
else:
    print('选择错误')