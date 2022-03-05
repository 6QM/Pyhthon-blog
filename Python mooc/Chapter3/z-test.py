"""
print(5//2)
print(int(4/2))
print(5%3)

不换行>>>,end=" "<<<
"""
# for i in range(9,0,-1):
#     print(i)
# print("End,%s" % (15%10))
# str = "1123456"
# str1 = ""
# l = len(str)-1
# for i in range(l,-1,-1):
#     print(str[i])
#     str1 +=str[i]
# print(str1)
"""
x = 1
while 1 :
    x +=1
    n10 = 0
    str7 = ""
    str9 = ""
    str91 = ""
    # while 1:  # and (1< int(str7)//100 < 9) and  (1< int(str91)//100 < 9):
    n10 = x
    n7 = n10
    n9 = n10
    while n10 != 0:  # 将10进制转换为7进制
        m0 = n10
        n10 %= 7
        str7 += str(n10)
        n10 = m0 // 7
    print(str7 + "   7777777")  # 逆序，则其该十进制的九进制为此数目的逆序
    while n9 != 0:  # 将10进制转换为9进制
        m1 = n9
        n9 %= 9
        str9 += str(n9)
        n9 = m1 // 9
    # print(str9)  # 逆序，则其该十进制的九进制为此数目的逆序
    # 将字符串逆序为正常的九进制
    l = len(str9) - 1
    for i in range(l, -1, -1):
        str91 += str9[i]  # 顺序，则其该十进制的九进制为此数目
    print(str91 + "   9999999")
    if str91 == str7:
        print(str(x) + "Bingo")
"""
n = int(input())
l1 = []
l2 = []
# t1 = 0
t2 = 1
for i in range(n):
    l1 += input().split()                                               #将所有测量的情况输入为一个列表进行储存
print(l1)
l2 = len(l1)                                                      #获得列表长度，以便进行遍历元素
print("列表长度为：",str(l2))
for j in range(0,l2-3,2) :
    if ((90 <= int(l1[j]) <= 140) and (60 <= int(l1[j+1]) <= 90)) :    #首次测得某个周期内收缩压和舒张压两者均“正常”的第”1“小时（该周期有可能只为1小时）
        t1 = 1                                                        #记录当前“正常”周期的小时数
        if ((90 <= int(l1[j+2]) <= 140) and (60 <= int(l1[j+3]) <= 90)) :    #连续”正常“的第”t1+1“小时
            t2 += t1                                                          #记录当前“正常”周期的连续小时数
            print("连续============================================================正常的第%d个小时" % t2)
        else:
            print("重置连续小时的寄存器")
            l2 += str(t2).split()
            t2 = 0
print("寄存器 %s" %l1)
print("最后连续小时数:%d"  % t2)
print(max(l2))
