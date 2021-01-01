#a set can be thought of simply 
	#as a well-defined collection of distinct objects, 
#typically called elements or members.
# Sets are distinguished from other object types
#by the unique operations that can be performed on them.
#Defining a Set

#Python’s built-in set type has the following characteristics:
#Sets are unordered.
#Set elements are unique. Duplicate elements are not allowed.
#A set itself may be modified, 
#but the elements contained in the set must be of an immutable type.

#A set can be created in two ways.
#First, you can define a set with the built-in set() function:
#x = set(<iter>)
x=set(['foo','qux','quick','can','never'])
print('set is:',x)

#Strings are also iterable, so a string can be passed to set() as well.
#You have already seen that list(s) generates a list of the characters
	# in the string s.
 #Similarly, set(s) generates a set of the characters in s:
def setFromString():
	s='ayesha'
	x1=set(s)
	print('set created using string:',x1)
	#the resulting sets are unordered: the original order, 
		#as specified in the definition, 
	#is not necessarily preserved. 
	#Additionally, duplicate values are only represented in the set once,

#Alternately, a set can be defined with curly braces ({}):
def setUsingCurlyBraces():
	x2={1,3,5,6,7,8,90}
	print('set is:',x2)
	#When a set is defined this way, each <obj> becomes a distinct element of the set,
	#even if it is an iterable.
	#This behavior is similar to that of the .append() list method.

#The argument to set() is an iterable. 
#It generates a list of elements to be placed into the set.
#The objects in curly braces are placed into the set intact, even if they are iterable

#Observe the difference between these two set definitions:
s={'foo'}
print('s:',s)
s1=set('foo')
print('s1:',s1)

#A set can be empty. 
#Python interprets empty curly braces ({}) as an empty dictionary, 
#so the only way to define an empty set is with the set() function
def emptySet():
	x3=set()
	print('set is:',x3)
	#An empty set is false in Boolean context:
	print(bool(x3))
	print(x3 or 1)
	print(x3 or 0)
	print(x3 and 1)
	print(x3 and 0)

#Python does not require this, though. 
#The elements in a set can be objects of different types:
def setElements():
	s={'ayesha',1,3.12,None}
	print('Set:',s)
	#Don’t forget that set elements must be immutable. 
	#For example, a tuple may be included in a set:
	s1={42, 'foo', (1, 2, 3), 3.14159}
	print('Set:',s1)
	#But lists and dictionaries are mutable, so they can’t be set elements:

#Set Size and Membership
#The len() function returns the number of elements in a set, 
#and the in and not in operators can be used to test for membership:
def setSizeAndMembership():
	print(len(x))
	print('can' in x) # return true if element in set otherwise return false
	print('xm' in x) 

#Operating on a set
#Many of the operations that can be used for Python’s other 
	#composite data types 
#don’t make sense for sets. 
#For example, sets can’t be indexed or sliced. 
#However, Python provides a whole host of operations on set objects 
#that generally mimic the operations that are defined for mathematical sets.
#Operators vs. Methods
#Most, though not quite all, set operations in Python can be performed 
	#in two different ways: 
#by operator or by method

x1 = {'baz', 'qux', 'quux'}

#setOperationsAndMethods
def setUnion():
	#set union can be performed with the | operator:
	print('union of x and x1 is:',x|x1) #both elements should be set
	#Set union can also be obtained with the .union() method. 
	#The method is invoked on one of the sets, and the other 
		#is passed as an argument:
	print('union is:',x.union(x1))
	#The .union() method, on the other hand, will take any iterable 
	 #as an argument, 
	#convert it to a set, and then perform the union.
	#More than two sets may be specified with either the operator 
		#or the method:
	a = {1, 2, 3, 4}
	b = {2, 3, 4, 5}
	c = {3, 4, 5, 6}
	d = {4, 5, 6, 7}
	print(a.union(b,c,d))
	print(a|b|c|d)

	
def setIntersection():
	#x1.intersection(x2[, x3 ...])
	#x1 & x2 [& x3 ...]
	#Compute the intersection of two or more sets.
	print('intersection is:',x.intersection(x1))
	# can use & operator for intersection
	print(x & x1)
	a = {1, 2, 3, 4}
	b = {2, 3, 4, 5}
	c = {3, 4, 5, 6}
	d = {4, 5, 6, 7}
	print(a.intersection(b,c,d))
	print(a&b&c&d)

#x1.difference(x2[, x3 ...])
#x1 - x2 [- x3 ...]
#Compute the difference between two or more sets.
def setDiff():
	print('difference is:')
	print(x.difference(x1))
	print(x-x1)
	#you can specify more than two sets:
	a = {1, 2, 3, 30, 300}
	b = {10, 20, 30, 40}
	c = {100, 200, 300, 400}
	print(b.difference(a,c))
	print(c-a-b)

#x1.symmetric_difference(x2)
#x1 ^ x2 [^ x3 ...]
#Compute the symmetric difference between sets.
def symmetricDiff():
	print('symmetric_difference is:')
	print(x1.symmetric_difference(x))
	print(x^x1)
	#The ^ operator also allows more than two sets:
	a = {1, 2, 3, 4, 5}
	b = {10, 2, 3, 4, 50}
	c = {1, 50, 100}
	print(a^b^c)
	#As with the difference operator, when multiple sets are specified, 
	#the operation is performed from left to right.

#x1.isdisjoint(x2)
#Determines whether or not two sets have any elements in common.
def disjointSets():	
	print('Disjoint set is:')
	print(x1.isdisjoint(x)) # returns false if any common element
	print( x1- {'baz'})
	print(x1.isdisjoint(x - {'baz'}))
	#If x1.isdisjoint(x2) is True, then x1 & x2 is the empty set:
	a = {1, 3, 5}
	b = {2, 4, 6}
	print(a.isdisjoint(b))
	print(a & b) 

#x1.issubset(x2)
#x1 <= x2
#Determine whether one set is a subset of the other.
def isSubset():
	print(x1.issubset(x))
	print(x<=x1) # return true if 1st set is subset of 
		#2nd otherwise return false
	#A set is considered to be a subset of itself:
	print(x<=x)

#x1 < x2
#Determines whether one set is a proper subset of the other.
# if x2 is subset of x1 but both sets are nt equal sets
def isProperSubset():
	print(x<x1) # returns true if propersubset otherwise returns false
	#While a set is considered a subset of itself, 
		#it is not a proper subset of itself:
	print(x<x)

#x1.issuperset(x2)
#x1 >= x2
#Determine whether one set is a superset of the other.
#A superset is the reverse of a subset. 
#A set x1 is considered a superset of another set x2 if x1 contains 
	#every element of x2.
#x1.issuperset(x2) and x1 >= x2 return True if x1 is a superset of x2:
def isSuperSet():
	print(x>=x1)
	print(x.issuperset(x1))
	#A set is also considered a superset of itself:
	print(x>=x)

#x1 > x2
#Determines whether one set is a proper superset of the other.
#A proper superset is the same as a superset, except that 
the sets can’t be identical.
#A set x1 is considered a proper superset of another set x2 
#if x1 contains every element of x2, and x1 and x2 are not equal.
#x1 > x2 returns True if x1 is a proper superset of x2:
def properSuperSet():
	print(x>x1)
	#A set is not a proper superset of itself:
	print(x>x)

#functioncalls

#setFromString()
#setUsingCurlyBraces()
#emptySet()
setElements()
#setSizeAndMembership()
#setUnion()
#setIntersection()
#setDiff()
#symmetricDiff()
#disjointSets()
#isSubset()
#isProperSubset()
#isSuperSet()
#properSuperSet()

