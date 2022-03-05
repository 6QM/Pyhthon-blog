"""
描述
监护室每小时测量一次病人的血压，若收缩压在90 - 140之间并且舒张压在60 - 90之间（包含端点值）则称之为正常，现给出某病人若干次测量的血压值，计算病人保持正常血压的最长小时数。
输入
第一行为一个正整数n，n < 100
其后有n行，每行2个正整数，分别为一次测量的收缩压和舒张压，中间以一个空格分隔。
输出
输出仅一行，血压连续正常的最长小时数。
样例输入
4
100 80            #均在区间内->正常
90 50
120 60            #均在区间内->正常
140 90            #均在区间内->正常
样例输出
2
"""
#测血压
n = int(input())
l1= []
for i in range(n):
    l1 += input().split()
# print(l1)
# 存所有的值
x = 0
strx = ""
lx = []
#存连续正常的检测次数（小时数）
for i in range(0,len(l1),2):                                         #每两个一组，进行遍历，相当于对输入的每一行进行整行的顺序判断
    if ((90 <= int(l1[i]) <= 140) and (60 <= int(l1[i+1]) <= 90)) :   #对一组的两个进行“正常'判断
        x += 1
        strx = str(x)
        print("if")                                 #对于条件语句，进行print输出显示，是一个不错的习惯!!!
        if i == len(l1)-2:
            lx += strx                              #考虑在做最后一次判断（遍历到最右侧一组，即键入的最后一行时），仍为正常，需对列表lx进行更新（+1）
    else:
        lx += strx
        x = 0
        print("else")
        #不记录，置零
# print(lx)
# print(len(lx))
print(max(lx))

