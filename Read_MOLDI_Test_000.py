import xlrd
import pandas as pd
import numpy as np
import tkinter
import re
import scipy.stats
import matplotlib.pyplot as plt


normal_mzs=[1526, 1536, 2791, 2819]
normal_rows=len(normal_mzs)

tkinter.Tk().withdraw()
filename=tkinter.filedialog.askopenfilename()

book=xlrd.open_workbook(filename)
nsheets=book.nsheets
sheet_names=book.sheet_names()
sheets={}

for sheet_name in sheet_names:    
    nrows=book.sheet_by_name(sheet_name).nrows
    current_header=book.sheet_by_name(sheet_name).row_values(2)
    current_data=[book.sheet_by_name(sheet_name).row_values(i) for i in range(3, nrows)]
    sheets[sheet_name]=pd.DataFrame(current_data, columns=current_header)

def detect(mzs):
    mzs_missing=[]
    
    for normal_mz in normal_mzs:
        for mz in mzs:
            if mz<normal_mz+6 and mz>normal_mz-6:
                break
        else:
            mzs_missing.append(normal_mz)
    return mzs_missing                

for sheet_name in sheet_names:
    df=sheets[sheet_name]

    actual_rows=len(df.index)

    if actual_rows<normal_rows:
        mzs=list(df['m/z'])
        mzs_missing=detect(mzs)

        i=actual_rows

        for mz_missing in mzs_missing:
            df.ix[i]=0
            df['m/z'].ix[i]=mz_missing
            i+=1

    df=df.sort_index(by='m/z')
    df=df.reset_index().drop('index', axis=1)

    hep_ratio=df['Area'].ix[2]/df['Area'].ix[3]
    saa_ratio=df['Area'].ix[0]/df['Area'].ix[1]

    patt=r'[\D\d]+_0_'
    name=re.findall(patt, sheet_name)[0].replace('_0_', '').replace('-', '_')    

    df['name']=name
    df['hep/hhep']=hep_ratio
    df['SAA/IS_SAA']=saa_ratio

    sheets[sheet_name]=df

df=pd.concat([sheets[sheet_name] for sheet_name in sheet_names], keys=sheet_names)

names=list(df['name'].unique())

df['hep avg']=np.nan
df['hep std']=np.nan

df['SAA avg']=np.nan
df['SAA std']=np.nan

df=df.reset_index()

for name in names:
    avg=df['hep/hhep'][df['name']==name].mean()
    df['hep avg'][df['name']==name]=avg

    std=df['hep/hhep'][df['name']==name].std()
    df['hep std'][df['name']==name]=std

    #////////////////////////////////////////////
    
    avg=df['SAA/IS_SAA'][df['name']==name].mean()
    df['SAA avg'][df['name']==name]=avg

    std=df['SAA/IS_SAA'][df['name']==name].std()
    df['SAA std'][df['name']==name]=std

    #//////////////////////////////////////////

    df['SAA std'][df['level_1']==1]=np.nan
    df['SAA std'][df['level_1']==2]=np.nan
    df['SAA std'][df['level_1']==3]=np.nan

    df['SAA avg'][df['level_1']==1]=np.nan
    df['SAA avg'][df['level_1']==2]=np.nan
    df['SAA avg'][df['level_1']==3]=np.nan

    df['hep std'][df['level_1']==1]=np.nan
    df['hep std'][df['level_1']==2]=np.nan
    df['hep std'][df['level_1']==3]=np.nan

    df['hep avg'][df['level_1']==1]=np.nan
    df['hep avg'][df['level_1']==2]=np.nan
    df['hep avg'][df['level_1']==3]=np.nan

    df['SAA/IS_SAA'][df['level_1']==1]=np.nan
    df['SAA/IS_SAA'][df['level_1']==2]=np.nan
    df['SAA/IS_SAA'][df['level_1']==3]=np.nan

    df['hep/hhep'][df['level_1']==1]=np.nan
    df['hep/hhep'][df['level_1']==2]=np.nan
    df['hep/hhep'][df['level_1']==3]=np.nan

df.to_csv('combined.csv')
print('Done!')
