import pandas as pd
from pandas import Series

#Series:A Series is a one-dimensional array-like object containing a sequence of values (of similar types to NumPy types) 
#and an associated array of data labels, called its index. The simplest Series is formed from only an array of data. 
#In the following index is similar to indexing of a list.
#create series
obj=pd.Series([4,5,0,-3,10])
print('Series is:',obj)
#on printing a series the indexes are add automatiically starting fron '0' and datatype od series is also mentioned 

#fetch value and index of pandas series:We can get the array representation and index object of the Series via its values
 #and index attributes, respectively:
#Also, we can directly access its values same as in list.
def valueAndIndex():
	print(obj)
	print('print values of series:',obj.values) #print values only
	print('print index of obj:',obj.index) #tells the start , range and increment of indexes
	print('value at obj[1]:',obj[1])

#Assign custom index in series: we can create a Series with an index identifying each data point with a label. 
#Any mathematical operation(as np.sqrt) will change the value of the series not the index.
def CustomIndex():
	obj1=pd.Series([4,5,7,-2],index=['a','b','e','d'])
	#print('obj2 is:',obj1)
	#print('obj2[a]:',obj1['a']) #value fetching using indexes
	return obj1

#filtering and maths operations:
def filteringAndMaths():
	print('obj at obj<0:',obj[obj<0]) # display the value and its index which is less than 0 along with datatype of series
	print('Series at obj**2',obj**2) # it will display all the elements of series

#make series from dictionary:
def makeFromDict():
	data1 = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000} #defining a dictionary
	obj2=pd.Series(data1) #will convert a dictionary into Series
	#print('Series is:',obj2) #will make keys of an dictionary index of series
	return obj2

#is null and not null:
def isOrnotNull():
	obj3=makeFromDict() #calling funtion and assinging its returned value to obj3
	#if series is not null it returns true against each index and return datatype according to displayed series
	#it returns false if series is null
	print('obj3 is null or not?(using notnull funtion):',pd.notnull(obj3)) 
	#if series is not null it returns false against each index and return datatype according to displayed series
	#if series is null it returns true
	print('obj3 is null or not? (using isnull function):',pd.isnull(obj3))

#override the index:
def indexOverride():
	data1 = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
	state=['California', 'Ohio', 'Oregon', 'Texas','Egypt']
	#we only add 2 new index remaing are same the new added index are null in output
	obj4 = pd.Series(data1, index=state)
	#print('obj4 is:',obj4) #change the index of series specified in state list
	return obj4

#Combining series: The two series are combined with index arranged in ascending alphabetical order.
def combineSeries():
	obj5=makeFromDict()
	obj6=indexOverride()
	print('obj5 is:',obj5)
	print('obj6 is:',obj6)
	print('Combined series:',obj5+obj6) #combine series having indexs in text/words
	# can't combine 3 or m0re series trial to combine 
	#will result combined dictionary null
	print(obj) 
	print('Combined series are:',obj+obj5+obj6)
	 #order matters and if we place the numbered index series at first place numbers index comes first
	 #but it makes all elements of combined series null because we cant combine numbered indexed series with alphabetical index
	print('combined series:',obj5+obj6+obj) 
	print('combined series:',obj5+obj6+obj) 

#Naming the series and the index:
def namingSeriesAndIndex():
	obj8=makeFromDict()
	obj8.name='Population'
	obj8.index.name='State'
	print('obj8 is\n',obj8)

#function calls

#valueAndIndex()
#CustomIndex()
#filteringAndMaths()
#makeFromDict()
#isOrnotNull()
#indexOverride()
combineSeries()
#namingSeriesAndIndex()