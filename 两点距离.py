l=[int(x) for x in input().split()]
for i in range(len(l)):
    s=sqrt((l[0]-l[1])*(l[0]-l[1])+(l[2]-l[3])*(l[2]-l[3]))
    print(float(s))