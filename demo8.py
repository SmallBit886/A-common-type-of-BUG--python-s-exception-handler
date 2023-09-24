''''''
'''python中常见的异常类型'''
#数学运算的异常
#print(10/0) #ZeroDivisionError: division by zero

#索引异常
lst=[11,2,234,5]
#print(lst[4])   #IndexError: list index out of range

#映射中没有这个键
dic={'a':'1','b':'2'}
#print(dic['d']) #KeyError: 'd'

#未声明/初始化对象（没有属性）
#print(name) #NameError: name 'name' is not defined

#Python语法错误
#int a =10   #SyntaxError: invalid syntax

#传入无效的参数
#a=int('hello')  #ValueError: invalid literal for int() with base 10: 'hello'
