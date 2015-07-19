import xlrd
from pandas import DataFrame, Series

data=xlrd.open_workbook('D:\\Database\\letters.xls')
table=data.sheet_by_index(0)

rownumber=table.nrows

l=[]

for i in range(rownumber):
	l.append(table.row_values(i)[0].rstrip())

lowerletters=[]
	
for it in l:
	lowerletters.append(it.lower())
	
df=DataFrame(lowerletters)
	
df.to_csv('D:\\Database\\lowercase.csv')