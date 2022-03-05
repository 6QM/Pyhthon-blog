import re
a = "Beautiful, is; better*than\nugly"
print(re.split(";| |,|\*|\n",a)) #注意转义字符的运行，对于*字符，需写作*\