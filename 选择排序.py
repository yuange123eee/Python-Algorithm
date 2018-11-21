l=[1,2,3,4,5,66,6,9,76,55,99]
for i in range(len(l)):
    for j in range(i,len(l)):
        if l[i]>l[j]:
            l[i],l[j]=l[j],l[i]
            print(l)
