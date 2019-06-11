import numpy as np
import cv2

arr = np.ones((5, 5))
print(arr*5/2)

np.random.seed(101)
rnd = np.random.randint(low=0, high=100, size=(5, 5))
print(rnd)
print("mfig num of array: ", rnd.mfig())
print("min num of array: ", rnd.min())
