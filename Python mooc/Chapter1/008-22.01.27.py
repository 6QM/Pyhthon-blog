# 描述
# 输入两个长度为4的字符串，交换这两个字符串的前两个字符后输出  ## 需要将其分割为列表里的元素
# 输入
# 两个长度为4的字符串
# 输出
# 交换这两个字符串的前两个字符后输出
# 样例输入
# ABCD
# 1234
# 样例输出
# 12CD
# AB34
#*******************************************************************************************
#下面是一行内输入两个长度为4的字符串
l1 = input().split()
f1 = l1[0][0]
f2 = l1[0][1]
f3 = l1[0][2]
f4 = l1[0][3]
s1 = l1[1][0]
s2 = l1[1][1]
s3 = l1[1][2]
s4 = l1[1][3]
n1 = s1
n2 = s2
n3 = f1
n4 = f2

l1[0] = n1+n2+f3+f4
print(l1[0])
l1[1] = n3+n4+s3+s4
print(l1[1])
#*******************************************************************************************
#下面是用两行输入长度为4的字符串
l1 = input()
l2 = input()

f1 = l1[0]
f2 = l1[1]
f3 = l1[2]
f4 = l1[3]
s1 = l2[0]
s2 = l2[1]
s3 = l2[2]
s4 = l2[3]
n1 = s1
n2 = s2
n3 = f1
n4 = f2

l1 = n1+n2+f3+f4
print(l1)
l2 = n3+n4+s3+s4
print(l2)