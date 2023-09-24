#BUG的常见类型
''''''
#1
'''input()返回的类型为字符串类型'''
age=input('请输入你的年龄')
print(type(age))    #<class 'str'>
if int(age)>=18:
    print('成年人')
else:
    print('未成年人')
#2
i=0
while i<10: #NameError: name 'i' is not defined
    print(i)
    i+=1
#3
for i in range(3):
    uname=input('请输入用户名')
    pwd=input('请输入密码')
    if uname=='smallbite' and pwd=='mjb2002621':
        print('输入正确')
        break
    else:
        print('输入有误，请重新输入！')
else:
    print('对不起，三次输入均有误')

