# -*- coding: utf-8 -*-
def createCounter():
	def plus():
		i = 0
		while True:
			i = i + 1
			yield i
	x = plus()
	def counter():
		return next(x)
	return counter

# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')