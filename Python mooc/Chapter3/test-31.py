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

