dict = {'First':1,'Second':2,'Third':3};
print (dict['First'])

#set
s = set([1,2,3,4])
print(s)
#set会自动过滤重复元素
s.add(4);
print(s)
#set可以进行数学上的并集交集操作
s1 = set([1,2,3]);
s2 = set([1,2,4]);
print((s1 & s2))
print((s1 | s2));