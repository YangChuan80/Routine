import xlrd
import pandas as pd
import numpy as np
import re
import warnings
import sys
import time

#/////Start Timing/////////////////////////////
start_time=time.time()

#/////Ignoring Warnings///////////////////////
warnings.filterwarnings("ignore")

#/////Default Peaks////////////////////////////
normal_mzs=[1526, 1536, 2791, 2819]
normal_rows=len(normal_mzs)

filename='.\\Raw MALDI.xlsx'
book=xlrd.open_workbook(filename)
print('Source file: '+sys.path[0]+filename+' loaded!')

#///Extraction////////////////////////////////////////////
nsheets=book.nsheets

sheet_names=book.sheet_names()
sheets={}

for sheet_name in sheet_names:    
    nrows=book.sheet_by_name(sheet_name).nrows
    current_header=book.sheet_by_name(sheet_name).row_values(2) 
    current_data=[book.sheet_by_name(sheet_name).row_values(i) for i in range(3, nrows)]
    sheets[sheet_name]=pd.DataFrame(current_data, columns=current_header)   #///DataFrame Construction////////

#///////////////////////////////////////////////////////////////////////////////////////////////////////
#///Function: Finding Missed Peak///////
def detect_missed(mzs):
    mzs_missing=[]
    
    for normal_mz in normal_mzs:
        for mz in mzs:
            if mz<normal_mz+6 and mz>normal_mz-6:   #Searching in this range
                break
        else:
            mzs_missing.append(normal_mz)
    return mzs_missing

#///Function: Finding Redundant Peak////////
def detect_redundant(mzs):
    mzs_adjacents=[]    

    for normal_mz in normal_mzs:
        d=10
        m=0
        for mz in mzs:
            if abs(normal_mz-mz)<d:
                d=abs(normal_mz-mz)
                m=mz
        mzs_adjacents.append(m)

    for mzs_adjacent in mzs_adjacents:
        mzs.remove(mzs_adjacent)

    return mzs

#///Function: Make certain cells blank/////////////
def blank():
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

    df['SAA CV'][df['level_1']==1]=np.nan
    df['SAA CV'][df['level_1']==2]=np.nan
    df['SAA CV'][df['level_1']==3]=np.nan

    df['hep CV'][df['level_1']==1]=np.nan
    df['hep CV'][df['level_1']==2]=np.nan
    df['hep CV'][df['level_1']==3]=np.nan

    df['name'][df['level_1']==1]=np.nan
    df['name'][df['level_1']==2]=np.nan
    df['name'][df['level_1']==3]=np.nan
        
    df['hep avg'][df['Tail']%2==0]=np.nan
    df['SAA avg'][df['Tail']%2==0]=np.nan
    df['hep std'][df['Tail']%2==0]=np.nan
    df['SAA std'][df['Tail']%2==0]=np.nan
    df['hep CV'][df['Tail']%2==0]=np.nan
    df['SAA CV'][df['Tail']%2==0]=np.nan

    df['tag'][df['level_1']==1]=np.nan
    df['tag'][df['level_1']==2]=np.nan
    df['tag'][df['level_1']==3]=np.nan
    df['tag'][df['Tail']%2==0]=np.nan

#/////Feedback//////////////////////
print('Wrangling...')

#///////////////////Main Loop///////////
peak_missing_amount=0
peak_redundant_amount=0
peak_redundant_item=[]
peak_missing_item=[]

for sheet_name in sheet_names:
    df=sheets[sheet_name]

    actual_rows=len(df.index)    

    if actual_rows<normal_rows:
        mzs=list(df['m/z'])
        mzs_missing=detect_missed(mzs)

        i=actual_rows
        
        for mz_missing in mzs_missing:
            df.ix[i]=0
            df['m/z'].ix[i]=mz_missing
            i+=1
        peak_missing_amount+=1
        peak_missing_item.append(sheet_name.replace('_0_', ' @ ').replace('_1', ''))
            
    elif actual_rows>normal_rows:
        mzs=list(df['m/z'])
        mzs_redundant=detect_redundant(mzs)

        for mz_redundant in mzs_redundant:
            df=df.drop(df[df['m/z']==mz_redundant].index)
            
        peak_redundant_amount+=1
        peak_redundant_item.append(sheet_name.replace('_0_', ' @ ').replace('_1', ''))
        

    df=df.sort_index(by='m/z')
    df=df.reset_index().drop('index', axis=1)

    hep_ratio=df['Area'].ix[2]/df['Area'].ix[3]
    saa_ratio=df['Area'].ix[0]/df['Area'].ix[1]

    #Regular Expressions////Matching Sample Names
    patt=r'[\D\d]+_0_'
    name=re.findall(patt, sheet_name)[0].replace('_0_', '').replace('-', '_')

    #Regular Expressions////Matching Vial NOs
    patt1=r'_0_[\D\d]+_1$'
    id=re.findall(patt1, sheet_name)[0].replace('_0_', '').replace('_1', '')

    #Regular Expressions////Matching Tails of the Vials
    patt2=r'\d+$'
    tail=int(re.findall(patt2, id)[0])

    if len(id)==2:
        id=id[0]+'0'+id[1]

    df['Tail']=tail
    df['id']=id
    df['name']=name
    df['hep/hhep']=hep_ratio
    df['SAA/IS_SAA']=saa_ratio
    df['tag']=name

    sheets[sheet_name]=df


#///////////////////Combining DataFrame///////////////////////
    #|||||||||Feedback: Combining|||||||||||||||||||||||||
print('Combining...')
df=pd.concat([sheets[sheet_name] for sheet_name in sheet_names], keys=sheet_names)

#|||||||||Feedback: Start Parsing|||||||||||||||||||||||||
print('Parsing...')

#////去重///////////////////////
names=list(df['name'].unique())

#///Description Statistics Initialization/////////////
df['hep avg']=0
df['hep std']=0
df['hep CV']=0

df['SAA avg']=0
df['SAA std']=0
df['SAA CV']=0

#///Change the sheetnames from indeces into column names
df=df.reset_index()

#////////Loop of Processing Data in the Same Names///////////////
for name in names:
    avg=df['hep/hhep'][df['name']==name].mean()
    df['hep avg'][df['name']==name]=avg

    std=df['hep/hhep'][df['name']==name].std()
    df['hep std'][df['name']==name]=std

    cv=std*100/avg
    df['hep CV'][df['name']==name]=cv

    #////////////////////////////////////////////
    
    avg=df['SAA/IS_SAA'][df['name']==name].mean()
    df['SAA avg'][df['name']==name]=avg

    std=df['SAA/IS_SAA'][df['name']==name].std()
    df['SAA std'][df['name']==name]=std

    cv=std*100/avg
    df['SAA CV'][df['name']==name]=cv

    #/////////////////////////////////////////////

    if name.find('standard') != -1 or name.find('Standard') != -1:
        tag=name.replace('standard', '').replace('Standard', '').replace('_', '').replace(' ', '')
        df['tag'][df['name']==name]=tag        

#////Calling Function////////////////////////////
print('Trimming...')
blank()

#/////Sorting////////////////////////
df=df.sort_index(by=['id', 'level_1'])
df=df.set_index('level_0')

#/////Output///////////////////////////////////////
df.to_csv('.\\combined.csv')

#///Function: Layout Display///////////
def layout(names):
    layout_names=[]
    layout_series=[]
    for name in names:
        patt4=r'[\D\d]+_0_'
        sample_name=re.findall(patt4, name)[0].replace('_0_', '')
        
        if sample_name.find('standard')!=-1 or sample_name.find('Standard')!=-1:
            sample_name=sample_name.replace('standard', '').replace('Standard', '').replace('_', '')       

        patt5=r'_0_[\D\d]+_1$'
        id_name=re.findall(patt5, name)[0].replace('_0_', '').replace('_1', '')

        if len(id_name)==2:
            id_name=id_name[0]+'0'+id_name[1]

         
        layout_names.append((id_name, sample_name))

    d=96-len(layout_names)

    for i in range(d):
        layout_names.append(('Z'+str(i),np.nan))

    sample_dict=dict(layout_names)
    s=pd.Series(sample_dict).sort_index()
    df=pd.DataFrame(np.array(s).reshape(8,12),
                           columns=[1,2,3,4,5,6,7,8,9,10,11,12],
                           index=['A','B','C','D','E','F','G','H'])
    return df

dfl=layout(sheet_names)

#/////Final Feedback////////////////////
print('\nDone!\n')
print('Plate Layout:')
print(dfl, '\n')
print('Total Sample Amount: ', nsheets)
print('\tPeak Missing: ', peak_missing_amount)
print('\t\tMissing Item(s): ', peak_missing_item, '\n')
print('\tPeak Redundant: ', peak_redundant_amount)
print('\t\tRedundant Item(s): ', peak_redundant_item, '\n')
print('Document Exported: ', sys.path[0]+'\\combined.csv.\n')
print('Total Runing Time: ', time.time()-start_time, 'seconds.')
