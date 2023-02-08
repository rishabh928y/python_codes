from numpy import *

# arr = array([1,2,3,2,5, 4], int)

# print(arr)
# arr = array([1,2,3,4,5], float)
# arr = linspace(0, 15,20)
# arr = arange(1,15,2)
# arr =  logspace(1,40,5)
# print('%.2f' %arr[4])

# arr = ones(5,int)

# # print(arr.dtype)
# # print(arr)

# arr1 = array([1,2,3,4,5])
# arr2 = array([6,1,9,3,2])

# arr1 = arr1+5

# arr3 = arr1 + arr2

# print(arr3)
# print(log(arr3))
# print(concatenate([arr1,arr2]))

# arr1 = array([2,6,8,1,3])

# arr2 = arr1.view()      #shallow copy

# arr2 = arr1.copy()      #deep copy

# print(id(arr1))
# print(id(arr2))

arr1 = array([ [1,2,3,6,2,9]  ,  [4,5,6,7,5,3]  ])
# print(arr1.ndim)       #gives number of dimensions
# print(arr1.shape)      #gives the number of rows and coloumns

# arr2 = arr1.flatten()

# arr3 = arr2.reshape(2,2,3)

# print(arr2)
# print(arr3) 

# m = matrix('1 2 ; 3 6 ; 4 5 ; 6 7')

# print(m)
# print(diagonal(m))
# print(m.max())
# print(m.min())

m1 = matrix('1 2 3 ; 6 4 5 ; 1 6 7')
m2 = matrix('1 2 3 ; 6 8 5 ; 2 6 7')

m3 = m1*m2

print(m3)
