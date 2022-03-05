# 描述
# 利用公式x1 = (-b + sqrt(b*b-4*a*c))/(2*a), x2 = (-b - sqrt(b*b-4*a*c))/(2*a)求一元二次方程ax2+ bx + c =0的根，其中a不等于0。
#
# 输入
# 输入一行，包含三个浮点数a, b, c（它们之间以一个空格分开），分别表示方程ax2 + bx + c =0的系数。
# 输出
# 输出一行，表示方程的解。
# 若b2 = 4 * a * c,则两个实根相等，则输出形式为：x1=x2=...。
# 若b2 > 4 * a * c,则两个实根不等，则输出形式为：x1=...;x2 = ...，其中x1>x2。
# 若b2 < 4 * a * c，则有两个虚根，则输出：x1=实部+虚部i; x2=实部-虚部i，即x1的虚部系数大于等于x2的虚部系数，实部为0时不可省略。实部 = -b / (2*a), 虚部 = sqrt(4*a*c-b*b) / (2*a)
#
# 所有实数部分要求精确到小数点后5位，数字、符号之间没有空格。
# 样例输入
# 样例输入1
# 1.0 2.0 8.0
#
# 样例输入2
# 1 0 1
# 样例输出
# 样例输出1
# x1=-1.00000+2.64575i;x2=-1.00000-2.64575i
#
# 样例输出2
# x1=0.00000+1.00000i;x2=0.00000-1.00000i
import math
l1 = input().split()
a,b,c = float(l1[0]),float(l1[1]),float(l1[2])
if b*b == 4*a*c :                    #注意等号与赋值的区别
    x1 = (-b+math.sqrt(b*b-4*a*c))/(2*a)      #x1=x2
    x2 = x1
    print("x1=x2=%.5f" %(x1) )
elif b*b > 4*a*c :
    x1 = (-b+math.sqrt(b*b-4*a*c))/(2*a)          #x1>x2
    x2 = (-b-math.sqrt(b*b-4*a*c))/(2*a)
    print("x1=%.5f;x2=%.5f" %(x1,x2) )
elif b*b < 4*a*c :
    x1a = -b/(2*a)                   #x1实部

    x1b = math.sqrt(4*a*c-b*b)/(2*a)     #x1虚部
    # x1 = x1a + "+" + x1b + "i"        #x1>x2
    x2a = -b/(2*a)                  #x2实部
    x2b = math.sqrt(4*a*c-b*b)/(2*a)     #x2虚部
    # x2 = x1a + "-" + x1b + "i"        #x1>x2
    if abs(x1a) == 0 and abs(x2a) == 0 :
        x1a = abs(x1a)
        x2a = abs(x2a)

    elif abs(x2a) == 0 :
        x2a = abs(x2a)
    elif abs(x1a) == 0 :
        x1a = abs(x1a)
    # if abs(x1a) == 0 and abs(x2a) == 0 :
    #     print("x1=%.5f+%.5fi;x2=%.5f-%.5fi" % (abs(x1a), x1b, x2a, x2b))
    # elif abs(x2a) == 0 :
    #     print("x2=%.5f+%.5fi;x2=%.5f-%.5fi" % (x1a, x1b, abs(x2a), x2b))

    print("x1=%.5f+%.5fi;x2=%.5f-%.5fi" % (x1a, x1b, x2a, x2b))

