# Natural Language Processing using Python

# Introduction to numpy
# Importing Libraries
import numpy as np

# arange()
# np.arange([start,] stop[, step,], dtype=None)
np.arange(10)

np.arange(1,10)

np.arange(1,10,2)
np.arange(1,10,0.5)

np.arange(1,10,dtype='float64')

# Examining the ndarray
arr = np.arange(1,10)

arr.ndim

arr.shape

arr.size
arr.dtype
arr.itemsize

# Memory Usage
arr.itemsize * arr.size

# Why use Numpy? Compare the time to do the same operation using
# numpy and normal python lists
# %timeit list1 = range(1,1000)
# %timeit list2 = np.arange(1,1000)


# Important functions in numpy
# List to array
np.asarray([1,2,3,4,5])

list2d = [[1,2,3],[4,5,6]]
arr2d = np.asarray(list2d)

# Generate zeros
# zeros(shape, dtype=float, order='C')

listzeros = np.zeros((3,4), dtype='int32')

# Linspace
# np.linspace(start, stop, num=50, endpoint=True, retstep=False)

np.linspace(1,4,num=4)
np.linspace(1,4,num=8)
np.linspace(1,4,num=8,endpoint=False)

# Random generation
np.random.random((3,4))

# Max, min, mean, median, std etc
# np.max(a, axis=None, out=None, keepdims=False)
# np.min(a, axis=None, out=None, keepdims=False)
# np.mean(a, axis=None, dtype=None, out=None, keepdims=False)
# np.median(a, axis=None, out=None, overwrite_input=False)
# np.std(a, axis=None, dtype=None, out=None, ddof=0, keepdims=False)
# np.sum(a, axis=None, dtype=None, out=None, keepdims=False)

rarr = np.random.random((3,4))

np.max(rarr, axis=0)
np.max(rarr, axis=1)

np.min(rarr, axis=0)
np.min(rarr, axis=1)

np.median(rarr, axis=0)
np.median(rarr, axis=1)

# Reshaping
# np.reshape(a, newshape, order='C')
new_rarr = np.reshape(rarr, (12,))
new_rarr = np.reshape(rarr, (12,1))

# Slicing
rarr = np.random.random((4,5))

rarr[:,:]
rarr[1:3,:]

rarr[:,1:]
rarr[:,1:3]

rarr[1:3,1:3]

rarr[[0,3],:]
rarr[:,[0,3]]


rarr[:-1,:]
rarr[-1:,:]