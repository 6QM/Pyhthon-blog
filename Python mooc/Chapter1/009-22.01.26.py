# 描述
# 输入两个长度为3的字符串，每个串前两个字符是数字,后一个字符是字母。 求这两个串中的整数的和
# # 输入
# 一行，两个字符串
# 输出
# 两个字符串中整数的和
# 样例输入
# 12B 34D
# 样例输出
# 46

l1 = input()
n1 = l1.split()[0][0]
n2 = l1.split()[0][1]
n3 = l1.split()[1][0]
n4 = l1.split()[1][1]
print(int(n1+n2)+int(n3+n4))       # 对字符串线拼接，再转为整型