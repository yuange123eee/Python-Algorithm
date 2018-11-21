```c
#include<stdio.h>      //头文件    stdio标准的输入输出流
int main()             //主函数 
{
    printf("hello world!");   //输出 字符串用""括起来
    return 0;   
}










```

```c
//解题方式
1.
#include<stdio.h>
int main()
{
    int t,a,b;
    scanf("%d",&t);
    while(t--){
        scanf("%d %d",&a,&b);
        printf("%d\n",a+b);    
    }  
    return 0;
}
//输入t表示有t组，利用while循环来输入多组//
2.
#include<stdio.h>
int main()
{
    while(scanf("%d %d",&a,&b)!=EOF){
        printf("%d\n",a+b);
        
        
        
    }
    return 0；
}
//scanf("%d %d",&a,&b)！=EOF如果输入为真，那么继续输入。如果输入为假，那么结束循环
//未知输入的组数

3.
#include<stdio.h>
int main()
{
    int a,b;
    while(scanf("%d",&a)&&a!=0){
        scanf("%d",&b);
        printf("%d\n",a+b);
      
    }
    
    
    return 0;
}
//当a输入为0的时候结束


```

