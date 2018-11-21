# l=[int(x) for x in input().split(" ")]
# l.reverse()
# print(l)

def f():
    x=1
    if n==1:
        return x
    y=1
    if n==2:
        return y
    i=2
    while True:
        x=x+y
        i=i+1
        if i==n:
            return x
print(f())



