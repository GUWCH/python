import math
a = int (input('a='))
b = int (input('b='))
c = int (input('c='))
def quadratic(a,b,c):
	x1 = (-b+math.sqrt(b**2-4*a*c))/2
	x2 = (-b-math.sqrt(b**2-4*a*c))/2
	return x1,x2
print(quadratic(a,b,c))
def my_abs(x):
	#参数类型检查，只能允许整数和浮点数类型
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x>0:
        return x;
    else:
        return -x;
print(my_abs(9))
print(my_abs(-5))
#空函数
def nop():
#pass 占位符，让代码能运行
	pass;

#游戏中计算坐标
x = int(input('x='))
y = int(input('y='))
step = int(input('step='))
angle = float((input('angle=')))
def move(x,y,step,angle):
	nx = x + step*math.cos(angle)
	ny = y + step*math.sin(angle)
	return nx,ny 

print(move(x,y,step,angle))
