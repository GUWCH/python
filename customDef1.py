#import math
#给一个默认参数2，不传递时默认是2次方
#需要改变默认值时在对应位置输入即可更改
#要传空值的时候用None来判断传入是否为空
def power1(x,n=2):
    s = 1
    while n>0:
    	n = n-1
    	s = s*x
    return s

print(power1(5,3))