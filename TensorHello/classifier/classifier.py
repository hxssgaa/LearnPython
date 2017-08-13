import scipy.io
import matplotlib.pyplot as plt
import numpy as np

mat = scipy.io.loadmat('ex4data1.mat')
X, y = mat['X'], mat['y']
m = len(X)
# data = X[0]
# image_data = np.reshape(X[1], (20, 20))
# plt.imshow(image_data, cmap='gray_r')

mat = scipy.io.loadmat('ex4weights.mat')
nn_params = [mat['Theta1'], mat['Theta2']]


plt.show()
