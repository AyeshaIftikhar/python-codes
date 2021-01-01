#String Manipulation
s = 'foo'
t = 'bar'
u = 'baz'
#String perators#The + Operator
#The + operator concatenates strings. 
#It returns a string consisting of the operands joined together
def plusOperator():
	print('s and t:',s + t)
	print('s,t and u combined:',s + t + u)
	print('Go team' + '!!!')

#The * Operator#The * operator creates multiple copies of a string. 
#If s is a string and n is an integer,
#either of the following expressions returns a string consisting 
#of n concatenated copies of s:
#both are same s * n ,n * s
def MultiplyOperator():
	print(s*4)
	print(4*t)
	#The multiplier operand n must be an integer. 
	#You’d think it would be required to be a positive integer,
	#it can be zero or negative,#in which case the result is an empty string:
	print(u*-8)

#The in Operator
#Python also provides a membership operator that can be used with strings. 
#The in operator returns True if the first operand is contained within the second, 
#and False otherwise:
def inOperator():
	print(s in 'That\'s food for thought.')
	print( s in 'That\'s good for now.')

#There is also a not in operator, which does the opposite:
def notInOperator():
	print('z' not in 'abc')
	print( 'z' not in 'xyz')

#Built-in String FUnctions
#ord(c)
#Returns an integer value for the given character.
def OrdInOperator():
	#returns code in ASCII(string to ascii code conversion)
	print(ord('c'))
	print(ord('$'))
	print(ord('~'))
	#Returns unicode
	print(ord('€'))
	print(ord('∑'))

#char(n)
#Returns a character value for the given integer.(ascii to character conversion)
def CharNOperator():
	#ASCII
	print(chr(35))
	print(chr(255))
	print(chr(97))
	print(chr(98))

#len(s)
#Returns the length of a string.
def lengthOp():
	 a = 'I am not a string.'
	 print(len(a))

#str(obj)
#Returns a string representation of an object.
def STROp():
	print(str(49.2))
	print(str(3+4j))
	print(str(3 + 29))
	print(str('ayesha'))

#String Indexing
d=s+t
def StringIndexing():
	print('string is:',d)
	print('length of d:',len(d))
	print('0 index:',d[0])
	print('1 index:',d[1])
	print('d[len(s)-1]:', d[len(s)-1])
		#Attempting to index beyond the end of the string results in an error:
		#String indices can also be specified with negative numbers,
		# in which case indexing occurs from the end of the string backward
	print('-1 index:',d[-1])
	print('d[-len(d)]:',d[-len(d)])#reverse index with -
		#Attempting to index with negative numbers beyond the start of the string results in an error:
#StringIndexing()

#String slicing
def StringSlicing():
	print('slice:',d[2:5])
	print('d[:4]:',d[:4])
	#Slicing of string is same as slicing of a list
	#Omitting both indices returns the original string, in its entirety. Literally.
	# It’s not a copy, it’s a reference to the original string:
	res1= d[:]
	print(res1)
	print(id(d))
	print(id(t))
	#is operatora 
	print(d is res1)

#StringSlicing()

#Interpolating Variables Into a String
def interpolatingVar():
	n = 20
	m = 25
	prod = n * m
	print('The product of', n, 'and', m, 'is', prod)

#interpolatingVar()

#f-string
def Usef_string():
	n = 20
	m = 25
	prod = n * m
	print(f'The product of {n} and {m} is {prod}')

#Modifying Strings
#In a nutshell, you can’t. 
#Strings are one of the data types Python considers immutable, 
#meaning not able to be changed
def Modifying_String():
	q='fooxball'
	print(q)
	#q= q[:3] + 't' + q[4:]
	#using builtin method replace() 
	q = q.replace('x', 't')# first argument is the character to be replaced 
	#and 2nd is the one with 1st is going to replaced
	print(q)

#Modifying_String()

#case conversion
def Case_Conversion():
	st='The sun also rises'
	print('string is:',d)
	print("other string is:",st)
	print('capitalize:',d.capitalize())
	print('lower case',d.lower())
	print('swap the cases',st.swapcase()) #swap cases of alphabatic characters
	print('in title form',st.title())
	print('upper case letters',st.upper())
	print(st.count('o')) #Counts occurrences of a substring in the target string.
	print(d.endswith('bar'))
	 #Determines whether the target string ends with a given substring.
	print(st.endswith('lso', 0, 4))
	print('foo bar foo baz foo qux'.index('foo')) 
	#print index of the string
	print(st.rfind('o')) 
	#Searches the target string for a given substring starting at the end.
	#print(st.find(a)) 
	#Searches the target string for a given substring.
	print(d.rindex('f')) 
	#Searches the target string for a given substring starting at the end.
	print(st.startswith('a')) 
	#Determines whether the target string starts with a given substring.

#Case_Conversion()

# Find and Replace
#These methods provide various means of searching the target string 
#for a specified substring.

#character classification
#Methods in this group classify a string based on the characters it contains.
def character_classification():
	print(d.isalnum()) 
#Determines whether the target string consists of alphanumeric characters.
	print(t.isalpha())
#Determines whether the target string consists of alphabetic characters.
	print(u.isdigit())
#Determines whether the target string consists of digit characters
	print(s.isidentifier())
#Determines whether the target string is a valid Python identifier.
	print(d.islower()) 
#Determines whether the target string’s alphabetic characters are lowercase.
	print(s.isprintable()) 
#Determines whether the target string consists entirely of printable characters.
	print(t.isspace()) 
#Determines whether the target string consists of whitespace characters.
	print(d.istitle()) 
#Determines whether the target string is title cased.
	print(u.isupper()) 
#Determines whether the target string’s alphabetic characters are uppercase.
	print(t.center(4)) 
#Centers a string in a field.
	print(d.expandtabs()) 
#Expands tabs in a string.
	print(t.ljust(10)) 
#Left-justifies a string in field.
	print(u.lstrip()) 
#Trims leading characters from a string.
	print(d.replace('foo','bat'))
#Replaces occurrences of a substring within a string.
	print(t.rjust(10)) 
#Right-justifies a string in a field.
	print(u.rstrip())
 #Trims trailing characters from a string.
	print(t.strip())
 #Strips characters from the left and right ends of a string.
	print(s.zfill(6)) 
#Pads a string on the left with zeros.

#Converting Between Strings and Lists
def Convert_StringtoList():
	print('d '.join(['foo', 'bar', 'baz', 'qux']))
#Concatenates strings from an iterable.
	print('foo##bar##baz'.partition('##'))
#Divides a string based on a separator.
	print('foo@@bar@@baz'.rpartition('@@'))
#Divides a string based on a separator.
	print('foo\n\tbar   baz\r\fqux'.rsplit()) 
#Splits a string into a list of substrings.
	print('www.realpython.com'.split('.', maxsplit=1))
#Splits a string into a list of substrings.
	print('foo\f\f\fbar'.splitlines())
#Breaks a string at line boundaries.

#Convert_StringtoList()

#the byte objects
def byte_objects():
	#Defining a Literal bytes Object	
	b = b'foo bar baz'
	print(b)
	#As with strings, you can use any of the single, double, or triple quoting mechanisms:
	print( b'Contains embedded "double" quotes')
	print(b"Contains embedded 'single' quotes")
	print( b'''Contains embedded "double" and 'single' quotes''')
	print(b"""Contains embedded "double" and 'single' quotes""")
	#Only ASCII characters are allowed in a bytes literal. 
	#Any character value greater than 
	#127 must be specified using an appropriate escape sequence:

#byte_objects()

#Defining a bytes Object With the Built-in bytes() Function
def builtin_bytes():
	b = bytes('foo.bar', 'utf8')#Creates a bytes object from a string.
	c = bytes(8)#Creates a bytes object consisting of null (0x00) bytes.
	d = bytes([100, 102, 104, 106, 108])#Creates a bytes object from an iterable.
	print('byte object from an iterable',d)
	print('bytes consisting of null',c)
	print('byte object from a string',b)

#builtin_bytes()

#Operations on bytes Objects
def operationsOnByte():
	#The in and not in operators:
	b = b'abcde'
	print( b'cd' in b)
	print(b'foo' not in b)
	#The concatenation (+) and replication (*) operators:
	print(b + b'fghi')
	print(b*5)
	#Indexing and slicing:
	print(b[2])
	print(b[1:5])
	#Built-in functions:
	print('Length:',len(b),'Maximum:',max(b),'Minimum:',min(b))
	#all opertion of string can be implemented on bytes
	#Returns a bytes object constructed from a string of hexadecimal values.
	d = bytes.fromhex(' aa 68 4682cc ')
	print(d)
	print(d.hex())#Returns a string of hexadecimal value from a bytes object.
	#bytearray Objects
	ba = bytearray('foo.bar.baz', 'UTF-8')
	print(ba)


#function calls

#operationsOnByte()
#builtin_bytes()
#byte_objects()
#Convert_StringtoList()
#character_classification()
#Case_Conversion()
#Modifying_String()
#Usef_string()
#interpolatingVar()
#StringSlicing()
#StringIndexing()
#STROp()
#lengthOp()
#CharNOperator()
#OrdInOperator()
#notInOperator()
#inOperator()
#MultiplyOperator()
#plusOperator()