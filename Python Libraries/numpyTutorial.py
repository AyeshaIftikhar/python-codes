import numpy as np
#numpy os used when you need to use arrays for some type of data
#each function of Numpy library is accessed using the Numpy object "np"

#shows differecnce between array and list
def arrayVsList():
	list1=[1,3,4,5,6,7]
	print('list is',list1)
	# array() creates an array or convert data into array
	array1=np.array(list1)
	print('array is',array1)

#find size and shape of the array:  total elements inside the array
def sizeAndshape():
	arr=np.array([(1,2,3,4),(5,6,7,8)])
	print('array is:',arr)
	# size() to find size of array
	print('size of Array:',np.size(arr))
	#shape() to find shape of the array wether is is 2-D , 3-D 
	print('shape of the array:', np.shape(arr))

#global array
arr=np.array([(1,2,3,4),(5,6,7,8)])
#Reshaping numpy array: change the dimension of array from (2,4) to (4,2)
def reshapeArray():
	print('Original Array:',arr)
	# reshape() is usend to change the shape/dimensions of the array, 
	# you have to tell manually in which shaoe you want your array to transform
	#consider the size of array and then convert he array into new form according to the factors of size
	arr1=np.array([(1,2,3,4),(5,6,7,8),(1,3,4,5)])
	#print('Array after reshaping:(12 elements 3*4)',arr1.reshape(3,4))
	#print('Array after reshaping:(12 elements 6*2)',arr1.reshape(6,2))
	print('Array after reshaping:', arr.reshape(8,1))
	print('Array after reshaping:', arr.reshape(1,8))

# Datatype and change datatype: we can change datatypes directly using astype function
def arrayDatatype():
	#dtype tells the datatype of array
	print('Datatype of Array:',arr.dtype)
	##change datatype
	#astype() used to change the array type
	float_arr=arr.astype(np.float64)
	print('New Array:',float_arr)
	print('Datatype of new Array:',float_arr.dtype)

# Indexing and slicing: Indexing and slicing is same as a list for 1-D array but it is different for 2-D array.
#We can also change the elements of 2-D array. array1[1,3] here 1 means row at index 1
#i.e. row number 2 and 3 means column at index number 3 i.e. 4th column.
#As a whole,in 2nd row 4th column i.e 6
def IndexingAndSlicingArray():
	print('Array at index [1]:', arr[1]) # using this type of index will display all columns values
	print('Array at index[1,3]:',arr[1,3])
	#slicing
	print('in slice:',arr[:2,3:]) # display item as different array elements
	print(arr[:2,3]) #display items as same array elements

#Transpose and Dot product: transpose and dot product can be done by “T” and “dot” function respectively.
#for dot product (5,2)*(2,5) the column number and row number of respective arrays should be same
def TandDOnArray():
	arr2=np.arange(10).reshape(5,2)   ##5*2=10,5*2 matrix/array #default create an array
	print(arr2)
	#transpose of Array
	print('Transpose on Array:',arr2.T) ## becomes 2*5 matrix/array
	#dot product
	print('Dot product on Array',np.dot(arr2.T,arr2))

#Universal functions: ndarray functions(Max,min,mean,sum,standard deviation(std),variance(var)),
#numpy functions(sqrt,exp,arange,random.randn,square,log). ndarray is np.array
def UniversalFun():
	array3=np.array([1,2,3,4,5,6,7,8,9,0,40])
	print('Array is:',arr1)
	print('sum of array elements:',array3.sum())
	print('maximum in array elements:',array3.max())
	print('standard deviation:',array3.std())
	print('variance of array:',array3.var())
	print('median of Array:',np.median(array3))
	print('square root of elements:',np.sqrt(array3))

#Conditional logic on Array operations: Using “where” function. “np.where(array4 > 0, 2, -2)” says 
#that list all elements in array 4 greater than 0 →change all those elements to 2 → else change to -2(i.e if array4 <0)
def ConditonalLogic():
	array4=np.random.randn(2,3) # random will select random numbers 
	print('Array is:',array4)
	print('Arrya>0 :', array4>0) # give answer in boolean and check each element of array
	#define if else condtion 1st part is if then and 2nd is else
	print('Array> 0,2 and -2: ',np.where(array4 > 0, 2, -2))

#Operation on row and column: “ axis = 0 ” performs an operation on each y-axis within the array. 
#“ axis = 1 ” performs an operation on each x-axis within the array. 
#“ axis = None” performs an operation on all values in the array, it is default
def opOnArray():
	print('Operation on y-axis:', arr.sum(axis=0))
	print('operation on x-axis:',arr.sum(axis=1))
	print('operation on complete region:', arr.sum(axis=None))

#Concatenate arrays: we have concatenated two 2*4 matrix and resultant is 4*4 matrix
def ConcateArray():
	array5=np.random.randn(2,4)
	print('concatenate arr and array5:',np.concatenate((arr,array5)))

#Sorting,unique,sets: Sorting by rows and columns. 1st row desc 2nd row asc
def sortingArray():
	arr.sort(1) # sort the array
	print('sorted array:',arr)
	names = np.array(['Chandu','Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe','ayesha'])
	print('Array of names:',names)
	print('unique names in names:', np.unique(names)) #find all uniques names # inshort print all names only once
	print('sorted set names:',sorted(set(names))) #sort the names

#identity matrix
def IdentityMatrix():
	print('create identity:',np.identity(2))
	print(np.eye(2,4,k=2))


#fuction calls
#arrayVsList()
sizeAndshape()
#reshapeArray()
#arrayDatatype()
#IndexingAndSlicingArray()
#TandDOnArray()
#UniversalFun()
#ConditonalLogic()
#opOnArray()
#ConcateArray()
#sortingArray()
IdentityMatrix()