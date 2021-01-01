import sys


#Exceptions versus Syntax Errors
print( 0 / 0 )

#Raising an exception
x = 10
if x > 5:
    #raise Exception('x should not exceed 5. The value of x was: {}'.format(x))

#The AssertionError Exception
#assert ('linux' in sys.platform), "This code runs on Linux only."

#The try and except Block: Handling Exceptions
def linux_interaction():
    assert ('linux' in sys.platform), "Function can only run on Linux systems."
    print('Doing something.')


#without try catch block
#linux_interaction()
# with try catch 
def practice():
	try:
		linux_interaction()
		with open('file.log') as file:
	    		read_data = file.read()
	    	
	#Exception FileNotFoundError
	#Raised when a file or directory is requested but doesn’t exist. Corresponds to errno ENOENT.
	except FileNotFoundError as fnf_error:
	    print(fnf_error)
	#except:
		#print('Could not open file.log')
	   #pass
	    #print('Linux function was not executed')
	except AssertionError as error:
		print(error)
		print('The linux_interaction() function was not executed')

#the else clause
def practices():
	try:
	    linux_interaction()
	except AssertionError as error:
	    print(error)
	else:
			#You can also try to run code inside the else clause and catch possible exceptions there as well:
	    print('Executing the else clause.')
		#try:
			#with open('file.log') as file:
			#	read_data = file.read()
	   	#except FileNotFoundError as fnf_error:
	    	#print(fnf_error)

#Cleaning Up After Using finally
def func():
	try:
	    linux_interaction()
	except AssertionError as error:
	    print(error)
	else:
	    try:
	        with open('file.log') as file:
	            read_data = file.read()
	    except FileNotFoundError as fnf_error:
	        print(fnf_error)
	finally:
	    print('Cleaning up, irrespective of any exceptions.')




#practice()
#practices()
func()