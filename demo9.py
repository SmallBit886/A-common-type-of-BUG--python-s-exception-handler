#使用traceback打印异常信息

#print(10/0)
import traceback
try:
    print('----------------------------')
    print(1/0)
except:
    traceback.print_exc()
    '''打印到日志当中'''