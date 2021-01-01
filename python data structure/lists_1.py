#list
a = ['foo','bar', 'baz', 'qax','pen']
print('list a:',a)

 #lists are ordered
b=['pen','baz','bar', 'foo', 'qax']  
if a == b:
	print('list a and b:',a,b)
else:
	print('list b:',b)

#list can contain arbitrary objects
c=[2,4,6,8]
print('list c:',c)

# varrying types of elements
d=[21,23,'football',3,4,6,'bark', False,3.14,'c']
print('list d:',d)

# empty and sigleton list
e=[]
f=['ayesha']
print('list e and f:',e,f)

#list objects don't need to be unique
g=['ayesha', 'kaynat', 'ayesha']
print('list g:',g)

#list objects can be accessed using index starting from 0
print('first element of g is',g[0])
print('2nd element of g is',g[1])
print('4th element of d is',d[3])

#negative list address counts from the end of the list 
print('element of g is',g[-1])

#slicing
print('From d:', d[2:9])
#negative indexes also specified
print('From d:',d[-7:-2])
#omitting the 1st index starts the slice at the begining of the list
print(d[:5],d[0:5]) # both works same
#omitting the 2nd index extends the slice to the end of the list
print(d[2:], d[2:10]) # both are same
print(d[:5]+d[5:])

#can specify a stride-- either positive or negative
print(a[0:3:4])
print(a[1:3:4])
print(a[2:3:4])
print(a[6:0:-2])

#reversing the list
print(a[::-1])

#[:] operator
print(b[:]) #returns new object that is copy of b

#python operators and buit inn function
#the "in" and "not in" operators
print('qux' in a) #in
print('thud' not in a) #not in

#concatination(+) and replication(*) operator
#concatination
a=a+['axe','iron']
print(a)
#replication(*)
c=c*2
print(c)

#len(), min() and max() functions
#len()
print('length of a is:', len(a))
#min()
print("Minimun of b:",min(b))
#max()
print("Maximum of c:", max(c))


#nested lists
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

#lists are muteable
#modifying a single list value
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
#can delete multiple elements out of the middle of a list by assigning the appropriate slice to an empty list.
c[1:3]=[]
print(c)
#also can use del keyword with that slice
del c[1:3]
print(c)

#Prepending and Appending elements of list, done using +concatination operator or += operator
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
a.extend([1,2,3])
print(a) # behaves like + operator 

#insert >> insert n object into a list
# a.insert(<index>, <obj>)
c.insert(2,'sun')
print(c)

#remove >> removes an object from the list
#a.remove(obj)
d.remove(3)
print(d)

#pop >> removes an element from the list
#a.pop(index=-1)
#must return the value that was removed
#a.pop() simply remove the last element from the list
g.pop()
print(g)
g.pop(1)
print(g)
d.pop(-5)
print(d)
#lists are dynamics

