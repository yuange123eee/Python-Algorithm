while 1:
    a,b,k,c,d=input()
    a,b,c,d=int(a),int(b),int(c),int(d)
    x=a*d
    y=b*d
    c=c*b
    d=d*b
    if k=="+":
        x=x+c
        if x%y==0:
            print(x/y)
        elif x%y!=0:
            i=2
            while i<=y:
                if x%i==0 and y%i==0:
                    x=x/i
                    y=y/i
                    i=2
            i=i+1
    print("%d/%d"%(x,y))