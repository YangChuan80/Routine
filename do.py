import pandas as pd
import xlrd
import xlsxwriter


sheet=['3uL_HP_0_A1_1','3uL_HP_0_A10_1','3uL_HP_0_A2_1','3uL_HP_0_A3_1',
       '3uL_HP_0_A4_1','3uL_HP_0_A6_1','3uL_HP_0_A7_1',
       '3uL_HP_0_A8_1','3uL_HP_0_A9_1','4uL_HP_0_A11_1','4uL_HP_0_A12_1',
       '4uL_HP_0_B1_1','4uL_HP_0_B10_1','4uL_HP_0_B12_1','4uL_HP_0_B3_1',
       '4uL_HP_0_B4_1','4uL_HP_0_B6_1','4uL_HP_0_B7_1','4uL_HP_0_B9_1',
       '5uL_HP_0_C1_1','5uL_HP_0_C10_1','5uL_HP_0_C2_1','5uL_HP_0_C3_1',
       '5uL_HP_0_C4_1','5uL_HP_0_C5_1','5uL_HP_0_C6_1','5uL_HP_0_C7_1',
       '5uL_HP_0_C8_1','5uL_HP_0_C9_1','6uL_HP_0_C11_1','6uL_HP_0_C12_1',
       '6uL_HP_0_D1_1','6uL_HP_0_D2_1','6uL_HP_0_D3_1','6uL_HP_0_D4_1',
       '6uL_HP_0_D5_1','6uL_HP_0_D6_1','6uL_HP_0_D7_1','6uL_HP_0_D8_1',
       '7uL_HP_0_D9_1','7uL_HP_0_E1_1','7uL_HP_0_E3_1','7uL_HP_0_E4_1',
       '7uL_HP_0_E6_1','7uL_HP_0_E7_1','7uL_HP_0_E9_1','7uL_HP_0_F1_1',
       '7uL_HP_0_F2_1','7uL_HP_0_F3_1',
       'STD_0_B11_1','STD_0_B2_1','STD_0_B5_1','STD_0_B8_1','STD_0_E2_1',
       'STD_0_E5_1','STD_0_E8_1']

data=pd.ExcelFile('D:\\Database\\Origianl Intensity.xls')
dict_merged={}
dffinal=pd.DataFrame(dict_merged)

for sheetname in sheet:
   dict_merged[sheetname]=data.parse(sheetname,skiprows=[0,1])


drop_columns=['time', 'SN', 'Quality Fac.', 'Res.', 'Area', 'Rel. Intens.', 'FWHM', 'Chi^2', 'Bk. Peak']

df_final=pd.DataFrame(dict_merged[sheet[0]].drop(drop_columns,axis=1),
                 columns=['m/z','Intens.','Tag'])
df_final['Tag']=sheet[0]

i=0
l=[]

for sheetname in  sheet[1:]:
   df=pd.DataFrame(dict_merged[sheetname].drop(drop_columns,axis=1),
                 columns=['m/z','Intens.','Tag'])
   df['Tag']=sheetname
   df.set_index(['Tag'])
   l.append(df)

df_concat=pd.concat(l,keys=sheet)
df_final=df_concat.drop(['Tag'],axis=1)

   


df_final.to_csv('D:\\Database\\Export Intensity.csv')

   
  
