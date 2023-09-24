
#python的异常处理机构
'''try:
   except
'''
try:
    a = int(input('请输入一个整数'))
    b = int(input('请输入一个整数'))
    result=a/b
    print(result)
except ZeroDivisionError:
    print('除数不能为0')
print('程序结束')