# 数组形状

数组的形状：每个维度中元素的数量

```bash
>>> import numpy as np
>>> arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
>>> print(arr)
[[ 1  2  3  4  5]
 [ 6  7  8  9 10]]
>>> arr.shape
(2, 5)
```

上例是个两维数组，有 2 行 5 列

```bash
>>> arr = np.array([1,2,3,4,5],ndmin=5)
>>> print(arr)
[[[[[1 2 3 4 5]]]]]
>>> arr.shape
(1, 1, 1, 1, 5)
```

# 维度转换——重塑

1 维 -> 2 维

```bash
>>> arr = np.array([1,2,3,4,5,6])
>>> newarr = arr.reshape(2,3)
>>> arr
array([1, 2, 3, 4, 5, 6])
>>> newarr
array([[1, 2, 3],
       [4, 5, 6]])
>>> arr.shape
(6,)
>>> newarr.shape
(2, 3)
```

1 维 -> 3 维

```bash
>>> arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
>>> newarr = arr.reshape(2,3,2)
>>> arr
array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12])
>>> newarr
array([[[ 1,  2],
        [ 3,  4],
        [ 5,  6]],

       [[ 7,  8],
        [ 9, 10],
        [11, 12]]])
>>> arr.shape
(12,)
>>> newarr.shape
(2, 3, 2)
```

**注意**：维度不是随意转换的，必须前后维度乘积相等

错误案例：

```bash
>>> arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
>>> newarr = arr.reshape(3,3,3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: cannot reshape array of size 12 into shape (3,3,3)
```

reshape 返回的是视图，因为 base 非空

```bash
>>> arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
>>> newarr = arr.reshape(2,3,2)
>>> newarr.base
array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12])
```

numpy 还能自动计算维度，我们用-1 填充即可（但是只能有一个-1）：

```bash
>>> arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
>>> newarr = arr.reshape(2,2,-1)
>>> newarr.shape
(2, 2, 3)
>>> newarr
array([[[ 1,  2,  3],
        [ 4,  5,  6]],

       [[ 7,  8,  9],
        [10, 11, 12]]])
```

高维 -> 1 维：

```bash
>>> arr = np.array([[1,2,3],[4,5,6]])
>>> arr
array([[1, 2, 3],
       [4, 5, 6]])
>>> newarr = arr.reshape(-1)
>>> newarr
array([1, 2, 3, 4, 5, 6])
>>> newarr.shape
(6,)
```
