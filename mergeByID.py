#This script reads data from two different excel sheet and
#then merge them based on ID and present o/p in another Excel sheet

#It requires "pandas" moduled to be imported
# Use pip install pandas
# also it required xlrd module to be installed
# use pip install xlrd
import pandas as pd


file1 = 'sheet1.xlsx'
file2 = 'sheet2.xlsx'
# the output is written in result.xlsx file, if file not there, it creates one
dest_file = 'result.xlsx'

#read data frame of file1
s1 = pd.read_excel(file1)
print s1.set_index('ID')
#set_index is used to print the data based on ID, instead of index

#read data frame of file2
s2 = pd.read_excel(file2)
print s2.set_index('ID')

#merging the data gram based on ID
merged = s1.merge(s2, on="ID", how="outer")
print merged.set_index('ID')
merged.set_index('ID').to_excel(dest_file)
