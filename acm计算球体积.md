描述 根据输入的半径值，计算球的体积。

输入
​    输入数据有多组，每组占一行，每行包括一个实数，表示球的半径。（0<R<100）
输出
​    输出对应的球的体积，对于每组输入数据，输出一行，计算结果四舍五入为整数
​    Hint:PI=3.1415926
样例输入

    1
    1.5

样例输出

    4
    14
---------------------
```c
//C语言版
    #include <stdio.h>
    int main()
    {
    	double p=3.1415926,v,r;
    	while (scanf("%lf",&r)!=EOF)
    	{
    		printf("%d\n",(int)(4.0/3.0*p*r*r*r+0.5));
    	} 
    	return 0;
    }


//思路：因为输入的有小数，所以都用double类型，题目要求四舍五入，但编译器不会自动四舍五入，那么在计算结果后+0.5即可
```



```python
#python版
import math
while 1:
    a=int(input())
    pi=3.1415926
    v=(4/3)*pi*a*a*a
    print(round(v))


#import math
#round()函数可以用来四舍五入

#另一种方法
while 1:
    a=float(input())
    pi=3.1415926
    v=(4/3)*pi*a*a*a+0.5
    print(int(v))




```

