''''''
'''
try:
except:
else:
'''
try:
    a = int(input('请输入一个整数'))
    b = int(input('请输入一个整数'))
    result=a/b
except BaseException as e:
    print('出错了',e)
else:
    print(result)

