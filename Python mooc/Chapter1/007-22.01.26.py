n = int(input())
list1 = ["","",""]
list1[0] = n%10           # 反向输出的第一个数,
list1[1] = (n//10)%10     # 注意将输入的字符转换成整型，以便参与计算
list1[2] = n//100
print(list1[0],end="")    #  <<,end="">>在使用多个print()时不换行
print(list1[1],end="")
print(list1[2])