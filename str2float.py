# -*- coding: utf-8 -*-
from functools import reduce

def char2int(char):
	digits = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'.':None}
	return digits[char]

def multi(x,y):
	if y== None:
		return x
	return x*10+y

def str2float(s):
	temp = float(reduce(multi,map(char2int,s)))
	return temp/(10**(len(s)-s.find('.')-1))
	
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')