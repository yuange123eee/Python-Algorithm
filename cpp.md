位，字节，字

字节是最常用的计算机存储单位。**1个字节等于8个位**

字：根据机器的不同，所占的位数也不同

**scanf函数**

例:

​	scanf("%d",&k);

**细节的地方**



****

**格式化输出**

%d 整型数占位符

%f 浮点数占位符

%o 八进制无符号

%u 无符号占位符

%c 字符型占位符

%s 字符串占位符

%x 十六进制占位符

输出字符串用%s

%lf 双精度浮点型double



**格式化输入**

scanf(格式化字符串，参数。。。。)

一定要按照顺序输入



**printf字域宽度**



#include<stdio.h>
int main()
{
​    char a[]="liu";
​    char b[]="jing";
​    char c[]="yuan";


```c
printf("%5s%5s%5s",a,b,c);
return 0;
```
}