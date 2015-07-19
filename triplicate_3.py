import pandas as pd

#Load Data from the File
raw=pd.read_csv('D:\\Database\\Inventory of validation set_lung cancer.csv',
                header=None,
                skiprows=[0])

#Count Length of the Columns
col_count=len(raw.columns)
names=[str(x) for x in range(1,col_count+1)]

#Rename the Columns
raw.columns=names

#Construct a Void Dictionary
dict_mul={}

#Triplicate the Values
for i in range(1,col_count+1):combo=[]; for j in range(3):combo.append(raw[str(i)]);dict_mul[str(i)]=pd.concat(combo,axis=1).stack().reset_index()[0]

#Concate the Triplicated Columns
df=pd.concat([dict_mul[str(i)] for i in range(1,col_count+1)],
             axis=1,
             keys=names)

#Output the Results to File
df.to_csv('D:\\Database\\Export Triplicated.csv')

print('Mission Accomplished!\n')
