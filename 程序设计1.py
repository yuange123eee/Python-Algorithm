a=int(input())
while a>0:
    s1=0
    s2=0
    x=input().split(" ")
    for i in x[0]:
        if i%2!=0:
            s1=s1+i
        elif i%2==0:
            s2=s2+i
        print(s1,s2)


