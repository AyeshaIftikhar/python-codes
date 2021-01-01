#Types of functions
#Built-in functions,
# such as help() to ask for help,
# min() to get the minimum value,
# print() to print an object to the terminal,… 
#User-Defined Functions (UDFs), 
#which are functions that users create to help them out; And
#Anonymous functions, 
#which are also called lambda functions 
#because they are not declared with the standard def keyword.

#Fun actions vs. Methods
# Define a function `plus()`
def plus(a,b):
  return a + b
  
# Create a `Summation` class
class Summation(object):
  def sum(self, a, b):
    self.contents = a + b
    return self.contents 


#user defined functins
def hello():
  #print("Hello World") 
  	#can add loops, flow control and more in functions...
  name = str(input("Enter your name: "))
  if name:
    print ("Hello " + str(name))
  else:
    print("Hello World") 
  return 

def hello1():
  print("Hello World") 
  return("hello")

def hello_noreturn():
  print("Hello World")

# functions immediately exit when they come across a return statement, 
#even if it means that they won’t return any value:
def run():
  for x in range(10):
     if x == 2:
      return
  print("Run!")

#Another thing that is worth mentioning 
#when you’re working with the return statement is the fact
#that you can use it to return multiple values. 
#To do this, you make use of tuples.
def plus(a,b,c):
  sum = a + b + c
  return (sum, a)

#How To Add Docstrings To A Python Function
def hello3():
	"""Prints "Hello World".

	Returns:
	    None
	"""
	print("Hello World") 
	return 

#Function Arguments in Python
#Default Arguments
#Default arguments are those that take a default value if no argument value is passed during the function call.
# Define `plus()` function
def add(a,b = 2):
  return a + b

#Required Arguments
#the required arguments of a UDF are those that have to be in there. 
#These arguments need to be passed during the function call and in precisely the right order,
# Define `plus()` with required arguments
def addition(a,b):
  return a + b

#Keyword Arguments
#If you want to make sure that you call all the parameters in the right order,
#you can use the keyword arguments in your function call. 
#You use these to identify the arguments by their parameter name.
# Define `subtract()` function
def subtract(a,b):
  return a - b

#Variable Number of Arguments
#In cases where you don’t know the exact number of arguments that you want to pass to a function, 
#you can use the following syntax with *args:
# Define `plus()` function to accept a variable number of arguments
def sumation(*args):
 # return sum(args)# using built in function sum
	#avoiding built in function sum
	total = 0
	for i in args:
		total += i
	return total

#Global vs Local Variables
# Global variable `init`
init = 1

# Define `plus()` function to accept a variable number of arguments
def plus1(*args):
  # Local variable `sum()`
  total = 0
  for i in args:
    total += i
  return total
  
# Access the global variable
print("this is the initialized value " + str(init))
# (Try to) access the local variable
#print("this is the sum " + str(total))

#Anonymous Functions in Python
#Anonymous functions are also called lambda functions in Python
#because instead of declaring them with the standard def keyword, 
#you use the lambda keyword.
double = lambda x: x*2
#print(double(5))

# `sum()` lambda function
sum1 = lambda x, y: x + y;
# Call the `sum()` anonymous function
#print(sum1(4,50))

#You use anonymous functions when you require a nameless function for a short period of time, 
#and that is created at runtime. 
#Specific contexts in which this would be relevant is when you’re working with filter(), map() and reduce():
from functools import reduce

my_list = [1,2,3,4,5,6,7,8,9,10,22]
# Use lambda function with `filter()`
filtered_list = list(filter(lambda x: (x*2 > 10), my_list))
# Use lambda function with `map()`
mapped_list = list(map(lambda x: x*2, my_list))
# Use lambda function with `reduce()`
reduced_list = reduce(lambda x, y: x+y, my_list)

#print(filtered_list)
#print(mapped_list)
#print(reduced_list)

#Using main as function
def main():
  hello3()
  print("This is a main function")

#besides the __main__ function, 
#you also have an __init__ function that initializes an instance of a class or an object.
 
# Execute `main()` function 
if __name__ == '__main__':
  main()
#calling main()
#main()

# Calculate the sum
#print(sumation(1,4,5,100))
# Call `subtract()` function with keyword arguments
#print(subtract(a=1000, b=200))

#print(addition(30,59))

# Call `plus()` with only `a` parameter
#print(add(a=60))
# Call `plus()` with `a` and `b` parameters
#print(add(a=4, b=50))

#hello3()

# Call `plus()` and unpack variables 
#sum, a = plus(50,19,30)
# Print `sum()`
#print(sum)

#r=plus(1,3)
#print(r)
#SumInstance=Summation()
#result=SumInstance.sum(4,7)
#print(result)
#print(hello())
#print(hello1())
#hello_noreturn()

# Multiply the output of `hello()` with 2 
#hello1() * 2
# (Try to) multiply the output of `hello_noreturn()` with 2 
#hello_noreturn() * 2
#print(run())