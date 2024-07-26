# Numpy

- 全称：Numerical Python 用于处理数组的 python 包
- numpy 中的数组比 python 自带的快 50 倍。因为在 numpy 中数组在内存是连续存储的`引用的位置性`--类比数据库的聚集存储
- numpy 中的数组，它的数据类型是 ndarray，和 python 自带的 list **不一样**
- numpy 部分是 python 写的，但大多数涉及快速计算的部分是 c++ 写的，[源码](https://github.com/numpy/numpy)

我的 numpy 版本：

```bash
C:\Users\15170>python
Python 3.11.5 | packaged by Anaconda, Inc. | (main, Sep 11 2023, 13:26:23) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import numpy
>>> print(numpy.__version__)
1.24.4
```

## 目录

[数组](./array.md)

[数据类型](./dataType.md)

[数组形状](./shape.md)

[数组操作](./operation.md)
