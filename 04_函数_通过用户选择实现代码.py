def registeer():
    print('注册')
    
def login():
    print('登录')
    
def user_info():
    print('用户信息')

mapping = {
    '1': (registeer, '注册'),
    '2': (login, '登录'),
    '3': (user_info, '用户信息')
}

line_list = []
for k, v in mapping.items():
    line = '{}.{}'.format(k, v[-1])
    line_list.append(line)
message = ' '.join(line_list)
print(message)    

choice = input('选择：')
func = mapping.get(choice)
if func:
    func[0]()
else:
    print('选择错误')