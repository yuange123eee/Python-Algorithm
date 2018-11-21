n,k =input().split(" ")
l=[]
i=1
l.append(i)
while i<=int(n):
    j=1
    while j<=int(k):
        if i%j==0:
            if l[i]==0:
                l[i]=0
            else:
                l[i]=0
        j=j+1
    i=i+1
for i in range(1,int(n)):
    if l[i]==1:
        print(i)
