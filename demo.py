# -*- coding: UTF-8 -*-

# 这是单行注释，学习参考链接地址：https://www.w3cschool.cn/python/python-variable-types.html
import random

"""
这是长文本注释，双引号，随便多长，呵呵
"""

'''
这也是长文注释，单引号的
'''

print "世界你好，哈哈"

# 变量
a=b=c=9 #多个变量赋值同为9
print b
e,f,g=9,2.03,"jojo" #为多个对象指定多个变量
print g

# 字符串
strs = 'Hello World!'
print strs[0:5] #输出为：love
print strs * 2 # 输出字符串两次
print strs + "TEST" # 输出连接的字符串

# 列表 List
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
print list # 输出完整列表
print list[0] # 输出列表的第一个元素
print list[1:3] # 输出第二个至第三个的元素 
print list[2:] # 输出从第三个开始至列表末尾的所有元素
print tinylist * 2 # 输出列表两次
print list + tinylist # 打印组合的列表

# 原组 类似于List
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2 )
tinytuple = (123, 'john')
print tuple # 输出完整元组
print tuple[0] # 输出元组的第一个元素
print tuple[1:3] # 输出第二个至第三个的元素 
print tuple[2:] # 输出从第三个开始至列表末尾的所有元素
print tinytuple * 2 # 输出元组两次
print tuple + tinytuple # 打印组合的元组

# 字典 {}
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

print dict['one'] # 输出键为'one' 的值
print dict[2] # 输出键为 2 的值
print tinydict # 输出完整的字典
print tinydict.keys() # 输出所有键
print tinydict.values() # 输出所有值

# 数据类型转换
aa=int("123456")
bb=str(2) 
print str(aa)+bb

'''
# 算术运算符
 +	加 - 两个对象相加	a + b 输出结果 30
-	减 - 得到负数或是一个数减去另一个数	a - b 输出结果 -10
*	乘 - 两个数相乘或是返回一个被重复若干次的字符串	a * b 输出结果 200
/	除 - x除以y	b / a 输出结果 2
%	取模 - 返回除法的余数	b % a 输出结果 0
**	幂 - 返回x的y次幂	a**b 为10的20次方， 输出结果 100000000000000000000
//	取整除 - 返回商的整数部分	9//2 输出结果 4 , 9.0//2.0 输出结果 4.0

# 比较运算符
 ==	等于 - 比较对象是否相等	(a == b) 返回 False。
!=	不等于 - 比较两个对象是否不相等	(a != b) 返回 true.
<>	不等于 - 比较两个对象是否不相等	(a <> b) 返回 true。这个运算符类似 != 。
>	大于 - 返回x是否大于y	(a > b) 返回 False。
<	小于 - 返回x是否小于y。所有比较运算符返回1表示真，返回0表示假。这分别与特殊的变量True和False等价。注意，这些变量名的大写。	(a < b) 返回 true。
>=	大于等于 - 返回x是否大于等于y。	(a >= b) 返回 False。
<=	小于等于 - 返回x是否小于等于y。	(a <= b) 返回 true。

# 赋值运算符
 =	简单的赋值运算符	c = a + b 将 a + b 的运算结果赋值为 c
+=	加法赋值运算符	c += a 等效于 c = c + a
-=	减法赋值运算符	c -= a 等效于 c = c - a
*=	乘法赋值运算符	c *= a 等效于 c = c * a
/=	除法赋值运算符	c /= a 等效于 c = c / a
%=	取模赋值运算符	c %= a 等效于 c = c % a
**=	幂赋值运算符	c **= a 等效于 c = c ** a
//=	取整除赋值运算符	c //= a 等效于 c = c // a
'''

# 条件语句
num = 5     
if num == 3:            # 判断num的值
    print 'boss'        
elif num == 2:
    print 'user'
elif num == 1:
    print 'worker'
elif num < 0:           # 值小于零时输出     print 'error' else:     print 'roadman'     # 条件均不成立时输出 
	print 0.00

# for循环
for letter in 'Python':     # 第一个实例
   print '当前字母 :', letter
   
fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # 第二个实例
	print '当前字母 :', fruit
	
# 随机数
import random #需要引用包
print random.random() #随机生成下一个实数，它在[0,1)范围内。
print random.choice(range(99)) #从0到9中随机挑选一个整数。
 
# html代码标识符
print r'\n'
print R'\"'

# 时间
import time;  # 引入time模块
ticks = time.time()
print "当前时间戳为:", ticks

localtime = time.localtime(time.time())
print "本地时间为 :", localtime
localtime = time.asctime( time.localtime(time.time()) )
print "本地时间为 :", localtime
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) # 2016-04-07 10:25:09

# 函数
def printme( description="这是给默认值，如果调用函数没传值则用默认值"):
   "打印任何传入的字符串"
   print description;
   return; 

printme(description="调用用户自定义函数：printme"); 
printme();

# 读取键盘输入
str = raw_input("请输入：");
print "你输入的内容是: ", str

# 
import os
 
# 给出当前的目录
os.getcwd()