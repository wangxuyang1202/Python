############## 标准数据类型
'''
不可变数据类型（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
可变数据类型（3 个）：List（列表）、Dictionary（字典）、Set（集合）。
Number：包含 int  float  boolean  complex
'''
a = 1
b = 1.0
c = True  # True 首字母需要大写，否则编译错误
d = 1 + 2j  # 复数需要使用j表示虚数单位
print(type(a), type(b), type(c), type(d))  # type 查看变量类型
print(isinstance(a+d, complex), end='')  # isinstance(variable, type/tuple) 判断是否正确
                                         # 若第二个参数输入其他格式，会报错：TypeError: isinstance() arg 2 must be a type or tuple of types
print(a,b)
print()  # 默认输出换行

import keyword
print(keyword.kwlist)  # 输出所有关键字

'''
isinstance 和 type 的区别在于：
type()不会认为子类是一种父类类型。
isinstance()会认为子类是一种父类类型。
'''
class A:
    pass
class B(A):
    pass
print(type(A()) == A)  # True
print(isinstance(A(), A))  # True
print(type(B()) == A)  # False
print(isinstance(B(),A))  # True
#  在python中false的真实值是0，true的真实值是1
print(True+True) # 2
