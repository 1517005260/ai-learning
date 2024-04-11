#!/usr/bin/env python3  
#指定解释器才可以被./执行
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

# 定义一个推理函数，来计算并返回准确率
def infer(model, dataset, device):
    model.eval() # 进入验证模式
    acc_num = 0  # 推理过程中验证正确的样本数量

    # 定义上下文管理器来约束模型不要改变参数
    # 验证的时候不用改变参数、计算梯度，训练的时候才要
    with torch.no_grad():   # with相当于conda，提供了临时的执行环境，执行完毕后清理
        for data in dataset:
            datas, label = data
            outputs = model(datas.to(device))   # 将数据送往设备，由模型处理后输出到output

            # 我们对三种花进行识别，输出模型认为概率最大的那个作为答案
            # torch.max函数返回一对元组：第一个是最大值，第二个是最大值的索引
            predict_y = torch.max(outputs, dim=1)[1]  # dim是维度的索引，一共两维。0维是batch_size，1维是结果维度
            # predict_y就是最大值的“下标”，像数组一样

            # 对正确数量累加
            # .eq()方法会返回true/false(1/0)
            # .sum()是因为每次我们会送入一批数据，我们要找到这批数据中所有正确的结果，即累加true(1)的数量，最后累加到acc_num里
            # .item()将torch的元素类型tensor转换为int类型
            acc_num += torch.eq(predict_y, label.to(device)).sum().item()
    
    acc = acc_num / len(dataset)
    return acc

# 搭建训练过程
def main(lr = 0.005, epochs = 20):  #传入学习率和学习轮数，这里给定了数值
    # 创建模型
    model = NN(4, 12, 6, 3).to(device)
    # 4个输入特征维度  
    # 12是超参，可以自行调整，看哪个效果好选哪个，这里进行了升维
    # 6进行了降维
    # 最后输出一定是3，因为我们只有3种花

    # 定义损失函数，这里我们选用CrossEntropyLoss 交叉熵函数
    loss_function = nn.CrossEntropyLoss() 

    # 定义参数(w,b)
    # 找到模型中所有可以梯度下降（所有可以因训练而改变）的参数
    pg = [p for p in model.parameters() if p.requires_grad]

    optimizer = optim.Adam(pg, lr=lr)  # 优化器，采用了Adam算法

    # 定义训练完的模型（模型权重）的存储路径
    save_path = os.path.join(os.getcwd(), "results/weights")  # 存储在 ./results/weights
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    
    # 开始训练
    for epoch in range(epochs):
        model.train()   # 设置为训练模式
        acc_num = torch.zeros(1).to(device)   # 初始化为一维标量0
        sample_num = 0  # 已经训练的样本数

        # tqdm封装进度条
        train_bar = tqdm(train_loader, file=sys.stdout, ncols=100)  # 以stdout方式、宽度为100地打印train_loader长度

        # 循环数据集
        for datas in train_bar:
            data, label = datas
            label = label.squeeze(-1)  # 上保险以预防我们不想要的多余标签内容,避免了由于数据格式不一致而可能引起的问题
            sample_num += data.shape[0] #shape第0维是批大小，其他维是特征

            optimizer.zero_grad()  # 梯度清零，初始化

            outputs = model(data.to(device))
            predict_class = torch.max(outputs, dim=1)[1]
            acc_num += torch.eq(predict_class, label.to(device)).sum()  # 这里不用.item()是因为acc_num一开始就被初始化为torch的数据类型tensor

            loss = loss_function(outputs, label.to(device))
            loss.backward()  # 求导
            optimizer.step() # 梯度下降

            train_acc = acc_num / sample_num
            # 加到进度条上
            train_bar.desc = "train epoch[{}/{}]  loss:{:.3f}".format(epoch + 1, epochs, loss)
        
        # 每轮学习完验证一下正确率
        val_acc = infer(model, val_loader,device)
        print("train epoch[{}/{}]  loss:{:.3f}  val_acc:{:.3f}".format(epoch + 1, epochs, loss, val_acc))

        # 验证完改下参数并保存
        torch.save(model.state_dict(), os.path.join(save_path, "nn.pth"))

        # 每轮训练完后重置数据
        train_acc = 0
        val_acc = 0
    
    print("Finished Training!")

    # 测试
    test_acc = infer(model, test_loader, device)
    print("test_acc:",test_acc)


if __name__ == "__main__":
    main()