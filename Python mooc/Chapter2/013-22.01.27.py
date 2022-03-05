s = input().split()
x,y = float(s[0]),float(s[1])
if x <= 1 and x >= -1 :
    if y<= 1 and y >= -1 :
        print("yes")
    else :
        print("no")
else :
    print("no")