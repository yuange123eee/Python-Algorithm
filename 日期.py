month,day=[int(x) for x in input().split("/")]
c=0
if month==1 and 0<=day<=31:
    c=day
    print("这是2018年的%d天"%(c))
elif month==2 and 0<=day<=28:
    c=31+day
    print("这是2018年的%d天"%(c))
elif month==3 and 0<=day<=31:
    c=31+28+day
    print("这是2018年的%d天"%(c))
elif month==4 and 0<=day<=30:
    c=31+28+31+day
    print("这是2018年的%d天"%(c))
elif month==5 and 0<=day<=31:
    c=31+28+31+30+day
    print("这是2018年的%d天"%(c))
elif month==6 and 0<=day<=30:
    c=31+28+31+30+31+day
    print("这是2018年的%d天"%(c))
elif month==7 and 0<=day<=31:
    c=31+28+31+30+31+30+day
    print("这是2018年的%d天"%(c))
elif month==8 and 0<=day<=31:
    c=31+28+31+30+31+30+31+day
    print("这是2018年的%d天"%(c))
elif month==9 and 0<=day<=30:
    c=31+28+31+30+31+30+31+31+day
    print("这是2018年的%d天"%(c))
elif month==10 and 0<=day<=31:
    c=31+28+31+30+31+30+31+31+30+day
    print("这是2018年的%d天"%(c))
elif month==11 and 0<=day<=30:
    c=31+28+31+30+31+30+31+31+30+31+day
    print("这是2018年的%d天" % (c))
elif month ==12 and 0<=day<=31:
    c=31+28+31+30+31+30+31+31+30+31+30+day
    print("这是2018年的%d天" % (c))


