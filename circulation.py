# arr = [1,2,3,4,5,6,7,8,9]
# sum = 0;
# for x in arr:
# 	sum = sum + x;
# print(sum)
# for循环
list = list(range(101));
sum = 0
for x in list:
	sum = sum + x;
print(sum)

#while循环
sum2 = 0;
n = 99;
while n > 0:
	sum2 = sum2 + n;
	n = n-2;
print(sum2)

names = ['Bart', 'Lisa','Adam'];
for x in names:
	print('Hello,'+ x);

#break中断循环
n = 1;
while n<=100:
	if n>10:
		break;
	print(n)
	n = n + 1;
print('End');

#continue跳过当前循环
n = 0;
while n < 10:
	n = n + 1;
	if n % 2 == 0:
		continue;
	print(n);