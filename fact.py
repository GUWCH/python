def fact(n):
    if n==1:
        return 1
    return n * fact(n-1)
print(fact(5))
L = []
n = 1
while n <= 99:
    L.append(n)
    n = n + 2
print(L)
# python高级特性 切片
N = ['Michal','Bob','Jake','Nicolas','Constantine']
#此为常规截取方法
# r = []
# n = 3
# for i in range(n):
#     r.append(N[i])
# print(r)
#python提供了slice方法
print(N[0:3])
#截取倒数最后一个
print(N[-1])
#截取倒数几位
print(N[-2:])
#截取倒数区间
print(N[-3:-1])
#字符串也可执行切片操作