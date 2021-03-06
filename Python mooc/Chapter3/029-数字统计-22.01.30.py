"""
描述
请统计某个给定范围[L, R]的所有整数中，数字2出现的次数。

比如给定范围[2, 22]，数字2在数2中出现了1次，在数12中出现1次，在数20中出现1次，在数21中出现1次，在数22中出现2次，所以数字2在该范围内一共出现了6次。

输入
输入共 1 行，为两个正整数 L 和 R，之间用一个空格隔开。
输出
输出共 1 行，表示数字 2 出现的次数。
样例输入
样例 #1：
2 22

样例 #2：
2 100
样例输出
样例 #1：
6

样例 #2：
20
"""
n = input().split()          #给定范围区间,将区间整数转化为字符串，进行遍历
total = 0
str1 = ""
# for i in range(int(0),int(1),1):
for i in range(int(n[0]),int(n[1])+1):           #注意 i是整型
    str1+=str(i)          #将遍历的序号转换为字符串，收集起来
    if "2" in str(i):          #对每一个字符串，进行单个字符检查
        c = len(str(i))
        while c != 0:
            if i %10 == 2:                 #对整型i进行（最右边的）个位数的检查，看是否有“2”,其次，检查其左边一位（办法：先除以10，在对2进行求余,看结果是否等于2）
                total += 1
            i = i //10
            c -= 1
# print(str1)
print(total)
