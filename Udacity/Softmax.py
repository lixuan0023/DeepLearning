import numpy as np
"""Softmax."""

scores = np.array([3.0, 1.0, 0.2])

def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    return np.exp(x)/np.sum(np.exp(x),axis=0)


print(softmax(scores))

# Plot softmax curves
import matplotlib.pyplot as plt
x = np.arange(-2.0, 6.0, 0.1)
scores = np.vstack([x, np.ones_like(x), 0.2 * np.ones_like(x)])
print(scores.shape)

stm = softmax(scores)
print(stm.shape)
print(x.shape,stm[:][0].shape)

fig, ax = plt.subplots()
ax.plot(x, stm[:][0], linewidth=2,label='x')
ax.plot(x, stm[:][1], linewidth=2,label='1')
ax.plot(x, stm[:][2], linewidth=2,label='0.2')

ax.legend(loc='best')
ax.set_xlabel('x')
ax.set_ylabel('softmax')
plt.show()
