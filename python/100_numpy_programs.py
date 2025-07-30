# 1. Import the numpy package under the name `np` (★☆☆)
import numpy as np

# 2. Print the numpy version and the configuration (★☆☆)
np.__version__
np.show_config()

# 3. Create a null vector of size 10 (★☆☆)
null_vector=np.zeros(10)

# 4. How to find the memory size of any array (★☆☆)
id(null_vector)
null_vector.size
null_vector.itemsize

# 5. How to get the documentation of the numpy add function from the command line? (★☆☆)
np.add.__doc__
np.info(np.add)

# 6. Create a null vector of size 10 but the fifth value which is 1 (★☆☆)
null_vector=np.zeros(10)
null_vector[4]=1
null_vector

# 7. Create a vector with values ranging from 10 to 49 (★☆☆)
array7=np.arange(10,50)

# 8. Reverse a vector (first element becomes last) (★☆☆)
length=array7.shape[0]
length
temp=array7[length-1]
array7[length-1]=array7[0]
array7[0]=temp
array7

array7[::-1]

# 9. Create a 3x3 matrix with values ranging from 0 to 8 (★☆☆)
matrix_9=np.arange(0,9).reshape(3,3)
matrix_9

# 10. Find indices of non-zero elements from [1,2,0,0,4,0] (★☆☆)
a=[1,2,0,0,4,0]
array_10=np.array(a)
array_10
array_10.nonzero()

# 11. Create a 3x3 identity matrix (★☆☆)
np.eye(3,3)

# 12. Create a 3x3x3 array with random values (★☆☆)
from numpy.random import randint
np.array(randint(1,100,27)).reshape(3,3,3)

# 13. Create a 10x10 array with random values and find the minimum and maximum values (★☆☆)
array_13=np.array(randint(1,1000,100)).reshape(10,10)
array_13.min()
array_13.max()

# 14. Create a random vector of size 30 and find the mean value (★☆☆)
array_14=np.array(randint(1,100,30))
array_14
array_14.mean()

# 15. Create a 2d array with 1 on the border and 0 inside (★☆☆)
array_15=np.ones((5,5))
array_15[1:4,1:4]=0
array_15

Z = np.ones((10,10))
Z[1:-1,1:-1] = 0
print(Z)

# 16. How to add a border (filled with 0's) around an existing array? (★☆☆)
array_13=np.array(randint(1,1000,100)).reshape(10,10)
array_13[0:10:9,0:10]=0
array_13[0:10,0:10:9]=0
array_13

Z = np.ones((5,5))
Z = np.pad(Z, pad_width=1, mode='constant', constant_values=0)
print(Z)

Z[:, [0, -1]] = 0
Z[[0, -1], :] = 0
print(Z)

# 17. What is the result of the following expression? (★☆☆)
0*np.nan
np.nan==np.nan
np.inf>np.nan
np.nan-np.nan
np.nan in set([np.nan])
0.3==3*0.1

# 18. Create a 5x5 matrix with values 1,2,3,4 just below the diagonal (★☆☆)
matrix_18=np.arange(0,25).reshape(5,5)
length=matrix_18.shape[1]
for i in range(length-1):
    matrix_18[i+1,i]=i+1
matrix_18

Z = np.diag(1+np.arange(4),k=-1)
print(Z)

# 19. Create a 8x8 matrix and fill it with a checkerboard pattern (★☆☆)
matrix_19=np.zeros((8,8))
row=matrix_19.shape[0]
col=matrix_19.shape[1]
for i in range(row):
    for j in range(col):
        if i%2==0 and j%2==1:
            matrix_19[i,j]=1
        elif i%2==1 and j%2==0:
            matrix_19[i,j]=1
matrix_19

matrix_19=np.zeros((8,8))
matrix_19[1::2,::2]=1
matrix_19[::2,1::2]=1
matrix_19

# 20. Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element? (★☆☆)
matrix_20=np.arange(0,336).reshape(6,7,8)
matrix_20
matrix_20[1,5,3] #d

# 21. Create a checkerboard 8x8 matrix using the tile function (★☆☆)
array_21=np.array([[0,1],[1,0]])
array_21
np.tile(array_21,(4,4))

# 22. Normalize a 5x5 random matrix (★☆☆)
from numpy.random import rand
rand(5,5) #d

# 23. Create a custom dtype that describes a color as four unsigned bytes (RGBA) (★☆☆)



# 24. Multiply a 5x3 matrix by a 3x2 matrix (real matrix product) (★☆☆)
arr1=np.random.randint(0,20,15).reshape(5,3)
arr2=np.random.randint(0,20,6).reshape(3,2)
np.multiply(arr1,arr2) #d

# 25. Given a 1D array, negate all elements which are between 3 and 8, in place. (★☆☆)
array_25=np.arange(0,10)
for i in range(10):
    if array_25[i]>=3 and array_25[i]<=8:
        array_25[i]=-array_25[i]
array_25

# 26. What is the output of the following script? (★☆☆)
print(sum(range(5),-1))
from numpy import *
print(sum(range(5),-1)) #d

# 27. Consider an integer vector Z, which of these expressions are legal? (★☆☆)
Z=2
Z**Z
2 << Z >> 2
Z <- Z
1j*Z
Z/1/1
Z<Z>Z #d

# 28. What are the result of the following expressions? (★☆☆)
np.array(0) / np.array(0)
np.array(0) // np.array(0)
np.array([np.nan]).astype(int).astype(float) #d

# 29. How to round away from zero a float array ? (★☆☆)
np.array([0.5,0.23,0.9,9.8,1.3,2.44,8.66,6.928]).round() #d

# 30. How to find common values between two arrays? (★☆☆)
array_1=np.array([5,6,9,3,4])
array_2=np.array([1,7,6,5,3,2])
np.intersect1d(array_1,array_2)

# 31. How to ignore all numpy warnings (not recommended)? (★☆☆)


# 32. Is the following expressions true? (★☆☆)
np.sqrt(-1) == np.emath.sqrt(-1) #d

# 33. How to get the dates of yesterday, today and tomorrow? (★☆☆)


# 34. How to get all the dates corresponding to the month of July 2016? (★★☆)


# 35. How to compute ((A+B)*(-A/2)) in place (without copy)? (★★☆)


# 36. Extract the integer part of a random array of positive numbers using 4 different methods (★★☆)


# 37. Create a 5x5 matrix with row values ranging from 0 to 4 (★★☆)
a=np.array([0,1,2,3,4])
np.tile(a,(5,1))

# 38. Consider a generator function that generates 10 integers and use it to build an array (★☆☆)
def value(a):
    for i in range(a):
        yield i
array_38=np.array([])
for i in value(10):
    array_38[i]=i
array_38

# 39. Create a vector of size 10 with values ranging from 0 to 1, both excluded (★★☆)
np.random.rand(10)

# 40. Create a random vector of size 10 and sort it (★★☆)
a=np.random.randint(1,50,10)
np.sort(a)

# 41. How to sum a small array faster than np.sum? (★★☆)
from functools import reduce
arr=np.array([0,1,2,3,4])
reduce(lambda x,y:x+y,arr)

# 42. Consider two random arrays A and B, check if they are equal (★★☆)
array_1=np.array([1,2,3,4])
array_2=np.array([1,2,3,4])
np.array_equal(array_1,array_2)

# 43. Make an array immutable (read-only) (★★☆)
tuple(np.array([1,2,3,4]))

# 44. Consider a random 10x2 matrix representing cartesian coordinates, convert them to polar coordinates (★★☆)


# 45. Create random vector of size 10 and replace the maximum value by 0 (★★☆)
a=np.random.randint(1,50,10)
a
maximum=a.max()
for i in range(10):
    if a[i]==maximum:
        a[i]=0
a

# 46. Create a structured array with `x` and `y` coordinates covering the [0,1]x[0,1] area (★★☆)

# 47. Given two arrays, X and Y, construct the Cauchy matrix C (Cij =1/(xi - yj)) (★★☆)

# 48. Print the minimum and maximum representable values for each numpy scalar type (★★☆)

# 49. How to print all the values of an array? (★★☆)
array_49=np.array([1,2,3,4,5,6,7,8,9])
for i in array_49:
    print(i)

# 50. How to find the closest value (to a given scalar) in a vector? (★★☆)
array_59=np.array([10,6,76,45,99,30,42,71,69])
val=int(input("Enter the number: "))
for i in range(array_59.size):
    if array_59[i]==val:
        if i==0:
            print(array_59[i+1])
        elif i==array_59.size-1:
            print(array_59[i-1])
        else:
            print(array_59[i+1])
            print(array_59[i-1])

# 51. Create a structured array representing a position (x,y) and a color (r,g,b) (★★☆)

# 52. Consider a random vector with shape (100,2) representing coordinates, find point by point distances (★★☆)

# 53. How to convert a float (32 bits) array into an integer (32 bits) array in place?
array_53=np.float32(np.array([9.3,5.66,6.85,3.87,7.542]))
np.int32(array_53)

# 54. How to read the following file? (★★☆)
"""
1, 2, 3, 4, 5
6,  ,  , 7, 8
 ,  , 9,10,11
"""

# 55. What is the equivalent of enumerate for numpy arrays? (★★☆)


# 56. Generate a generic 2D Gaussian-like array (★★☆)


# 57. How to randomly place p elements in a 2D array? (★★☆)


# 58. Subtract the mean of each row of a matrix (★★☆)
sub=0
array_58=np.arange(0,4).reshape(2,2)
array_58
row=array_58.shape[0]
for i in range(row):
    sub=array_58[i,:].mean()-sub
sub

# 59. How to sort an array by the nth column? (★★☆)
array_59=np.random.randint(1,100,20).reshape(5,4)

# 60. How to tell if a given 2D array has null columns? (★★☆)
array_60=np.array([[100,5,37,np.nan],[84,90,7,3]])
np.isnan(array_60)

import pandas as pd
df=pd.DataFrame([[100,5,37,2],[84,90,7,3]])
df1=df[df>10]
df1.isnull()

# 61. Find the nearest value from a given value in an array (★★☆)
array_61=np.array([10,6,76,45,99,30,42,71,69])
val=int(input("Enter the number: "))
for i in range(array_61.size):
    if array_61[i]==val:
        if i==0:
            print(array_61[i+1])
        elif i==array_61.size-1:
            print(array_61[i-1])
        else:
            print(array_61[i+1])
            print(array_61[i-1])

# 62. Considering two arrays with shape (1,3) and (3,1), how to compute their sum using an iterator? (★★☆)
a1=np.arange(1,4).reshape(1,3)
a1
b1=np.arange(1,4).reshape(3,1)
b1
sum(iter((a1,b1)))
np.add(a1,b1)

# 63. Create an array class that has a name attribute (★★☆)
class Array:
    name=""

# 64. Consider a given vector, how to add 1 to each element indexed by a second vector (be careful with repeated indices)? (★★★)

# 65. How to accumulate elements of a vector (X) to an array (F) based on an index list (I)? (★★★)

# 66. Considering a (w,h,3) image of (dtype=ubyte), compute the number of unique colors (★★☆)

# 67. Considering a four dimensions array, how to get sum over the last two axis at once? (★★★)



