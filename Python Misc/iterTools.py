#iterTool
#built-in zip() function, which takes any number of iterables as arguments 
#and returns an iterator over tuples of their corresponding elements:
z=list(zip([1, 2, 3], ['a', 'b', 'c']))
print(z)

#The iter() built-in function, when called on an iterable, returns an iterator object for that iterable:
z1=iter([1, 2, 3, 4])
print(z1)

#The map() built-in function is another “iterator operator” that, in its simplest form, 
#applies a single-parameter function to each element of an iterable one element at a time:
z2=list(map(len, ['abc', 'de', 'fghi']))
print(z2)

#Since iterators are iterable,
#you can compose zip() and map() to produce an iterator over combinations of elements in more than one iterable. 
z3=list(map(sum, zip([1, 2, 3], [4, 5, 6])))
print(z3)

#Taking a naive approach, you might write something like this:
def naive_grouper(inputs, n):
    num_groups = len(inputs) // n
    return [tuple(inputs[i*n:(i+1)*n]) for i in range(num_groups)]

#list and tuple in  naivegrouper
def better_grouper(inputs, n):
    iters = [iter(inputs)] * n
    return zip(*iters)

#the grouper recipe
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(better_grouper(nums,3)
#iters = [iter(nums)] * 2
#print(list(id(itr) for itr in iters))     

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(naive_grouper(nums,2))
