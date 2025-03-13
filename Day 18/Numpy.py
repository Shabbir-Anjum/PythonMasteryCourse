import numpy as np

# # Creating a 1D numpy array
# arr = np.array([1, 2, 3, 4, 5])
# print(arr)

# # Creating a 2D numpy array
# arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
# print('2nd element on 1st row: ', arr[1, 1])

# # Creating a 3D list (not numpy array) and accessing elements
# x = [[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]
# print(x[0][0][0])

# # Creating a 3D numpy array and accessing elements
# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# print(arr[0, 1, -1])  # Accessing last element of second row of first 2D array

# # Slicing arrays
# arr = np.array([1, 2, 3, 4, 5, 6, 7])
# print(arr[0:5])  # Slicing first 5 elements
# print(arr[0::5]) # Skipping 5 elements in each step
# print(arr[::2])  # Taking every second element
# print(arr[1:5:2])  # Taking every second element between index 1 and 5

# # Slicing 2D arrays
# print("Slicing 2D arrays")
# arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# print(arr[1, 1:4])  # Getting elements from index 1 to 4 in second row
# print(arr[0:2, 2])  # Getting the third column from both rows
# print(arr[0:2, 1:4])  # Getting subarray from both rows (columns 1 to 3)

# # Checking data type of an array
# arr = np.array(['apple', 'banana', 'cherry'])
# print(arr.dtype)

# # Creating arrays with specific data types
# arr = np.array([1, 2, 3, 4], dtype='S')  # String type
# print(arr)
# print(arr.dtype)

# arr = np.array([1, 2, 3, 4], dtype='i4')  # 4-byte integer type
# print(arr)
# print(arr.dtype)

# # Converting data types of an array
# arr = np.array([1.1, 2.1, 3.1])
# newarr = arr.astype('i')  # Converting float array to integer
# print(newarr)
# print(newarr.dtype)

# # Copy vs View example
# arr = np.array([1, 2, 3, 4, 5])
# x = arr.copy()
# arr[0] = 42
# print(arr)  # Modified original array
# print(x)  # Copy remains unchanged

# arrs = np.array([11, 12, 13, 14, 15])
# x = arrs.view()
# arrs[0] = 42
# print(arrs)  # Modified original array
# print(x)  # View also changes

# # Checking shape of an array
# arr = np.array([[1, 2, 3, 4,5], [5, 6, 7, 8,9]])
# print(arr.shape)

# # Creating arrays with specific dimensions
# arr = np.array([1, 2, 3, 4], ndmin=5)  # Creating a 5D array
# print(arr)
# print('shape of array :', arr.shape)

# # Reshaping arrays
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# newarr = arr.reshape(4, 3)  # Reshaping into 4x3
# print(newarr)

# a = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9],[10, 11, 12]])
# print(a.shape)  # Getting shape of the array

# # Checking if reshaped array is a view or copy
# arrss = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# print(arrss.reshape(2, 4).base)

# # Reshaping with -1 (automatically calculates dimension)
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8,9])
# print(len(arr))
# newarr = arr.reshape(3, 3,-1)
# print(newarr)

# # Flattening arrays
# arr = np.array([[1, 2, 3], [4, 5, 6],[1, 2, 3], [4, 5, 6]])
# newarr = arr.reshape(-1)
# print(newarr)

# # Iterating through arrays
# arrsss = np.array([[1, 2, 3], [4, 5, 6]])
# for x in arrsss:
#   print(x,"r")

# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# print(arr.shape)
# for x in arr:
#   print(x,'two')
#   for i in x:
#     print(i,'inner')

# # Concatenating arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
# arr = np.concatenate((arr1, arr2))
# print(arr)

# Stacking arrays
arr = np.stack((arr1, arr2), axis=1)
print(arr)

# Splitting arrays
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 6)
print(newarr)

# Searching for values
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x, 'l',arr[3])

# Filtering even numbers
ar = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(ar % 2 == 0)
print(x, 'even')

# Searching sorted array
arr = np.array([6, 7, 9,3])
x = np.searchsorted(arr, 3)
print(x)

# Sorting arrays
arr = np.array([3, 2, 0, 1])
print(np.sort(arr))

# Boolean indexing
arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr[x]
print(newarr)
