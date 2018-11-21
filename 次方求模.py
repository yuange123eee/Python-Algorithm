x=int(input())
while x:
    a,b,c=input().split(" ")
    a=int(a)
    b=int(b)
    c=int(c)
    i=0
    m=1
    while i<b:
        m=m*a
        i=i+1
    print(m%c)
    x=x-1