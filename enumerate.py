from collections import Iterable
L={'a':1,'b':2,'c':3}
# 打印key
# for key in L:
    # print(key)
# 同时迭代key 和value
for k, v in L.items():
    print(k, v)
print(isinstance('abc', Iterable))#str是否可迭代
print(isinstance([1,2,3],Iterable))#list是否可迭代
print(isinstance(123,Iterable))#整数是否可迭代
#按下标循环list，使用内置的enumerate方法
for i,value in enumerate(['a','b','c']):
    print(i, value)