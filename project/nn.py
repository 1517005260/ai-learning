import sys
import os
from torch.utils.data import DataLoader  # 分批处理数据
from tqdm import tqdm # 在终端显示进度条
import torch
import torch.utils.data
import torch.nn as nn # 封装了很多神经网络的常用功能
import torch.optim as optim # 优化算法库，包括但不限于梯度下降算法

from data_loader import iris_dataloader

# 初始化神经网络模型
class NN(nn.Module):
    #传入输入层、隐藏层、输出层维度（个数）
    def __init__(self, in_dim, hidden_dim1, hidden_dim2, out_dim):
        super().__init__()
        #定义层级结构
        #给三个层级起名字
        self.layer1 = nn.Linear(in_dim, hidden_dim1)
        self.layer2 = nn.Linear(hidden_dim1, hidden_dim2)  #接收dim1个数据，输出dim2个数据
        self.layer3 = nn.Linear(hidden_dim2, out_dim)

    def forward(self, x): #接收数据后怎么处理
        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)  #逐一前向传播即可

        return x 


# 定义计算环境
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")  #三目运算符，如果cuda存在那么结果为gpu环境，否则为cpu环境

# 划分数据集 ： 训练集，验证集，测试集
# 类比          习题   考试    高考
# 即验证集可以做多次，测试集只能做一次。二者都可以反应性能，测试集更“权威”
custom_dataset = iris_dataloader("/home/glk/project/pytorch-learning/project/iris_data/iris_data.txt")
train_size = int(len(custom_dataset) * 0.7)  # 70%用于训练
val_size = int(len(custom_dataset) * 0.2)
test_size = len(custom_dataset) - train_size - val_size
# 按照上述比例随机切分
train_dataset, val_dataset, test_dataset = torch.utils.data.random_split(custom_dataset, [train_size, val_size, test_size])

# 加载数据按批量封装
train_loader = DataLoader(train_dataset,batch_size=16,shuffle=True)  #shuffle表示是否对剩下的数据做打乱处理以提高训练效率，增加数据稳健性
# 但是，如果数据过大，shuffle=True 会消耗过多资源，需要取舍
# loader 实际上就是批数量，len(train_loader) * 16 = train_size
val_loader = DataLoader(val_dataset,batch_size=1,shuffle=False)
test_loader = DataLoader(test_dataset,batch_size=1,shuffle=False)

print("训练集大小:%d\n验证集大小%d\n测试集大小%d\n" % (train_size, val_size, test_size))