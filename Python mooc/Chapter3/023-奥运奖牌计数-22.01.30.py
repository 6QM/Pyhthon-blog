# 描述
# 2008年北京奥运会，A国的运动员参与了n天的决赛项目(1≤n≤17)。现在要统计一下A国所获得的金、银、铜牌数目及总奖牌数。
#
# 输入
# 输入n＋1行，第1行是A国参与决赛项目的天数n，其后n行，每一行是该国某一天获得的金、银、铜牌数目，以一个空格分开。
# 输出
# 输出1行，包括4个整数，为A国所获得的金、银、铜牌总数及总奖牌数，以一个空格分开。
# 样例输入
# 3
# 1 0 3
# 3 1 0
# 0 3 0
# 样例输出
# 4 4 3 11
d = int(input())
l1 = []
for i in range(d):
    l1 += input().split()         # 添加>>>.split()<<<可以将键入字符间的多余的空格去掉
a = len(l1)
# print(a)
Au = 0
Ag = 0
Cu = 0
while a != 0 :
    b = a - 1
    c = a - 2
    a -= 3
    Cu += int(l1[a-1])           #注意角标最开始是从l1[0]开始，因而对长度应该左偏移1个位置
    Ag += int(l1[b-1])
    Au += int(l1[c-1])
# print(l1)
print("%d %d %d %d" %(Au,Ag,Cu,(Au+Ag+Cu)))
