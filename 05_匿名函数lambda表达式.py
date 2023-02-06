
def func1(x, y):
    return x+y

# lambda 参数：代码块
func2 = lambda x,y: x+y
print(func2(1,2))

# 无参数
func3 = lambda : 100
print(func3())

# 动态参数
func4 = lambda *args, **kwargs: len(args)+len(kwargs)
print(func4(11,22,33,a1=44))

