import xlrd
from pandas import DataFrame, Series

excel_obj=xlrd.open_workbook('D:\\Database\\original_unstacked.xlsx')

sheet0=excel_obj.sheet_by_index(0)

rownumber=sheet0.nrows
colnumber=sheet0.ncols

l=[]

for i in range(colnumber):
	l.extend(sheet0.col_values(i))

i=0

lr=[]

for l_item in l:
	if l_item!='':
		lr.append(l_item)
		
df=DataFrame(lr)

df.to_csv('D:\\DataBase\\stacked.csv')