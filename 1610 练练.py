# Description
#
# 给定一个整数n，请求出0与n之间的所有偶数的和（包括0和n）？
# Input
# 有多组数据
#
# 每种情况第一行一个整数n（0 <= n <= 500)
# （用EOF结尾）
# Output
# # 每行输出所有偶数的和
try:
    l = [int(x) for x in input()]
    sum = 0
    for i in l:
        if l[i] % 2 == 0:
            sum = sum + l[i]
        print(sum)

except EOFerror:
    pass