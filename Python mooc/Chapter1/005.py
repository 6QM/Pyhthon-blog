substr = input()  # 第一行：子串  # 解法 1
mainstr = input()  # 第二行：为第一行的子串
a = substr in mainstr  #选中多行进行注释：ctrl+/
list = ["NO","YES"]
print(list[a])  # 借助列表的下标，以及真假与01的等价替换，来完成条件判断
# if substr in mainstr:             # 解法 2 ，使用了条件语句
#     print("Yes")
# else:
#     print("No")
