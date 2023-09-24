''''''
'''
try:
except:
else:
finally:    #无论是否产生异常，都会执行
'''
try:
    a = int(input('请输入一个整数'))
    b = int(input('请输入一个整数'))
    result=a/b
except BaseException as e:
    print('出错了',e)
else:
    print(result)
finally:
    print('谢谢您的使用，程序结束')
