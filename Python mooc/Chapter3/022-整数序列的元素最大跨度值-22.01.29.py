# 描述
# 给定一个长度为n的非负整数序列，请计算序列的最大跨度值（最大跨度值 = 最大值减去最小值）。
#
# 输入
# 一共2行，第一行为序列的个数n（1 <= n <= 1000)，第二行为序列的n个不超过1000的非负整数，整数之间以一个空格分隔。
# 输出
# 输出一行，表示序列的最大跨度值。
# 样例输入
# 6
# 3 0 8 7 5 9
# 样例输出
# 9
n = input()
s = input().split()
maxV = minV = int(s[0])
for x in s:
    # if maxV < int[x] :
    #     maxV = int[x]
    maxV = max(maxV,int(x))             #注意x的含义是对应角标下的字符串中的元素！！
    minV = min(minV,int(x))
print(maxV-minV)
