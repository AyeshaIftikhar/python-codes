#list : are objects and are mutable
#lists are dynamics, it means that you can change the elements in the list
#

a = ['foo','bar', 'baz', 'qax','pen']
b=['pen','baz','bar', 'foo', 'qax'] 
#lists are ordered
def listorder():
	print('list a:',a)
	print('list b:',b)
	if a == b:
		print('Okay')
	else:
		print('Not okay')

#listorder()

#list can contain arbitrary objects
c=[2,4,6,8]
def arbitraryValues():
	print('list c:',c)

#arbitraryValues()

## varrying types of elements(single list can have different types 
#of elements)
d=[21,23,'football',3,4,6,'bark', False,3.14,'c']
def varyElements():
	print('list d:',d)

varyElements()	

# empty and sigleton list
def emptyAndSingltonList():
	e=[]
	f=['ayesha']
	print('list e and f:',e,f)

emptyAndSingltonList()

#list objects don't need to be unique
g=['ayesha', 'kaynat', 'ayesha']
def listElements():
	print('list g:',g)

listElements()

#list objects can be accessed using index starting from 0
def AccessingElements():
	print('first element of g is',g[0])
	print('2nd element of g is',g[1])
	print('4th element of d is',d[3])
	#negative list address counts from the end of the list 
	print('element of g is',g[-1])

AccessingElements()

#slicing
def listSlicing():
	print('d',d)
	print('From d(2nd to 9th):', d[2:9]) #2nd(starting) to 9th(mentioned-1) index elements
	print('From d:',d[-7:-1]) #negative indexes also specified
	#omitting the 1st index starts the slice at the begining of the list
	print(d[:5],d[0:5]) # both works same
	#omitting the 2nd index extends the slice to the end of the list
	print(d[2:], d[2:10]) # both are same
	print(d[:5]+d[5:])

listSlicing()

#can specify a stride-- either positive or negative
def Stride():
	print('a',a)
	print(a[0:3:4])
	print(a[1:3:4])
	print(a[2:3:4])
	print(a[6:0:-2])
	#reversing the list
	print(a[::-1])

Stride()

#operators on list
def operators():
	#[:] operator
	print(b[:]) #returns new object that is copy of b
	#python operators and buit inn function
	#the "in" and "not in" operators
	print('qux' in a) #in
	print('thud' not in a) #not in
	#concatination(+) and replication(*) operator
	a=a+['axe','iron'] #concatination
	print(a)
	c=c*2 #replication(*)
	print(c)
	#len(), min() and max() functions
	print('length of a is:', len(a)) #len()
	print("Minimun of b:",min(b))#min()
	print("Maximum of c:", max(c)) 	#max()

operators()

#nested lists
def nestedLists():
	x=['aaa',['b','c',['infinite']],'end']
	print('From x:',x)
	print('From x: length of x is::',len(x))
	print('x[0] :',x[0])
	print('x[1] :',x[1])
	print('x[2] :',x[2])
	print('Elements of sublists:')
	print('From x[1] of x[0] :',x[1][0])
	print('From x[1] of x[1] :',x[1][1])
	print('From x[1] of x[2] :',x[1][2])
	print('From x[1] of x[2] of x[1] :',x[1][2][0])

nestedLists()

#lists are muteable
#modifying a single list value
def modifyList():
	a[2]=10
	a[-1]=30
	print(a)
	#delete a string element
	del a[3]
	print(a)
	#modify multiple values
	a[1:4]=[1.1,2.3,2.4,3.5] #number of elements need not to be equals to the number of replaced elements 
	print(a)
	# can replace multiple elements in place of multiple using slice
	b[1:2]=[13,45,78]
	print(b)
	#can replace an elemet with a sublist
	c[3]=[2,6,9]
	#can insert elements without deleting anything
	g[1:1]=[30,90, 100]
	print(g)
	#can delete multiple elements out of the middle of a list by assigning
	#the appropriate slice to an empty list.
	c[1:3]=[]
	print(c)
	#also can use del keyword with that slice
	del c[1:3]
	print(c)

modifyList()

#Prepending and Appending elements of list, 
#done using +concatination operator or += operator
def concationationOp():
	# += operator
	a+=['great','gott']
	print(a)
	# +concatination
	b=[35, 79]+b
	print(b)
	#list can be concatinated with another list 
	# can concate a single element
	c += 'sound'
	print(c)

def appendOp():
	b=listorder()
	#append >> appends an object to a list .
	a.append(123)
	print(a)
	x=b.append(1023)
	print(x)
	print(b)
	# iterateable object appended as an single object
	a.append([1,3,4])
	print(a)


#extend()>> iterate the list with an object from the iterable
def extendOp():
	a.extend([1,2,3])
	print(a) # behaves like + operator 

#insert >> insert n object into a list
# a.insert(<index>, <obj>)
def insertOp():
	c.insert(2,'sun')
	print(c)

#remove >> removes an object from the list
#a.remove(obj)
def removeOp():
	d.remove(3)
	print(d)

#pop >> removes an element from the list
#a.pop(index=-1)
#must return the value that was removed
#a.pop() simply remove the last element from the list
def popOp():
	g.pop()
	print(g)
	g.pop(1)
	print(g)
	d.pop(-5)
	print(d)
