import numpy as np
c=42,42,44
arr = np.array(c)

print(arr)
arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr)

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arr)


a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)


arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)


arr = np.array([1, 2, 3, 4])

print(arr[0])


arr = np.array([1, 2, 3, 4])

print(arr[2] + arr[3])

e=[[1,2,3,4,5], [6,7,8,9,10]]
print(e[0][1])
arr = np.array(e)

print('2nd element on 1st row: ', arr[1, -1])


arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[0, 1, 2])