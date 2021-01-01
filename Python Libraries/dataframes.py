import pandas as pd
from pandas import DataFrame

#A DataFrame represents a rectangular table of data and contains 
#an ordered collection of columns, 
#each of which can be a different value type (numeric, string, boolean, etc.).
#The DataFrame has both a row and column index; it can be thought of as 
#a dict of Series all sharing the same index. 
#Under the hood, the data is stored as one or more 
#two-dimensional blocks rather than a list, dict, 
#or some other collection of one-dimensional arrays.

#DataFrame from a dictionary: It is the most basic from of making a dataframe
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
df1 = pd.DataFrame(data)
print('DataFrame df1 is:\n',df1)

#head and tail method
def headAndTail():
	h=df1.head(2)
	print('Head of df1:\n',h)
	t=df1.tail(2)
	print('Tail of df1:\n',t)

#selecting particular columns from the data:
def particularData():
	df2=pd.DataFrame(data,columns=['year','pop'])
	#print('df2 is:\n',df2)
	return df2

#DataFrame functions: ‘loc’ and ‘iloc’ for rows.(df2.iloc[0])
def df_functions():
	df3=particularData()
	print('df3 is:\n',df3)
	print(df3['year']) # just display index/column names
	print(df3.year)
	# to select rows
	print('#######')
	print(df3.loc[2])


#delete columns and get the values:
def delColumn():
	df4=particularData()
	del df4['pop']
	print(df4.columns)
	print(df4.values)





#functional call
#headAndTail()
#particularData()
#df_functions()
#delColumn()
