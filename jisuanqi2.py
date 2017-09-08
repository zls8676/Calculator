#计算机
#导入tkinter
import tkinter

root = tkinter.Tk()

root.minsize(500,500)
root.title('Apple10 puls')

#定义运算操作的列表
lists =[]

#定义操作标志 运算
flag = False  # True点了运算  False 没点

#定义是否点了 =
isresult = False



#创建sz变量
sz = tkinter.StringVar()
sz.set('0')



#定义显示数字的方法
def sznum(num):
    global flag
    global isresult
    #检测是否点击了运算符
    if flag !=False:
        sz.set('0')

    #获取label中原有数值
    oldnum = sz.get()

    #检测原有显示数字是否为0
    if oldnum == '0':
        sz.set(num)
    else:
        #将原有数值和新的数值进行拼合
        print(oldnum+num)
        newnum = oldnum+num
        sz.set(newnum)
    #将运算标志重置
    flag = False
    #重置等号标志
    isresult = False
    
def dian(num):
    
    a = sz.get()
    if (num == 0) or ('.' not in list(a)):
        sz.set(a+num)
    
    
#定义加法的方法
def add():
    print('加法操作')
    #全局化 lists
    global lists
    global flag
    global isresult

    #一旦按了该按钮,表示第一个数字已经写完,将第一个数字加入列表
    #获取第一个完整数字,并且加入列表
    fullnum  =sz.get()
    lists.append(fullnum)

    #点击该按钮如果原有元素清空并且将运算结果作为第一个元组加进去
    if len(lists) >=3:
        result = str(eval(''.join(lists)))
        print(result)
        #将列表的原有元素清空并且将运算结果作为第一个元组加入进去
        lists = [result]
        #将结果显示
        sz.set(result)
    #将当前操作符号加入列表

    lists.append('+')
    print(lists)

    #设置标志标示点击运算符号
    flag = True
    print(lists)
    
    #重置等号
    
    
    isresult = False
    
#定义减法的方法
def jianfa():
    
    print('减法操作')

    #全局化lists
    global lists
    global flag
    global isresult
    

    
    #一旦按了该按钮 表示第一个数字已经写完，将第一个数字加入列表
    #获取第一个完整数字，并且加入列表
    fullnum = sz.get()
    lists.append(fullnum)

    #点击该按钮如果已经存在数字和运算符号，将前面的数值运算出来
    if len(lists) >= 3:
        result = str(eval(''.join(lists)))
        print(result)
        #将列表的原有元素清空并且将运算结果作为第一个元组加进去
        lists = [result]
        #将结果显示
        sz.set(result)
    
    #将当前操作符号加入列表
    lists.append('-')
    print(lists)

    #清空当前显示信息
    #show.set(0)

    #设置标志标识点击了运算符号
    flag = True
    print(lists)
    #重置等号
    isresult = False
    
#定义乘法的方法
def cf():
    print('乘法操作')

    #全局化lists
    global lists
    global flag
    global isresult

    
    #一旦按了该按钮 表示第一个数字已经写完，将第一个数字加入列表
    #获取第一个完整数字，并且加入列表
    fullnum = sz.get()
    lists.append(fullnum)

    #点击该按钮如果已经存在数字和运算符号，将前面的数值运算出来
    if len(lists) >= 3:
        result = str(eval(''.join(lists)))
        print(result)
        #将列表的原有元素清空并且将运算结果作为第一个元组加进去
        lists = [result]
        #将结果显示
        sz.set(result)
    
    #将当前操作符号加入列表
    lists.append('*')
    print(lists)

    #清空当前显示信息
    #sz.set(0)

    #设置标志标识点击了运算符号
    flag = True
    print(lists)
    #重置等号
    isresult = False
#定义除法的方法
def chuf():
    print('除法操作')

    #全局化lists
    global lists
    global flag
    global isresult

    
    #一旦按了该按钮 表示第一个数字已经写完，将第一个数字加入列表
    #获取第一个完整数字，并且加入列表
    fullnum = sz.get()
    lists.append(fullnum)

    #点击该按钮如果已经存在数字和运算符号，将前面的数值运算出来
    if len(lists) >= 3:
        print(sz.get())
        result = str(eval(''.join(lists)))
        print(result)
        #将列表的原有元素清空并且将运算结果作为第一个元组加进去
        lists = [result]
        #将结果显示
        sz.set(result)
    
    #将当前操作符号加入列表
    lists.append('/')


    print(lists)

   

    #清空当前显示信息
    #show.set(0)

    #设置标志标识点击了运算符号
    flag = True
    print(lists)
    #重置等号
    isresult = False
#定义正负的操作方法
def zf():
    zfnum = sz.get()
    if zfnum[0] == '-':
      sz.set(zfnum[1:])
    elif zfnum[0] !='-' and zfnum != '0':
        sz.set('-'+zfnum)
        
    
#定义清空操作
def qk():
    global flag
    flag = []
    sz.set('0')

    return sz.set
    
    

#定义退格操作
def tg():

    if sz.get()=='' or sz.get()=='0':
        sz.set('0')
        return
    else:
        num = len(sz.get())

        if num >1:
            anum = sz.get()
            
            anum = anum[0:num-1]
            sz.set(anum)
        else:
            sz.set('0')
            








#获取结果的方法
def dengyu():
    print('结果操作')

    
    
    global lists
    global isresult
    #判断上一次点击是不是等号
    if isresult != False:
        #退出函数
        return
    
    #将当前界面中的数字加入列表然后计算
    lists.append(sz.get())

    #将列表中的数据进行运算，运算之后显示
    if len(lists) >= 3:
        result = str(eval(''.join(lists)))
        print(result)
        #计算完毕，清空列表
        lists = []
        #在界面中显示结果
        sz.set(result)
        #设置标志标识点击了运算符号
        flag = True
    #等号点击了标志
    isresult = True
  
#用户显示操作数据label

label = tkinter.Label(root,textvariable=sz,
                      width=10,font=('宋体',30),
                      fg = 'black',bd = 10,bg='#fff',
                      anchor = 'e')
label.place(x=10,y=10,width=480,height=80)






#创建按钮
bth1 = tkinter.Button(root,text = '1',font=('楷体',40,'bold'),bg='cyan',fg='red',bd = 10,command = lambda : sznum('1'))
bth1.place(x=30,y=100,width = 80,height =80)
#创建按钮

bth2 = tkinter.Button(root,text= '2',font=('楷体',40,'bold'),bg='cyan',fg='red',bd = 10,command = lambda : sznum('2'))
bth2.place(x=120,y=100,width = 80,height =80)
#创建按钮

bth3 = tkinter.Button(root,text= '3',font=('楷体',40,'bold'),bg='cyan',fg='red',bd = 10,command = lambda : sznum('3'))
bth3.place(x=220,y=100,width = 80,height = 80)
#创建按钮
bth4 = tkinter.Button(root,text = '4',font=('楷体',40,'bold'),bg='cyan',fg='red',bd = 10,command = lambda : sznum('4'))
bth4.place(x=30,y=190,width=80,height=80)

bth5 = tkinter.Button(root,text = '5',font=('楷体',40,'bold'),bg='cyan',fg='red',bd = 10,command = lambda : sznum('5'))
bth5.place(x=120,y=190,width=80,height=80)


bth6 = tkinter.Button(root,text = '6',font=('楷体',40,'bold'),bg='cyan',fg='red',bd = 10,command = lambda : sznum('6'))
bth6.place(x=220,y=190,width=80,height=80)

bth7 = tkinter.Button(root,text = '7',font=('楷体',40,'bold'),bg='cyan',fg='red',bd = 10,command = lambda : sznum('7'))
bth7.place(x=30,y=290,width=80,height=80)

bth8= tkinter.Button(root,text = '8',font=('楷体',40,'bold'),bg='cyan',fg='red',bd = 10,command = lambda : sznum('8'))
bth8.place(x=120,y=290,width=80,height=80)

bth9 = tkinter.Button(root,text = '9',font=('楷体',40,'bold'),bg='cyan',fg='red',bd = 10,command = lambda : sznum('9'))
bth9.place(x=220,y=290,width=80,height=80)

bth0 = tkinter.Button(root,text = '0',font=('楷体',40,'bold'),bg='cyan',fg='red',bd = 10,command = lambda : sznum('0'))
bth0.place(x=30,y=380,width=170,height=80)

bthd = tkinter.Button(root,text = '.',font=('楷体',40,'bold'),bg='cyan',fg='red',bd = 10,command = lambda : dian('.'))
bthd.place(x=220,y=380,width=80,height=80)

bthzf = tkinter.Button(root,text = '±',font=('楷体',40,'bold'),bg='cyan',fg='red',bd = 10,command =zf)
bthzf.place(x=400,y=100,width=80,height=80)

btht = tkinter.Button(root,text = '←',font=('楷体',40,'bold'),bg='cyan',fg='red',bd = 10,command=tg)
btht.place(x=400,y=190,width=80,height=80)

bthc = tkinter.Button(root,text = 'c',font=('楷体',40,'bold'),bg='cyan',fg='red',bd = 10,command =qk)
bthc.place(x=400,y=290,width=80,height=80)

bthadd = tkinter.Button(root,text = '＋',font=('楷体',40,'bold'),bg='cyan',fg='red',bd = 10,command= add)
bthadd.place(x=310,y=380,width=80,height=80)

bthj = tkinter.Button(root,text = '－',font=('楷体',40,'bold'),bg='cyan',fg='red',bd = 10,command=jianfa)
bthj.place(x=310,y=290,width=80,height=80)

bthc = tkinter.Button(root,text = '×',font=('楷体',40,'bold'),bg='cyan',fg='red',bd = 10,command=cf)
bthc.place(x=310,y=190,width=80,height=80)

bthc = tkinter.Button(root,text = '÷',font=('楷体',40,'bold'),bg='cyan',fg='red',bd = 10,command= chuf)
bthc.place(x=310,y=100,width=80,height=80)

bthc = tkinter.Button(root,text = '＝',font=('楷体',40,'bold'),bg='cyan',fg='red',bd = 10,command=dengyu)
bthc.place(x=400,y=380,width=80,height=80)
#底部标签
label1 = tkinter.Label(root,text = '龙哥荣誉出品',bg = 'yellow',font = ('黑体',20,'bold'))
label1.place(x=30,y=465,width=450,height =30)

root.mainloop()




