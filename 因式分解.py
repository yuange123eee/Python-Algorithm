a = int(input())
b = ""
d=a
q=1
print("n=%d"%(a))
while q:
    if a == 1:
        break
    for i in range(2,a+1):
        if a == i:
            q == 0
            break
        if a % i==0:
            b+="%s * "%i
            a=a/i
            break
print("%s = %s%s" % (d,b,a))