# _*_ coding:utf-8 _*_
def findMinAndMax(L):
	if len(L) == 0:
		Min = None
		Max = None
	else:
		Min = L[0]
		for temp in L:
			if temp < Min:
				Min = temp
		Max = L[0]
		for temp in L:
			if temp > Max:
				Max = temp
	return(Min,Max)

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')