#Frozen Sets:
	#frozen sets are special type of sets which makes as set imutable.
	# as bascially Sets are Mutable and their contents can be changed
	# after creation but by using frozenset() function can make 
	#and set imutable.

f_set= frozenset([1,2,4,6])
print(f_set)
#fset=f_set.update([3,5]) #if you try to update an frozenset then
#it will throw the following exception
#AttributeError: 'frozenset' object has no attribute 'update'

#Modifying a Set
#Augmented Assignment Operators and Methods
#Each of the union, intersection, difference, 
	#and symmetric difference operators listed above 
#has an augmented assignment form that can be used to modify a set. 
#For each, there is a corresponding method as well.

#x1.update(x2[, x3 ...])
#x1 |= x2 [| x3 ...]
#Modify a set by union.
#x1.update(x2) and x1 |= x2 add to x1 any elements in x2 
	#that x1 does not already have:
def modifyUsingUnion():
	x1 = {'foo', 'bar', 'baz'}
	x2 = {'foo', 'baz', 'qux'}
	x1 |= x2
	print(x1)
	x1.update(['ayesha','quxd'])
	print(x1)


#x1.intersection_update(x2[, x3 ...])
#x1 &= x2 [& x3 ...]
#Modify a set by intersection.
#x1.intersection_update(x2) and x1 &= x2 update x1,
#retaining only elements found in both x1 and x2:
def modifyUsingIntersection():
	x1 = {'foo', 'bar', 'baz'}
	x2 = {'foo', 'baz', 'qux'}
	x1 &= x2
	print(x1)
	x2.intersection_update(x1)
	print(x2)

#x1.difference_update(x2[, x3 ...])
#x1 -= x2 [| x3 ...]
#Modify a set by difference.
#x1.difference_update(x2) and x1 -= x2 update x1, 
	#removing elements found in x2:
def modifyDiff():
	x1 = {'foo', 'bar', 'baz'}
	x2 = {'foo', 'baz', 'qux'}
	x1 -= x2
	print(x1)
	x2.difference_update(x1)
	print(x2)

#x1.symmetric_difference_update(x2)
#x1 ^= x2
#Modify a set by symmetric difference.
#x1.symmetric_difference_update(x2) and x1 ^= x2 update x1,
#retaining elements found in either x1 or x2, but not both:
def modfiySymmetricDiff():
	x1 = {'foo', 'bar', 'baz'}
	x2 = {'foo', 'baz', 'qux'}
	x1 ^= x2
	print(x1)
	x2.symmetric_difference_update(x1)
	print(x2)


#Other Methods For Modifying Sets
def OtherMethods():
	x = {'foo', 'bar', 'baz'}
	#x.add(<elem>)#Adds an element to a set.
#x.add(<elem>) adds <elem>, which must be a single immutable object, to x
	x.add('bat') 
	print(x)
	#x.remove(<elem>)#Removes an element from a set.
#x.remove(<elem>) removes <elem> from x. Python raises an exception if <elem> is not in x:
	x.remove('baz') 
	print(x)
	#x.discard(<elem>)#Removes an element from a set.
#x.discard(<elem>) also removes <elem> from x. However,
#if <elem> is not in x, this method quietly does nothing instead of raising an exception:
	x.discard('bat') 
	print(x)
	#x.pop()#Removes a random element from a set.
#x.pop() removes and returns an arbitrarily chosen element from x. 
#If x is empty, x.pop() raises an exception:
	print(x.pop())
	x.clear() #Clears a set.
#x.clear() removes all elements from x:
	print(x.clear())
	


#functionCalls
#modifyUsingUnion()
#modifyUsingIntersection()
#modifyDiff()
#modfiySymmetricDiff()
#OtherMethods()



