import numpy as np
X = np.array([[0, 0, 1],
              [0, 1, 1],
              [1, 0, 1],
              [1, 1, 1]])

y = np.array([[0],
              [1],
              [1],
              [0]])


np.random.seed(1)
# randomly initialize our weights with mean 0
# np.random.random return random floats in the half-open interval [0,1.0)
# 2*[0,1.0)-1 ==>[-1.0,1.0) 
syn0 = 2 * np.random.random((3, 4)) - 1
syn1 = 2 * np.random.random((4, 1)) - 1

# Feed forward through layers 0, 1, and 2
l0 = X
# l1 = nonlin(np.dot(l0, syn0))
# l2 = nonlin(np.dot(l1, syn1))
