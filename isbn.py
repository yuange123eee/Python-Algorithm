n,m = [int(x) for x in input().split()]
l1=[]
l2=[0]*n
for i in range(n):
    x=input().split()
    l1.append(x[0])
    l2[i]=x[1]
    print(l2[i])