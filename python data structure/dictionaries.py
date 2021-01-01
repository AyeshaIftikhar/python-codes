#dictionary
#A dictionary is a sequence of items. 
#Each item is a pair made of a key and a value. Dictionaries are not sorted. 
#You can access to the list of keys or values independently

#dictionaries are mutable, they can be changed after creation.
#represents collection types.

#defining a list
def dic():
	#MLB_team = {  'Colorado' : 'Rockies','Boston'   : 'Red Sox','Minnesota': 'Twins','Milwaukee': 'Brewers', }
	#return MLB_team	 
	#building a dictionary using dict() method
	MLBteam = dict([('Colorado', 'Rockies'),('Boston', 'Red Sox'),('Minnesota', 'Twins'),
	('Milwaukee', 'Brewers'),('Seattle', 'Mariners'),('NewYork', 'Ronaldo')])
	#return MLBteam
	# type(MLB_team)
	#<class 'dict'>
 	#print(MLB_team)

#dictionary elemnets are not accessible by number index
#If the key values are simple strings, 
#they can be specified as keyword arguments. 
MLB_team = dict(Colorado='Rockies',Boston='Red Sox',Milwaukee='Brewers',Seattle='Mariners')

#Accessing dictionary values 
#value of dictionary element is accessible by using 
	#corresponding key in square brackets[] 
def accessElements():
	print('value againsts Colorado key:',MLB_team['Colorado'])
	#If you refer to a key that is not in the dictionary, 
		#Python raises an exception:
	#print('value against Tornoto:', MLB_team['Toronto'])

#Adding an entry to an existing dictionary is simply a matter 
	#of assigning a new key and value:
def addValue():
	MLB_team['Kansas City'] = 'Royals'
	#If you want to update an entry, you can just assign 
		#a new value to an existing key:
	MLB_team['Seattle'] = 'KansasCity'
	return MLB_team

#To delete an entry, use the del statement, specifying the key to delete:
def delElemets():
	del MLB_team['Seattle']
	return MLB_team

#can used integers as dictionary keys
def dic1():
	d = {0: 'a', 1: 'b', 2: 'c', 3: 'd',4: 'ayesha'}
	print('dictionary:',d)
	#elemets can be accessed separatly using keys
	print('element at 0 key:',d[0])
	print('element at 4 key:',d[4])

#the numbers in square brackets appear as though they might be indices.
#But they have nothing to do with the order of the items in the dictionary.
#Python is interpreting them as dictionary keys. 
#If you define this same dictionary in reverse order, 
#you still get the same values using the same keys:
def dic2():
	d= {4:'ayesha',3: 'd', 2: 'c', 1: 'b', 0: 'a'}
	print('dictionary in reverse orer:',d)
	print('element at 0 key:',d[0])
	print('element at 4 key:',d[4])

#creating an dictionary incrementally
def incrementDic():
	person = {}
	# type(person)
	#<class 'dict'>
	print('Empty dictionary:',person)
	person['fname'] ='Joe'
	print('having one element:',person)
	person['lname'] = 'Fonebone'
	print('having two elements:',person)
	person['age'] = 51
	person['spouse'] = 'Edna'
	person['children'] = ['Ralph', 'Betty', 'Joey']
	person['pets'] = {'dog': 'Fido', 'cat': 'Sox'}
	print('having multiple elements:',person)
	#Once the dictionary is created in this way, its values are accessed the same way as any other dictionary
	#it is also a nested dictionary
	#Retrieving the values in the sublist or subdictionary requires an additional index or key:
	print('elements of subdictionary children:',person['children'][-1])
	print('element of subdictionary pets:', person['pets']['cat'])
	# the values contained in the dictionary don’t need to be the same type

#restrictions on dictionaries
#Almost any type of value can be used as a dictionary key in Python. 
#You can even use built-in objects like types and functions:
def dictionary():
	d = {int: 1, float: 2, bool: 3}
	print('built in datatypes:',d)
	print('float:',d[float])
	d = {bin: 1, hex: 2, oct: 3}
	print(d)
	print('hexadecimal:',d[hex])

#there are a couple restrictions that dictionary keys must abide by.
#First, a given key can appear in a dictionary only once. 
#Duplicate keys are not allowed.
#A dictionary maps each key to a corresponding value,
#so it doesn’t make sense to map a particular key more than once.
#when you assign a value to an already existing dictionary key, 
#it does not add the key a second time, but replaces the existing value:
#if you specify a key a second time during the initial creation of a dictionary, 
#the second occurrence will override the first:
#a dictionary key must be of a type that is immutable. 


#A tuple can also be a dictionary key, because tuples are immutable:
def tupleDic():
	d = {(1, 1): 'a', (1, 2): 'b', (2, 1): 'c', (2, 2): 'd',(3,1):'e'}
	print('tuple as dictionary', d)
	#can access elements separatly
	print('1st element :', d[(1,1)])
	#However, neither a list nor another dictionary can serve as a dictionary key, 
	#because lists and dictionaries are mutable:

#restrictions on dictionary values
#there are no restrictions on dictionary values. Literally none at all.
#A dictionary value can be any type of object Python supports, 
#There is also no restriction against a particular value appearing in a dictionary multiple times:
#built in dictionary methods

def builtinMethod():
	d = {'a': 10, 'b': 20, 'c': 30}
	#print(d)
		#clear >> Clears a dictionary.
	#d.clear()
		#d.get(<key>[, <default>])
		#Returns the value for a key if it exists in the dictionary.
	#print(d.get('b'))
		#If <key> is not found and the optional <default> argument is specified,
		# that value is returned instead of None:
	#print(d.get('z', -1))
		
def preMethods():
	d = {'a': 10, 'b': 20, 'c': 30}
		#d.items()
		#Returns a list of key-value pairs in a dictionary.
	#print(list(d.items()))
	#print(list(d.items())[1][0])
	#print(list(d.items())[1][1])
		#d.keys()
		#Returns a list of keys in a dictionary.
	#print(list(d.keys()))
		#d.values()
		#Returns a list of values in a dictionary.
	print(list(d.values()))
		#Any duplicate values in d will be returned as many times as they occur:
#The .items(), .keys(), and .values() methods actually return something called a view object
		#d.pop(<key>[, <default>])
		#Removes a key from a dictionary, if it is present, and returns its value.
	#print(d.pop('b'))
		#d.pop(<key>) raises a KeyError exception if <key> is not in d:
		#If <key> is not in d, and the optional <default> argument is specified,
		# then that value is returned, and no exception is raised:
	#print( d.pop('z', -1))
		#d.popitem()
		#Removes a key-value pair from a dictionary.
	print(d.popitem())
		#If d is empty, d.popitem() raises a KeyError exception:
		#d.update(<obj>)
		#Merges a dictionary with another dictionary or with an iterable of key-value pairs.
	d2 = {'b': 200, 'd': 400}
	#d.update(d2)
		#<obj> may also be a sequence of key-value pairs
	#d.update([('b', 200), ('d', 400)])
		#Or the values to merge can be specified as a list of keyword arguments:
	d.update(b=200, d=400)
	print(d)
		
		


	

# Function Calls

#d=dic()
#print(d)
#accessElements()
#result=addValue()
#print(result)
#out=delElemets()
#print(out)
#dic1()
#dic2()
#incrementDic()
#dictionary()
#tupleDic()
#builtinMethod()
preMethods()

