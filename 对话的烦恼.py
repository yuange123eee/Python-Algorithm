a=[0,1]
b=[]
l=[int(x) for x in input().split()]
for j in l:
    s=j//2
    y=j%2
    b=b+[y]
    n=s
    b.reverse()
    for i in b:
        print(a[i],end="")

