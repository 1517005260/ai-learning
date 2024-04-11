from torch.utils.data import Dataset
import os  # 操作文件路径
import pandas as pd  #处理输入数据
import numpy as np   #数据类型转换
import torch

class iris_dataloader(Dataset):
    #继承自父类Dataset，要求重写三个方法：init，get_item,len
    def __init__(self, data_path):
        # 初始化数据路径，以及加载数据
        self.data_path = data_path

        assert os.path.exists(self.data_path), "dataset does not exist"  # 判断数据集是否存在，不存在报异常

        df = pd.read_csv(self.data_path, names=[0, 1, 2, 3, 4])   #读取数据，并用df保存。数据中有5列，这里我们简单起名0 1 2 3 4

        # 神经网络是数学模型，我们需要定义数据集中非数字和数字的映射，然后更换数据集中的非数字
        d = {"Iris-setosa":0, "Iris-versicolor":1, "Iris-virginica":2}
        df[4] = df[4].map(d)  # 用map映射将key替换为value

        #加载数据和真值
        data = df.iloc[ : , 0:4]   #数据就是前四列。 其中iloc函数传两个参数行+列，这里是全部行和前四列
        label = df.iloc[ : , 4:]   #真值就是第五列

        # 数据归一化  Z值化
        data = (data - np.mean(data)) / np.std(data)  # 减去均值 除以标准差 => 令数据变成均值为0，方差为1的数据

        # 接下来要转换数据类型。pandas的默认数据类型是dataform，不能被torch的tensor识别
        self.data = torch.from_numpy(np.array(data, dtype="float32"))
        self.label = torch.from_numpy(np.array(label, dtype="int64"))

        # 统计数据集的数据数量
        self.data_num = len(label)
        print("当前数据集大小：%d\n" % self.data_num)
    
    def __len__(self):
        # 数据集大小
        return self.data_num
        #知道数据集大小，pytorch才能分批处理数据   类比malloc

    def __getitem__(self, index):   #index是样本的索引（下标）
        #获取数据集的数据样本
        self.data = list(self.data)
        self.label = list(self.label)  #数组封装能快速通过下标获得数据样本

        return self.data[index], self.label[index]  #由于index都相同，所以获得的数据和真值肯定一一对应