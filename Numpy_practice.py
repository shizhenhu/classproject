print("test the functions of Numpy")
import numpy as np
array = np.array([1, 4, 5, 8], float)
print(array)
print ("")
array = np.array([[1, 2, 3], [4, 5, 6]], float)  # a 2D array/Matrix
print (array)

# to see array indexing and slicing in action
print("the indexing of Numpy matrix")
array = np.array([1, 4, 5, 8], float)
print(array)
print ("")
print(array[1])
print ("")
print (array[:2])
print ("")
array[1] = 5.0
print (array[1])
print (array)

# Change False to True to see Matrix indexing and slicing in action

two_D_array = np.array([[1, 2, 3], [4, 5, 6]], float)
print (two_D_array)
print ("")
print (two_D_array[1][1])
print ("")
print (two_D_array[1, :])
print ("")
print (two_D_array[:, 2])

'''
Here are some arithmetic operations that you can do with Numpy arrays
'''
# Change False to True to see Array arithmetics in action

array_1 = np.array([1, 2, 3], float)
array_2 = np.array([5, 2, 6], float)
print (array_1 + array_2)
print ("")
print (array_1 - array_2)
print ("")
print (array_1 * array_2)

# Change False to True to see Matrix arithmetics in action
array_1 = np.array([[1, 2], [3, 4]], float)
array_2 = np.array([[5, 6], [7, 8]], float)
print (array_1 + array_2)
print ("")
print (array_1 - array_2)
print ("")
print (array_1 * array_2)

'''
In addition to the standard arthimetic operations, Numpy also has a range of
other mathematical operations that you can apply to Numpy arrays, such as
mean and dot product.

Both of these functions will be useful in later programming quizzes.
'''
array_1 = np.array([1, 2, 3], float)
array_2 = np.array([[6], [7], [8]], float)
print (np.mean(array_1))
print (np.mean(array_2))
print ("")
print (np.dot(array_1, array_2))
