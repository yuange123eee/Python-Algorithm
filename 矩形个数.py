try:
    while 1:
        a,b=input().split()
        a=int(a)
        b=int(b)
        sum=0
        for i in range(1,a+1):
            for j in range(1,b+1):
                sum=sum+i*j
        print(sum)
except EOFerror:
    pass
