# 数组操作

[迭代](#迭代)、[连接](#连接)、[拆分](#拆分)、[搜索](#搜索)、[排序](#排序)、[过滤](#过滤)

## 迭代

即遍历

一维：

```bash
>>> import numpy as np
>>> arr = np.array([1,2,3])
>>> for x in arr:
...     print(x)
...
1
2
3
```

二维：

```bash
>>> arr = np.array([[1,2,3],[4,5,6]])
>>> for x in arr:
...     print(x)
...
[1 2 3]
[4 5 6]
>>> for x in arr:
...     for y in x:
...             print(y)
...
1
2
3
4
5
6
```

三维：

```bash
>>> arr = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
>>> for x in arr:
...     for y in x:
...             for z in y:
...                     print(z)
...
1
2
3
4
5
6
1
2
3
4
5
6
```

简便方法：

```bash
>>> arr = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
>>> for x in np.nditer(arr):
...     print(x)
...
1
2
3
4
5
6
1
2
3
4
5
6
```

迭代不同数据类型的数组：

```bash
>>> arr = np.array([1,2,3]) # 整型
>>> for x in np.nditer(arr, flags=["buffered"], op_dtypes=["S"]):  # 转换成字符，numpy 需要额外空间 buffer 来进行这个转换
...     print(x)
...
b'1'
b'2'
b'3'
```

迭代步长：

```bash
>>> arr = np.array([[1,2,3,4],[5,6,7,8]])
>>> for x in np.nditer(arr[::, ::2]): # 取出所有行，列步长2
...     print(x)
...
1
3
5
7
```

有索引的迭代：

```bash
>>> arr = np.array([1,2,3])
>>> for idx, x in np.ndenumerate(arr):
...     print(idx, x)
...
(0,) 1
(1,) 2
(2,) 3

>>> arr = np.array([[1,2,3,4],[5,6,7,8]])
>>> for idx, x in np.ndenumerate(arr):
...     print(idx, x)
...
(0, 0) 1
(0, 1) 2
(0, 2) 3
(0, 3) 4
(1, 0) 5
(1, 1) 6
(1, 2) 7
(1, 3) 8
```

## 连接

基本连接操作：

```bash
>>> arr1 = np.array([[1,2],[3,4]])
>>> arr2 = np.array([[5,6], [7,8]])
>>> arr1
array([[1, 2],
       [3, 4]])
>>> arr2
array([[5, 6],
       [7, 8]])
>>> arr = np.concatenate((arr1, arr2))
>>> print(arr, arr.shape)
[[1 2]
 [3 4]
 [5 6]
 [7 8]] (4, 2)
>>> arr = np.concatenate((arr1, arr2), axis=1)
>>> print(arr, arr.shape)
[[1 2 5 6]
 [3 4 7 8]] (2, 4)
```

堆栈连接操作：

```bash
>>> arr = np.stack((arr1, arr2), axis=0)
>>> print(arr,arr.shape)
[[[1 2]
  [3 4]]

 [[5 6]
  [7 8]]] (2, 2, 2)
>>> arr = np.stack((arr1, arr2),axis=1)
>>> print(arr, arr.shape)
[[[1 2]
  [5 6]]

 [[3 4]
  [7 8]]] (2, 2, 2)
```

堆叠操作——和基本连接操作等价：

```bash
>>> arr = np.vstack((arr1, arr2)) # 按列堆叠
>>> print(arr, arr.shape)
[[1 2]
 [3 4]
 [5 6]
 [7 8]] (4, 2)
>>> arr = np.hstack((arr1, arr2)) # 按行堆叠
>>> print(arr, arr.shape)
[[1 2 5 6]
 [3 4 7 8]] (2, 4)
```

按高度（深度堆叠）

```bash
>>> arr = np.dstack((arr1, arr2))
>>> print(arr, arr.shape)
[[[1 5]
  [2 6]]

 [[3 7]
  [4 8]]] (2, 2, 2)
```

## 拆分

连接的逆操作

array_split 支持任意拆分；split 不支持不够的拆分

```bash
>>> arr =np.array([1,2,3,4,5,6,7,8])
>>> newarr = np.array_split(arr,4)
>>> newarr
[array([1, 2]), array([3, 4]), array([5, 6]), array([7, 8])]

>>> newarr = np.array_split(arr,5)
>>> newarr
[array([1, 2]), array([3, 4]), array([5, 6]), array([7]), array([8])]

>>> newarr = np.array_split(arr,9) # array_split 支持任意拆分
>>> newarr
[array([1]), array([2]), array([3]), array([4]), array([5]), array([6]), array([7]), array([8]), array([], dtype=int32)]

>>> newarr = np.split(arr, 8)
>>> newarr
[array([1]), array([2]), array([3]), array([4]), array([5]), array([6]), array([7]), array([8])]

>>> newarr = np.split(arr, 9)  # split 不支持不够的拆分
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<__array_function__ internals>", line 200, in split
  File "D:\anaconda\Lib\site-packages\numpy\lib\shape_base.py", line 872, in split
    raise ValueError(
ValueError: array split does not result in an equal division
```

分割二维数组

```bash
>>> arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
>>> newarr = np.array_split(arr,3)
>>> newarr
[array([[1, 2, 3]]), array([[4, 5, 6]]), array([[7, 8, 9]])]

>>> newarr = np.array_split(arr,4)
>>> newarr
[array([[1, 2, 3]]), array([[4, 5, 6]]), array([[7, 8, 9]]), array([], shape=(0, 3), dtype=int32)]

>>> newarr = np.array_split(arr,3,axis=1)
>>> newarr
[array([[1],
       [4],
       [7]]), array([[2],
       [5],
       [8]]), array([[3],
       [6],
       [9]])]

>>> newarr = np.hsplit(arr,3) # 与 hstack 对应
>>> newarr
[array([[1],
       [4],
       [7]]), array([[2],
       [5],
       [8]]), array([[3],
       [6],
       [9]])]
```

## 搜索

搜索数组的值：

```bash
>>> arr = np.array([1,2,3,4])
>>> x = np.where(arr == 4)
>>> x
(array([3], dtype=int64),)
```

搜索排序（插入）:

- left: a[i-1] < x <= a[i]
- right: a[i-1] <= x < a[i]

```bash
>>> arr = np.array([6,8,10,12])
>>> x = np.searchsorted(arr,10) # 我要把10插入到有序的arr中
>>> x # 插完后的下标
2
>>> x = np.searchsorted(arr,11)
>>> x
3
>>> x = np.searchsorted(arr,8, side="right")
>>> x
2
```

插入多个值：

```bash
>>> arr = np.array([1,3,5,7])
>>> x = np.searchsorted(arr,[2,4,6])
>>> x
array([1, 2, 3], dtype=int64)

'''
结果解释：类比“放回”的概率论问题。我们单独看这几个要插入的数。2要插在1，3之间，所以下标为2。4要插在3,5之间，此时我们不管之前的2，所以下标为2。
'''
```

## 排序

一维数组排序：

```bash
>>> arr = np.array([3,2,0,1])
>>> np.sort(arr)
array([0, 1, 2, 3])

>>> arr = np.array(['b','a','c'])
>>> np.sort(arr)
array(['a', 'b', 'c'], dtype='<U1')
```

二维数组排序：

```bash
>>> arr = np.array([[3,5,1],[2,5,1]])
>>> np.sort(arr)
array([[1, 3, 5],
       [1, 2, 5]])
```

## 过滤

bool 索引过滤：

```bash
>>> arr = np.array([1,2,3,4])
>>> x = [True,True,False,True]
>>> newarr = arr[x]
>>> newarr
array([1, 2, 4])
```

创建过滤器数组：

```python
import numpy as np

arr = np.array([1,2,3,4])
filter_array = []

for x in arr:
    if x > 2:
        filter_array.append(True)
    else:
        filter_array.append(False)

newarr = arr[filter_array]

print(newarr)

# 结果：[3 4]
```

简便方法：

```python
import numpy as np

arr = np.array([1,2,3,4])
filter_array = arr > 2

newarr = arr[filter_array]

print(newarr)
```
