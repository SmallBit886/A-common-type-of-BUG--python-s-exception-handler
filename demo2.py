#1
#
lst=[11,22,33,44]   #列表的索引从0开始
print(lst[2])   #33
'''
print(lst[4])   #IndexError: list index out of range
'''

lst=[]
#lst=append('A') #NameError: name 'append' is not defined
lst.append('A')
#append只能一个一个加
lst.append('B')
lst.append('C')
print(lst)#['A', 'B', 'C']

#输入名字找电影名字
lst=[{'title':'A','actors':['lala','haha','gege']},
     {'title':'B','actors':['xixi','bibi','ssss']},
     {'title':'C','actors':['12','13','14']}
    ]
name=input('请输入名字')
for item in lst:    #遍历列表 {}  item又是一个一个字典
   #print(item)
    '''
    {'title': 'A', 'actors': ['lala', 'haha', 'gege']}
    {'title': 'B', 'actors': ['xixi', 'bibi', 'ssss']}
    {'title': 'C', 'actors': ['12', '13', '14']}
    '''
    act_lst=item['actors']  #通过键值对找到演员的列表
    #print(act_lst)
    '''
    ['lala', 'haha', 'gege']
    ['xixi', 'bibi', 'ssss']
    ['12', '13', '14']
    '''
    for actor in act_lst:   #遍历演员的列表
        #print(actor)
        if name in actor:
            print(name,'出演了',item['title']) #为什么item['title']会跟着变化

