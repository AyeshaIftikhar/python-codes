#Frozen Sets
#Python provides another built-in type called a frozenset, 
#which is in all respects exactly like a set, except that a frozenset is immutable. 
#You can perform non-modifying operations on a frozenset:

def frozenSets():
	x = frozenset(['foo', 'bar', 'baz'])
	#print('Frozen set is:',x)
	print(len(x))
	print(x&{'baz','tar'})
	#But methods that attempt to modify a frozenset fail: 
	#can't add ,remove , discard and clear a frozen set

#Frozensets and Augmented Assignment
def fAndaSets():
	f = frozenset(['foo', 'bar', 'baz'])
	s={'baz', 'qux', 'quux'}
	f &=s
	print(f)
#Python does not perform augmented assignments on frozensets in place. 
#The statement x &= s is effectively equivalent to x = x & s.
#It isn’t modifying the original x. 
#It is reassigning x to a new object, and the object x originally referenced is gone
def withIdFandAsets():
	f = frozenset(['foo', 'bar', 'baz'])
	print(id(f))
	s={'baz', 'qux', 'quux'}
	f &=s
	print(f)
	print(id(f))

#Frozensets are useful in situations where you want to use a set, 
#but you need an immutable object.
#If you really feel compelled to define a set of sets (hey, it could happen),
#you can do it if the elements are frozensets, because they are immutable:
def setOfsets():
	x1 = frozenset(['foo'])
	x2 = frozenset(['bar'])
	x3 = frozenset(['baz'])
	x4=frozenset(['zip'])
	x = {x1, x2, x3,x4}
	print(x)

#If you find yourself needing to use sets as dictionary keys, you can use frozensets:
def fSetandDictionary():
	x = frozenset({1, 2, 3})
	y = frozenset({'a', 'b', 'c'})
	d = {x: 'foo', y: 'bar'}
	print(d)

#functionCalls
#frozenSets()
#fAndaSets()
#withIdFandAsets()
#setOfsets()
fSetandDictionary()

