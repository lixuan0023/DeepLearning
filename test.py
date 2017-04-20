import numpy as np
alpha = 0.1  # 学习速率
input_dim = 2  # 因为我们是做两个数相加，每次会喂给神经网络两个bit，所以输入的维度是2
hidden_dim = 16  # 隐藏层的神经元节点数，远比理论值要大（译者注：理论上而言，应该一个节点就可以记住有无进位了，但我试了发现4的时候都没法收敛），你可以自己调整这个数，看看调大了是容易更快地收敛还是更慢
output_dim = 1

X = np.array([[0,1]])
synapse_0 = 2 * np.random.random((input_dim, hidden_dim)) - 1
y= np.zeros_like(synapse_0)+3
aa = np.dot(X, y)
print(aa)
print(aa.shape,X.shape)
aaa =  np.zeros(hidden_dim)
print(aaa)
