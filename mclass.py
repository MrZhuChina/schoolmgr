# -*- coding: utf-8 -*-
#类模块
class std:
    pass
class cyks:
    xm=''
    xb=''
    lxdh=''
    bkh=''
    sfzh=''
    kc=''
    zw=''
    hjdz=''
    byxx=''
    cjyw=''
    cjsx=''
    cjyy=''
    zf=''
    pm=''
    ylqlb=''
    yx=''
    lq=''
    xnlxr=''
    yfb=''
    fb=''
    bz=''
    
    def __init__(self,xm,xb,bkh):
        self.xm=xm
        self.xb=xb
        self.bkh=bkh
    def check(self):
        pass
#*************
#验证身份证
#字符转数字
chmap = {  
    '0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,  
    'x':10,'X':10  
    }
def ch_to_num(ch):  
    return chmap[ch]      
  
#效验验证位  
def verify_list(l):  
    sum = 0  
    for ii,n in enumerate(l):  
        i = 18-ii  
        weight = 2**(i-1) % 11  
        sum = (sum + n*weight) % 11
    return sum==1
#效验
def verify_string(s):  
    char_list = list(s)  
    num_list = [ch_to_num(ch) for ch in char_list]  
    return verify_list(num_list)  
'''
#**debug**
s=input('输入身份证号:')
if verify_string(s):
    print('合法的身份证号码')
else:
    print('非法的身份证号码')
'''
