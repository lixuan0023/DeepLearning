<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=default"></script>

#”逆传播”算法的工作机制
Reference:  
>* [tensorfly.cn](http://www.tensorfly.cn/home/?p=76)
>* [Neural network and deep learning](https://github.com/mnielsen/neural-networks-and-deep-learning)

给出一小批训练样本\\(m\\)，下面算法将基于小批训练样本进行梯度下降学习步骤：

1. **输入训练样本集合**
2. **对于每一个训练样本 \\(x\\)**
	* **向前：**
		对于每一层\\(l = 2, 3, \ldots, L\\)计算 \\(z^{x,l} = w^l a^{x,l-1}+b^l\\)和 \\(a^{x,l} = \sigma(z^{x,l})\\)。
	* **输出层误差 \\(\delta^{x,L}\\):** 
	 	计算向量\\(\delta^{x,L} = \nabla_a C_x \odot \sigma'(z^{x,L})\\)。
	* **后向传播误差：**
		对于每一层\\(l = L-1, L-2, \ldots, 2\\)计算\\(\delta^{x,l} = ((w^{l+1})^T \delta^{x,l+1}) \odot \sigma'(z^{x,l})\\)。
3. **梯度下降：**
	对于每一层\\(l = L, L-1, \ldots, 2\\)，按照规则\\(w^l \rightarrow w^l-\frac{\eta}{m} \sum_x \delta^{x,l} (a^{x,l-1})^T\\)更新权重，按照规则\\(b^l \rightarrow b^l-\frac{\eta}{m} \sum_x \delta^{x,l}\\)更新偏差。