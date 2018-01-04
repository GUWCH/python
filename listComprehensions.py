# python内置方法 用于创建list的表达式
#生成的的元素放在前面 后面跟for循环 还可以加上判断进行筛选
print([x*x for x in range(1,11) if x%2 == 0])
# 使用两层循环，生成全排列
print([m + n for m in 'ABC' for n in 'XYZ'])
# 使用两个变量生成list
d = {'x':'A','y':'B','z':'C'}
print([k + '=' + v for k, v in d.items()])