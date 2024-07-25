## 数组

创建 numpy array 对象

直接传列表：

```bash
C:\Users\15170>python
Python 3.11.5 | packaged by Anaconda, Inc. | (main, Sep 11 2023, 13:26:23) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import numpy as np
>>> arr = np.array([1,2,3,4,5])
>>> print(arr)
[1 2 3 4 5]
>>> print(type(arr))
<class 'numpy.ndarray'>
```

or：传元组：

```bash
>>> arr = np.array((1,2,3,4,5))
>>> print(arr)
[1 2 3 4 5]
>>> type(arr)
<class 'numpy.ndarray'>
```

## 维度

n 维：创建时 n 重括号

0 维数组：

```bash
>>> arr = np.array(66)
>>> print(arr)
66
>>> arr.ndim
0
```

1 维：

```bash
>>> arr = np.array([1,2,3])
>>> print(arr)
[1 2 3]
>>> arr.ndim
1
```

2 维：

```bash
>>> arr = np.array([[1,2,3],[4,5,6]])
>>> print(arr)
[[1 2 3]
 [4 5 6]]
>>> arr.ndim
2
```

3 维：

```bash
>>> arr = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
>>> print(arr)
[[[1 2 3]
  [4 5 6]]

 [[1 2 3]
  [4 5 6]]]
>>> arr.ndim
3
```

更高维：

```bash
>>> arr = np.array([1,2,3,4,5],ndmin=5)
>>> print(arr)
[[[[[1 2 3 4 5]]]]]
>>> arr.ndim
5
```

## 索引

访问一维数组元素：

```bash
>>> arr = np.array([1,2,3,4])
>>> print(arr[2])
3
>>> arr[1] + arr[2]
5
```

二维：

```bash
>>> arr = np.array([[1,2,3],[4,5,6]])
>>> arr[0,1]
2
>>> arr[1,2]
6
```

三维：

```bash
>>> arr = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
>>> arr[0,0,0]
1
>>> arr[1,1,1]
5
```

### 负索引：从后往前找

例子：

```bash
>>> arr = np.array([[1,2,3],[4,5,6]])
>>> arr[1,-1]
6
```

## 裁剪数组

[start : end : step]

start 闭 end 开

```bash
>>> arr = np.array([1,2,3,4,5])
>>> arr[0:2]
array([1, 2])
>>> arr[0:]
array([1, 2, 3, 4, 5])
>>> arr[:3]
array([1, 2, 3])
>>> arr[::2]
array([1, 3, 5])
```

负裁剪

```bash
>>> arr[::-1]
array([5, 4, 3, 2, 1])
>>> arr[-3:-1]
array([3, 4])
```

二维数组裁剪

```bash
>>> arr = np.array([[1,2,3],[4,5,6]])
>>> print(arr)
[[1 2 3]
 [4 5 6]]
>>> arr[0,0:2]
array([1, 2])
>>> arr[0:2,2]
array([3, 6])
>>> arr[0:2,1:3]
array([[2, 3],
       [5, 6]])
>>> arr[::-1]
array([[4, 5, 6],
       [1, 2, 3]])
>>> arr[::,::-1]
array([[3, 2, 1],
       [6, 5, 4]])
```
