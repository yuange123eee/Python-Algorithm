python **try except**

 try:

​      Normal execution block

 except A:

​      Exception A handle

except B:

​     Exception B handle

except:

​     Other exception handle

 else:

​      if no exception,get here

 finally:

​      print("finally")   

>  说明：
>
>  正常执行的程序在try下面的Normal execution block执行块中执行，在执行过程中如果发生了异常，则**中断当前在Normal execution block中的执行**，跳转到对应的异常处理块中开始执行；
>
>  python**从第一个except X处开始查找**，如果找到了对应的exception类型则进入其提供的exception handle中进行处理，如果没有找到则直接进入except块处进行处理。except块是可选项，如果没有提供，该exception将会被提交给python进行默认处理，处理方式则是**终止应用程序并打印提示信息**；
>
>  如果在Normal execution block执行块中执行过程中没有发生任何异常，则在执行完Normal execution block后会进入else执行块中（如果存在的话）执行。