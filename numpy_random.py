import numpy as np

np.random.seed(50)
arr_rand = np.random.randint(0, 100, 50)
matrix_array = arr_rand.reshape(10, 5)

# index of numpy
argmin = matrix_array.argmin()
margmfig = matrix_array.argmfig()


np_arr = np.ones((10, 10))*10

# arange number
arr_test = np.arange(0, 10)
p = arr_test.reshape((2, 5))
print(p)
