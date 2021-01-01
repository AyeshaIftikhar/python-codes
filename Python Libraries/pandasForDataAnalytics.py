#A Data frame is a two-dimensional data structure, 
#i.e., data is aligned in a tabular fashion in rows and columns

import numpy as np
import pandas as pd
from pandas import DataFrame,Series
from openpyxl.workbook import Workbook

#series 
ser1 = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
#print('series is:',ser1)

#reindexing
def reindexing():
	ser_new=ser1.reindex(['a','b','c','d'])
	print('series after reindexing is:',ser_new)

#dataFrames
dframe1 = pd.DataFrame(np.arange(9.).reshape((3, 3)), columns=list('bcd'),index=['Ohio', 'Texas', 'Colorado'])
dframe2 = pd.DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'),index=['Utah', 'Ohio', 'Texas', 'Oregon'])

#Arithematic operations on dataframe
def ArithematicOp():
	print('dataframe1 is:',dframe1)
	print('dataframe2 is:',dframe2)
	print('union of dataframe:',dframe1+dframe2)  ##union
	print('intersection of dataframes:',dframe1-dframe2)  ## simple substraction

#Apply user defined functions on DataFrame
def userDefinedFun():
	f = lambda x: x.max() - x.min()
	print(dframe1.apply(f))
	print('######################')
	print(dframe1.apply(f,axis='columns'))

#sorting
def Sorting():
	df1 = pd.DataFrame(np.arange(9.).reshape((3, 3)), columns=list('bcd'),index=['Ohio', 'Texas', 'Colorado'])
	print(df1)
	print(df1.sort_index())
	print(df1.sort_index(axis=1))
	print('####################')
	print(df1.sort_values(by=['d','c','b']))

# Removing rows and columns: axis=0 for rows and axis=1 for columns
def removeRowAndColumn():
	print(dframe1)
	print(dframe1.drop('b',axis=1)) #removes b column
	print(dframe1.drop('Ohio',axis=0)) #removes Ohio row

#set and reset index:
def setAndreset():
	#condition set and reset index
	dframe3=pd.DataFrame(np.random.randn(4,3),index=list('abcd'),columns=list('wxy'))
	print(dframe3)
	print(dframe3[dframe3['w']>0])
	print(dframe3.reset_index())
	#set new column as index
	dframe3['ID']=['AS1','AS2','AS3','AS4'] # create a new column id
	print(dframe3)
	print(dframe3.set_index('ID')) #set index as id

# Missing Data (dropna() and fillna()),
#groupby,count,describe: axis=0 to drop rows 
#with NaN/Null ,axis=1 to drop columns with NaN/Null
def MissingData():
	dt={'a':[1,np.nan,3],'b':[10,np.nan,2],'c':[0,5,2]}
	dt=pd.DataFrame(dt)
	print(dt)
	print(dt.dropna()) #skip the entire index having null values
	print(dt.dropna(axis=1)) #only column having na null
	print(dt.fillna('100')) 
	#fill with mean value
	dt['a'].fillna(dt['a'].mean())
	#count,describe , groupby
	print(dt.count()) # just count values
	print(dt.describe()) # define all mean, standard deviation,etc

 #Read/Write CSV/HTML/Excel:
def readFile():
	#read_csv() function will read the data from CSV(Comma separated file) file
	df=pd.read_csv('Files/example.csv') 
	#read_excel() function will read data from excel file and you always 
	#need to specify the sheet number from which you want to read the data
	df=pd.read_excel('Files/excel_output.xlsx',sheet_name='Sheet1')

	##writing
	#to_csv() function will write data as CSV format
	df.to_csv('new_df.csv',index=False)
	#to_excel() will write data to excel sheet
	df.to_excel('output.xlsx',sheet_name='sheet1')

#correlation and covariance:
#A positive covariance/correlation means that the two variables at hand are positively related, 
#and they move in the same direction.
#A negative covariance /correlation means that the variables are inversely related, or that they move in opposite directions.
def CorrelationAndCovariance():
	dt={'a':[1,np.nan,3],'b':[10,np.nan,2],'c':[0,5,2]}
	dt=pd.DataFrame(dt)
	print(dt.corr()) #correlation
	print(dt.cov()) #covarience




#function call
#reindexing()
#ArithematicOp()
#userDefinedFun() 
#Sorting()
#removeRowAndColumn()
#CorrelationAndCovariance()
#setAndreset()
#MissingData()
readFile()
