import numpy as np

oneDim = np.array([1.0,2,3,4,5])   # a 1-dimensional array (vector)
print(oneDim)
print("#Dimensions =", oneDim.ndim)
print("Dimension =", oneDim.shape)
print("Size =", oneDim.size)
print("Array type =", oneDim.dtype, '\n')

twoDim = np.array([[1,2],[3,4],[5,6],[7,8]])  # a two-dimensional array (matrix)
print(twoDim)
print("#Dimensions =", twoDim.ndim)
print("Dimension =", twoDim.shape)
print("Size =", twoDim.size)
print("Array type =", twoDim.dtype, '\n')

arrFromTuple = np.array([(1,'a',3.0),(2,'b',3.5)])  # create ndarray from tuple
print(arrFromTuple)
print("#Dimensions =", arrFromTuple.ndim)
print("Dimension =", arrFromTuple.shape)
print("Size =", arrFromTuple.size)

#numpy ndarrays 
print('Array of random numbers from a uniform distribution')
print(np.random.rand(5))      # random numbers from a uniform distribution between [0,1]

print('\nArray of random numbers from a normal distribution')
print(np.random.randn(5))     # random numbers from a normal distribution

print('\nArray of integers between -10 and 10, with step size of 2')
print(np.arange(-10,10,2))    # similar to range, but returns ndarray instead of list

print('\n2-dimensional array of integers from 0 to 11')
print(np.arange(12).reshape(3,4))  # reshape to a matrix

print('\nArray of values between 0 and 1, split into 10 equally spaced values')
print(np.linspace(0,1,10))    # split interval [0,1] into 10 equally separated values

print('\nArray of values from 10^-3 to 10^3')
print(np.logspace(-3,3,7))    # cre

print('A 2 x 3 matrix of zeros')
print(np.zeros((2,3)))        # a matrix of zeros

print('\nA 3 x 2 matrix of ones')
print(np.ones((3,2)))         # a matrix of ones

print('\nA 3 x 3 identity matrix')
print(np.eye(3))              # a 3 x 3 identity matrix


x = np.array([1,2,3,4,5])

print('x =', x)
print('x + 1 =', x + 1)      # addition
print('x - 1 =', x - 1)      # subtraction
print('x * 2 =', x * 2)      # multiplication
print('x // 2 =', x // 2)     # integer division
print('x ** 2 =', x ** 2)     # square
print('x % 2 =', x % 2)      # modulo  
print('1 / x =', 1 / x)      # division


x = np.array([2,4,6,8,10])
y = np.array([1,2,3,4,5])

print('x =', x)
print('y =', y)
print('x + y =', x + y)      # element-wise addition
print('x - y =', x - y)      # element-wise subtraction
print('x * y =', x * y)      # element-wise multiplication 
print('x / y =', x / y)      # element-wise division
print('x // y =', x // y)    # element-wise integer division 
print('x ** y =', x ** y)    # element-wise exponentiation



x = np.arange(-5,5)
print('Before: x =', x)

y = x[3:5]     # y is a slice, i.e., pointer to a subarray in x
print('        y =', y)
y[:] = 1000    # modifying the value of y will change x
print('After : y =', y)
print('        x =', x, '\n')

z = x[3:5].copy()   # makes a copy of the subarray
print('Before: x =', x)
print('        z =', z)
z[:] = 500          # modifying the value of z will not affect x
print('After : z =', z)
print('        x =', x)


my2dlist = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]  # a 2-dim list
print('my2dlist =', my2dlist)
print('my2dlist[2] =', my2dlist[2])            # access the third sublist
print('my2dlist[:][2] =', my2dlist[:][2])      # can't access third element of each sublist
# print('my2dlist[:,2] =', my2dlist[:,2])      # invalid way to access sublist, will cause syntax error

my2darr = np.array(my2dlist)
print('\nmy2darr =\n', my2darr)

print('my2darr[2][:] =', my2darr[2][:])      # access the third row
print('my2darr[2,:] =', my2darr[2,:])        # access the third row
print('my2darr[:][2] =', my2darr[:][2])      # access the third row (similar to 2d list)
print('my2darr[:,2] =', my2darr[:,2])        # access the third column
print('my2darr[:2,2:] =\n', my2darr[:2,2:])     # access the first two rows & last two columns


my2darr = np.arange(1,13,1).reshape(3,4)
print('my2darr =\n', my2darr)

divBy3 = my2darr[my2darr % 3 == 0]
print('\nmy2darr[my2darr % 3 == 0] =', divBy3)            # returns all the elements divisible by 3 in an ndarray

divBy3LastRow = my2darr[2:, my2darr[2,:] % 3 == 0]
print('my2darr[2:, my2darr[2,:] % 3 == 0] =', divBy3LastRow)    # returns elements in the last row divisible by 3


my2darr = np.arange(1,13,1).reshape(4,3)
print('my2darr =\n', my2darr)

indices = [2,1,0,3]    # selected row indices
print('indices =', indices, '\n')
print('my2darr[indices,:] =\n', my2darr[indices,:])  # this will shuffle the rows of my2darr

rowIndex = [0,0,1,2,3]     # row index into my2darr
print('\nrowIndex =', rowIndex)
columnIndex = [0,2,0,1,2]  # column index into my2darr
print('columnIndex =', columnIndex, '\n')
print('my2darr[rowIndex,columnIndex] =', my2darr[rowIndex,columnIndex])


y = np.array([-1.4, 0.4, -3.2, 2.5, 3.4])    
print('y =', y, '\n')

print('np.abs(y) =', np.abs(y))                # convert to absolute values
print('np.sqrt(abs(y)) =', np.sqrt(abs(y)))    # apply square root to each element
print('np.sign(y) =', np.sign(y))              # get the sign of each element
print('np.exp(y) =', np.exp(y))                # apply exponentiation
print('np.sort(y) =', np.sort(y))              # sort array

x = np.arange(-2,3)
y = np.random.randn(5)
print('x =', x)
print('y =', y, '\n')

print('np.add(x,y) =', np.add(x,y))                # element-wise addition       x + y
print('np.subtract(x,y) =', np.subtract(x,y))      # element-wise subtraction    x - y
print('np.multiply(x,y) =', np.multiply(x,y))      # element-wise multiplication x * y
print('np.divide(x,y) =', np.divide(x,y))          # element-wise division       x / y
print('np.maximum(x,y) =', np.maximum(x,y)) 