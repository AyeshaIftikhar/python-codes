#tuples
#In Python, tuples are part of the standard language. 
#This is a data structure very similar to the list data structure. 
#The main difference being that tuple manipulation are 
#faster than list because tuples are immutable.

t = ('foo', 'bar', 'baz', 'qux', 'quux', 'corge')
print('tuple is :',t)
# can access using index nnumbers 
print('1st element of tuple is :',t[0])
# negative indexes will reservse the tuple order
print('element of tuple at t[-1]:',t[-1])
#slicing in tuples
print('slice of tuple:',t[1::2])
# all cases of slicing a list is applicable on tuples
# reverse of tuple
print('reverse is :',t[::-1])

#empty tuple
u= ()
#type(u)
print(u)

#mutiple inputs
v= (1, 2)
 #type(v)
#<class 'tuple'>
v = (1, 2, 3, 4, 5)
print(v)

#tuple packing and unpacking
#When unpacking, the number of variables on the left 
#must match the number of values in the tuple:

(s1, s2, s3, s4, s5) = v
print('s1',s1)
print('s2',s2)

#swapping 
a = 'full'
b = 'bark'
print('a and b:',a,b)

# We need to define a temp variable to accomplish the swap.
temp = a
a = b
b = temp
print('a and b after swapping:',a, b)