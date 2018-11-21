**pop()**方法总是删掉list的最后一个元素，并且它还返回这个元素，所以我们执行 L.pop() 后，会打印出 'Paul'。

当首先删除索引为 2 的Paul时，L变成了：

['Adam', 'Lisa', 'Bart']

这时，注意到Bart的索引已经从原来的3变成2了！

**参考代码:**

```python
L = ['Adam', 'Lisa', 'Paul', 'Bart']
L.pop(3)
L.pop(2)
print L
```

***注意列表中元素时刻位置变化***

------

***4-8***     元组



包含 0 个元素的 tuple，也就是空tuple，直接用 ()表示：

```python
>>> t = ()
>>> print t
()
```

是因为用()定义单元素的tuple有歧义，所以 Python 规定，单元素 tuple 要多加一个逗号“,”，这样就避免了歧义：

```python
>>> t = (1,)
>>> print t
(1,)
```

**注意：元组中“，”是重点**

**前面我们看到了tuple一旦创建就不能修改**

------

***5-2***     **if语句**

细心的同学可以发现，这两种条件判断是“非此即彼”的，要么符合条件1，要么符合条件2，因此，完全可以用一个 if ... else ... 语句把它们统一起来：

```python
if age >= 18:
    print 'adult'
else:
    print 'teenager'
```

利用 if ... else ... 语句，我们可以根据条件表达式的值为 True 或者 False ，分别执行 if 代码块或者 else 代码块。

**注意:** **else 后面有个“:”**





------

***函数***

形式参数和实际参数

***break退出循环***

用for循环或者while循环时，如果要在循环体内直接退出循环，可以使用**break**语句。

***continue继续循环***

在循环过程中，可以用break退出当前循环，还可以用**continue**跳过后续循环代码，继续下一次循环

‘

global 是把局部变量变为全局变量，而nonlocal是把全局变量变成被授予函数引用

lamlda表达式

```python
def ds(x):
    return 2*x+1
ds(5)
lambda x:2*x+1










```

