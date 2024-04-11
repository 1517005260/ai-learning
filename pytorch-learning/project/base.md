# 实战  -- 鸢尾花分类

## 大致解决方案
1. 自定义数据集加载，加载鸢尾花数据集，并将其划分为训练集和测试集。

2. `nn.Module`构造神经网络模型，对于这个问题，可以使用一个简单的多层感知器`MLP`模型。在输出层，可以使用`Softmax`激活函数将输出转换为概率分布。

3. 模型训练  
- 选择一个适当的损失函数，例如交叉嫡损失`Cross-Entropy Loss`，用于衡量模型预测与实际标签之间的差异。
- 选择一个优化算法，例如随机梯度下降`SGD`或`Adam`等，用于更新神经网络的权重以最小化损失函数。
- 设置训练参数，如批量大小`Batch Size`、学习率`Learning Rate`和训练轮数`Epochs`等。
- 使用训练集数据进行训练，不断更新神经网络权重以最小化损失。

4. 模型评估
- 使用测试集数据对训练好的神经网络模型进行评估，计算分类准确率等指标。
- 如果性能不佳，可以尝试调整神经网络结构（如增加隐藏层节点数）、优化算法（如调整学习率）或训练参数（如增加训练轮数）等，以提高模型性能。

5. 使用训练好的神经网络模型对新的鸢尾花数据进行分类预测。

## 详细步骤
1. 写脚本`data_loader.py`加载数据
- 详见代码注释
- `Z值化`[相关知识](https://www.zhihu.com/question/20107280/answer/1741114532)  => 本质就是对某一原始分值进行转换，变成的一个标准分值，该标准分值可使得原来无法比较的数值变得可比

2. 使用`nn.py`构建模型
- 详见代码注释
- 有关`batch_size`: 数据集的加载并不是一股脑的，因为可能太大了，超过了硬件处理负载上限<br>
  因此，我们选择批量运送数据，如`batch_size = 16` 说明一次训练16条数据

3. 训练结果（其中某次）：
- 造成每次准确结果不同的原因：验证集和测试集太少了，不能完整反应模型性能  ||  每次训练开始的随机数不一样，起点也不一样
``` bash
(base) glk@ggg:~/project/pytorch-learning/project$ ./nn.py 
/home/glk/project/anaconda3/lib/python3.11/site-packages/numpy/core/fromnumeric.py:3643: FutureWarning: The behavior of DataFrame.std with axis=None is deprecated, in a future version this will reduce over both axes and return a scalar. To retain the old behavior, pass axis=0 (or do not pass axis)
  return std(axis=axis, dtype=dtype, out=out, ddof=ddof, **kwargs)
当前数据集大小：150

训练集大小:105
验证集大小30
测试集大小15

train epoch[1/20]  loss:0.960: 100%|██████████████████████████████████| 7/7 [00:00<00:00, 37.75it/s]
train epoch[1/20]  loss:0.960  val_acc:0.867
train epoch[2/20]  loss:0.809: 100%|█████████████████████████████████| 7/7 [00:00<00:00, 503.18it/s]
train epoch[2/20]  loss:0.809  val_acc:0.833
train epoch[3/20]  loss:0.644: 100%|█████████████████████████████████| 7/7 [00:00<00:00, 514.36it/s]
train epoch[3/20]  loss:0.644  val_acc:0.900
train epoch[4/20]  loss:0.731: 100%|█████████████████████████████████| 7/7 [00:00<00:00, 586.72it/s]
train epoch[4/20]  loss:0.731  val_acc:0.867
train epoch[5/20]  loss:0.590: 100%|█████████████████████████████████| 7/7 [00:00<00:00, 554.33it/s]
train epoch[5/20]  loss:0.590  val_acc:0.900
train epoch[6/20]  loss:0.490: 100%|█████████████████████████████████| 7/7 [00:00<00:00, 422.51it/s]
train epoch[6/20]  loss:0.490  val_acc:0.933
train epoch[7/20]  loss:0.434: 100%|█████████████████████████████████| 7/7 [00:00<00:00, 413.70it/s]
train epoch[7/20]  loss:0.434  val_acc:0.933
train epoch[8/20]  loss:0.372: 100%|█████████████████████████████████| 7/7 [00:00<00:00, 537.94it/s]
train epoch[8/20]  loss:0.372  val_acc:0.933
train epoch[9/20]  loss:0.236: 100%|█████████████████████████████████| 7/7 [00:00<00:00, 480.49it/s]
train epoch[9/20]  loss:0.236  val_acc:0.933
train epoch[10/20]  loss:0.267: 100%|████████████████████████████████| 7/7 [00:00<00:00, 416.28it/s]
train epoch[10/20]  loss:0.267  val_acc:0.933
train epoch[11/20]  loss:0.139: 100%|████████████████████████████████| 7/7 [00:00<00:00, 543.30it/s]
train epoch[11/20]  loss:0.139  val_acc:0.933
train epoch[12/20]  loss:0.170: 100%|████████████████████████████████| 7/7 [00:00<00:00, 567.76it/s]
train epoch[12/20]  loss:0.170  val_acc:0.933
train epoch[13/20]  loss:0.059: 100%|████████████████████████████████| 7/7 [00:00<00:00, 528.08it/s]
train epoch[13/20]  loss:0.059  val_acc:0.933
train epoch[14/20]  loss:0.345: 100%|████████████████████████████████| 7/7 [00:00<00:00, 450.68it/s]
train epoch[14/20]  loss:0.345  val_acc:0.933
train epoch[15/20]  loss:0.179: 100%|████████████████████████████████| 7/7 [00:00<00:00, 395.61it/s]
train epoch[15/20]  loss:0.179  val_acc:0.933
train epoch[16/20]  loss:0.134: 100%|████████████████████████████████| 7/7 [00:00<00:00, 401.85it/s]
train epoch[16/20]  loss:0.134  val_acc:0.933
train epoch[17/20]  loss:0.073: 100%|████████████████████████████████| 7/7 [00:00<00:00, 505.75it/s]
train epoch[17/20]  loss:0.073  val_acc:0.933
train epoch[18/20]  loss:0.295: 100%|████████████████████████████████| 7/7 [00:00<00:00, 489.38it/s]
train epoch[18/20]  loss:0.295  val_acc:0.933
train epoch[19/20]  loss:0.155: 100%|████████████████████████████████| 7/7 [00:00<00:00, 451.74it/s]
train epoch[19/20]  loss:0.155  val_acc:0.933
train epoch[20/20]  loss:0.142: 100%|████████████████████████████████| 7/7 [00:00<00:00, 439.85it/s]
train epoch[20/20]  loss:0.142  val_acc:0.933
Finished Training!
test_acc: 0.9333333333333333
```