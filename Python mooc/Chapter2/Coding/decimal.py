# 保留小数点后5位
s = input().split()
x,y = float(s[0]),float(s[1])
f = (x+y)*x
print("%.5f" % f)