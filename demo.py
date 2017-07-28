# -*- coding: UTF-8 -*-

# ���ǵ���ע�ͣ�ѧϰ�ο����ӵ�ַ��https://www.w3cschool.cn/python/python-variable-types.html
import random

"""
���ǳ��ı�ע�ͣ�˫���ţ����೤���Ǻ�
"""

'''
��Ҳ�ǳ���ע�ͣ������ŵ�
'''

print "������ã�����"

# ����
a=b=c=9 #���������ֵͬΪ9
print b
e,f,g=9,2.03,"jojo" #Ϊ�������ָ���������
print g

# �ַ���
strs = 'Hello World!'
print strs[0:5] #���Ϊ��love
print strs * 2 # ����ַ�������
print strs + "TEST" # ������ӵ��ַ���

# �б� List
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
print list # ��������б�
print list[0] # ����б�ĵ�һ��Ԫ��
print list[1:3] # ����ڶ�������������Ԫ�� 
print list[2:] # ����ӵ�������ʼ���б�ĩβ������Ԫ��
print tinylist * 2 # ����б�����
print list + tinylist # ��ӡ��ϵ��б�

# ԭ�� ������List
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2 )
tinytuple = (123, 'john')
print tuple # �������Ԫ��
print tuple[0] # ���Ԫ��ĵ�һ��Ԫ��
print tuple[1:3] # ����ڶ�������������Ԫ�� 
print tuple[2:] # ����ӵ�������ʼ���б�ĩβ������Ԫ��
print tinytuple * 2 # ���Ԫ������
print tuple + tinytuple # ��ӡ��ϵ�Ԫ��

# �ֵ� {}
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

print dict['one'] # �����Ϊ'one' ��ֵ
print dict[2] # �����Ϊ 2 ��ֵ
print tinydict # ����������ֵ�
print tinydict.keys() # ������м�
print tinydict.values() # �������ֵ

# ��������ת��
aa=int("123456")
bb=str(2) 
print str(aa)+bb

'''
# ���������
 +	�� - �����������	a + b ������ 30
-	�� - �õ���������һ������ȥ��һ����	a - b ������ -10
*	�� - ��������˻��Ƿ���һ�����ظ����ɴε��ַ���	a * b ������ 200
/	�� - x����y	b / a ������ 2
%	ȡģ - ���س���������	b % a ������ 0
**	�� - ����x��y����	a**b Ϊ10��20�η��� ������ 100000000000000000000
//	ȡ���� - �����̵���������	9//2 ������ 4 , 9.0//2.0 ������ 4.0

# �Ƚ������
 ==	���� - �Ƚ϶����Ƿ����	(a == b) ���� False��
!=	������ - �Ƚ����������Ƿ����	(a != b) ���� true.
<>	������ - �Ƚ����������Ƿ����	(a <> b) ���� true�������������� != ��
>	���� - ����x�Ƿ����y	(a > b) ���� False��
<	С�� - ����x�Ƿ�С��y�����бȽ����������1��ʾ�棬����0��ʾ�١���ֱ�������ı���True��False�ȼۡ�ע�⣬��Щ�������Ĵ�д��	(a < b) ���� true��
>=	���ڵ��� - ����x�Ƿ���ڵ���y��	(a >= b) ���� False��
<=	С�ڵ��� - ����x�Ƿ�С�ڵ���y��	(a <= b) ���� true��

# ��ֵ�����
 =	�򵥵ĸ�ֵ�����	c = a + b �� a + b ����������ֵΪ c
+=	�ӷ���ֵ�����	c += a ��Ч�� c = c + a
-=	������ֵ�����	c -= a ��Ч�� c = c - a
*=	�˷���ֵ�����	c *= a ��Ч�� c = c * a
/=	������ֵ�����	c /= a ��Ч�� c = c / a
%=	ȡģ��ֵ�����	c %= a ��Ч�� c = c % a
**=	�ݸ�ֵ�����	c **= a ��Ч�� c = c ** a
//=	ȡ������ֵ�����	c //= a ��Ч�� c = c // a
'''

# �������
num = 5     
if num == 3:            # �ж�num��ֵ
    print 'boss'        
elif num == 2:
    print 'user'
elif num == 1:
    print 'worker'
elif num < 0:           # ֵС����ʱ���     print 'error' else:     print 'roadman'     # ������������ʱ��� 
	print 0.00

# forѭ��
for letter in 'Python':     # ��һ��ʵ��
   print '��ǰ��ĸ :', letter
   
fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # �ڶ���ʵ��
	print '��ǰ��ĸ :', fruit
	
# �����
import random #��Ҫ���ð�
print random.random() #���������һ��ʵ��������[0,1)��Χ�ڡ�
print random.choice(range(99)) #��0��9�������ѡһ��������
 
# html�����ʶ��
print r'\n'
print R'\"'

# ʱ��
import time;  # ����timeģ��
ticks = time.time()
print "��ǰʱ���Ϊ:", ticks

localtime = time.localtime(time.time())
print "����ʱ��Ϊ :", localtime
localtime = time.asctime( time.localtime(time.time()) )
print "����ʱ��Ϊ :", localtime
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) # 2016-04-07 10:25:09

# ����
def printme( description="���Ǹ�Ĭ��ֵ��������ú���û��ֵ����Ĭ��ֵ"):
   "��ӡ�κδ�����ַ���"
   print description;
   return; 

printme(description="�����û��Զ��庯����printme"); 
printme();

# ��ȡ��������
str = raw_input("�����룺");
print "�������������: ", str

# 
import os
 
# ������ǰ��Ŀ¼
os.getcwd()