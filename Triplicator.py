import pandas as pd
import tkinter as tk
from tkinter import messagebox

#////////Triplicate Function///////////////////////
def triplicate():
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
    for i in range(1,col_count+1):    
        combo=[]
        
        #*********Change circulation number here!!!!!
        for j in range(3):
            combo.append(raw[str(i)])
                
        #Recombination   
        dict_mul[str(i)]=pd.concat(combo,axis=1).stack().reset_index()[0]

    #Concate the Triplicated Columns
    df=pd.concat([dict_mul[str(i)] for i in range(1,col_count+1)],
                 axis=1,
                 keys=names)

    #Output the Results to File
    df.to_csv('D:\\Database\\Export Triplicated.csv')

    messagebox.showinfo('Successful',
                        'Data triplicated and corresponding file successfully exported!')
    
#////////////////Quit Function////////////////////////////////   

def quiteit():
    root.destroy()

#////////////Main////////////////////////////////////
#Window Instance

root=tk.Tk()
root.geometry('600x200+200+100')
root.title('Triplicator')

#////////////Widgets/////////////////////////////////
#Labels
label=tk.Label(root, text='Please put the raw data file here:',
               font=20)
label.place(x=50,y=20)

label=tk.Label(root, text='D:\\Database\\Inventory of validation set_lung cancer.csv',
               font=20)
label.place(x=80,y=50)


#Buttons
#Triplicate Button
button=tk.Button(root, text='Triplicate',
                 command=triplicate,
                 width=20, height=2,
                 font=20)
button.place(x=100,y=100)

#Quit Button
button=tk.Button(root, text='Exit',
                 command=quiteit,
                 width=20, height=2,
                 font=20)
button.place(x=340,y=100)

root.mainloop()


