# -*- coding: utf-8 -*-
#设置主菜单mainmenue
def pmainmenue():
    print('*'*20)
    print('选择菜单')
    print('1.系统设置')
    print('2.招生')
    print('3.')
    print('4.')
    print('5.')
    print('*'*20)
    userchoice=input("输入你的选择:")
    return userchoice
def menue1():
    pass
def menue2():
    pass
def menue3():
    pass
def menue4():
    pass
def menue5():
    pass
def wrongmenue():
    print('没有这个选项，请输入正确的编号：')
    t=pmainmenue()

t=pmainmenue()
if t==1 :
    domenue=menue1()
elif t==2:
    domenue=menue2()
elif t==3:
    domenue=menue3()
elif t==4:
    domenue=menue4()
elif t==5:
    domenue=menue5()
else:
    domenue=wrongmenue()
