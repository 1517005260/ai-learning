# 数据类型

int32:32 位整数

U：Unicode 字符。U1：1 位字符

```bash
C:\Users\15170>python
Python 3.11.5 | packaged by Anaconda, Inc. | (main, Sep 11 2023, 13:26:23) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import numpy as np
>>> arr = np.array([1,2,3])
>>> arr.dtype
dtype('int32')
>>> arr = np.array(['a','b','c'])
>>> arr.dtype
dtype('<U1')
```

创建数组时转换：int -> String

```bash
>>> arr = np.array([1,2,3,4],dtype='S')
>>> arr.dtype
dtype('S1')
```

无法转换：'a'无法转换成整数

```bash
>>> arr = np.array(['a','2','3'],dtype = 'i')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'a'
```

手动转换：

```bash
>>> arr = np.array([1.1,2.2,3.3])
>>> newarr = arr.astype('i')
>>> print(newarr)
[1 2 3]
>>> newarr.dtype
dtype('int32')

或者

>>> arr = np.array([1.1,2.2,3.3])
>>> newarr = arr.astype(int)
>>> print(newarr)
[1 2 3]
>>> newarr.dtype
dtype('int32')

>>> arr = np.array([1,0,3])
>>> newarr = arr.astype(bool)
>>> newarr
array([ True, False,  True])
>>> newarr.dtype
dtype('bool')
```

# 副本与视图

- 副本：原数组的备份，有数据。副本和原数据独立。
- 视图：原数组的指针，无数据。修改视图会变动原数据，修改原数据也会更改视图。

副本：

```bash
>>> arr = np.array([1,2,3,4,5])
>>> newarr = arr.copy()
>>> arr[0] = 61
>>> arr
array([61,  2,  3,  4,  5])
>>> newarr
array([1, 2, 3, 4, 5])
```

视图：

```bash
>>> arr = np.array([1,2,3,4,5])
>>> newarr = arr.view()
>>> arr[0]=61
>>> arr
array([61,  2,  3,  4,  5])
>>> newarr
array([61,  2,  3,  4,  5])
>>> newarr[1]=0
>>> newarr
array([61,  0,  3,  4,  5])
>>> arr
array([61,  0,  3,  4,  5])
```

检查一个对象是否拥有数据：看 base 属性是否有值。base 为空则说明对象有数据，因为 base 是引用了原对象的数据。如下代码，x 没有引用对象，所以 base 为空；y 引用了 arr，所以 base 为 arr。

```bash
>>> arr = np.array([1,2,3,4,5])
>>> x = arr.copy()
>>> y = arr.view()
>>> x.base
>>> y.base
array([1, 2, 3, 4, 5])
>>> arr.base
>>>
```
