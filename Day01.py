################################ 1.注释
# 此处为单行注释
'''
此处为多行注释
'''
"""
此处同样为多行注释
"""
############################### 2.输出语句
print("hello \nworld!")
##############################  3.行与缩进
# python用缩进，而不使用{}
if True:
    print ("Answer")
    print ("True")
else:
    print ("Answer")
    print ("False")    # 缩进不一致，会导致运行错误
##############################  4.多行语句 换行
total = 1 +\
        2 +\
        3    # 反斜杠“\”实现多行语句，否则会导致运行错误
print(total)
total2 = [1,
          2,
          3, 4] # 在 [], {}, 或 () 中的多行语句，不需要使用反斜杠(\)
print(total2)
############################### 5.截取字符串 变量[起始下标：结束下标：步长] 起始下标从0开始
text = '巴拉'*2+'小魔仙'
print(text)
textsub = text[-1:]
print(textsub)
############################## 6.等待用户输入
# input("\n请输入： 按下enter键退出")
############################## 7.同一行显示多条语句
import sys; x = 'python'; sys.stdout.write(x+"\n")
############################## 8.多个语句构成代码组
input1=2
if input1==1:
    print(1)
elif input1==2:
    print(2)
else:
    print(3)
print(input1, end="")  # 输出不换行