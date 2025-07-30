import numpy
list(zip((1,2,3,4),(5,6,7,8)))
dir(numpy)
import numpy as np
dir(np)
a=np.array([1,2,3,4,5,6,7,8])
dir(a)
a.size
a.shape=2,4
a
a.shape
a.reshape(2,2,2)
a.shape=2,2,2
a[0,:,:]
data=np.array(range(1,101)).reshape(2,10,5)
data
sum(data)
data[0,6,2]
data[0,2:7:2,0:3]
data[0:2,:,2:3]
data[1,5:8:2,:]
data[0:2,0:10:2,:]+data[0:2,0:10:2,:]

a=data[1,:,1:2]
a.shape
b=data[1,:,1]
b.shape

np.linspace(1,100,4)
np.zeros((2,6,6))
np.ones((2,6))+7
np.eye(5)
np.arange(1,100,3)
np.random.rand(2,3,3)
np.random.randn(2,10,4)
n=np.random.randint(1,100,20).reshape(5,4)
import array
dir(array)
n.sum()
n.sum(axis=1)
n
n.max()
n.argmax()
n

#1
np.zeros(10)
#2
np.ones(10)
#3
np.zeros(10)+5
#4
np.arange(10,51)
#5
np.arange(10,51,2)
#6
a=np.arange(0,9).reshape((3,3))
a
b=np.array(range(0,9))
b.shape=3,3
b
#7
np.eye(3,3)
#8
np.random.rand(1)
#9
np.random.randn(25)
#10
np.arange(0.01,1.01,0.01).reshape(10,10)
np.linspace(0.01,1.0,100).reshape(10,10)
#11
np.linspace(0,1,20)
#12
mat=np.arange(1,26).reshape(5,5)
mat
mat[2:5,1:5]
#13
mat[3,4]
#14
mat[0:3,1:2]
#15
mat[4,:]
#16
mat[3:5,:]
#17
mat.sum()
#18
mat.std()
#19
mat.sum(axis=0)

np.array([1,2,3])
arr=np.arange(1,11)
arr>4
arr[arr>4]

mat1=np.arange(1,26).reshape(5,5)
mat1
mat2=np.arange(26,51).reshape(5,5)
mat2
mat1+mat2
mat2-mat1
mat1**2
mat1**3
mat2**2
mat2**3
mat1.sum()
mat1.sum(axis=0)
mat2.sum(axis=1)
np.sqrt(mat1)
np.sqrt(mat2)
mat1=np.arange(1,101).reshape(4,5,5)
mat1
mat1.sum(axis=1)
mat1.sum(axis=0)

# Create a NumPy array of 10 zeros and then replace the fifth element with 1.
zero_array=np.zeros(10)
zero_array[4]=1
zero_array

# Create a 6x6 matrix and fill the border with 1s, and the rest with 0s.
z_mat=np.zeros((6,6))
z_mat[:,0:6:5]=1
z_mat

# Given a 1D array, replace all values greater than 10 with 10.
arr=np.arange(21)
arr[arr>10]=10
arr

# Create a 3x3 matrix with values from 1 to 9 and flatten it to a 1D array.
a=np.arange(1,10).reshape(3,3)
a.flatten()

# Generate a 3x3 random matrix and compute the sum of each row and column.
a=np.random.randint(1,100,9).reshape(3,3)
a.sum(axis=0)
a.sum(axis=1)

# Normalize a random 1D array (scale values between 0 and 1).
a=np.random.rand(10)
a

# Sort a NumPy array along the columns.
a=np.array([20,4,1,2,50,6,76,45,65]).reshape(3,3)
a
a.sort(axis=0)
a

arr2d = np.zeros((5,4))
arr2d
arr_length = arr2d.shape[0]
arr_length
for i in range(arr_length):
    arr2d[i]=i
arr2d

arr2d = np.zeros((5,4))
arr2d
arr_length = arr2d.shape[1]
arr_length
for i in range(arr_length):
    arr2d[:,i]=i
arr2d

np.__version__
dir(np)
id(np)

