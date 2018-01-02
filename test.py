# -*- coding: utf-8 -*-
def trim(s):
    if s =='':
        return s
    while s[:1] ==' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[:-1]
    return s
    #可用于去空，所有空格都会去除
    # for char in s:
    #     if char != " ":
    #         result += char
    #return result
# 测试:
if trim('hello  ') != 'hello':
    print('测试失败1!')
elif trim('  hello') != 'hello':
    print('测试失败2!')
elif trim('  hello  ') != 'hello':
    print('测试失败3!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败4!')
elif trim('') != '':
    print('测试失败5!')
elif trim('    ') != '':
    print('测试失败6!')
else:
    print('测试成功7!')