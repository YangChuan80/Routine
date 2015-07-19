import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox

#Button Method:
def matrixplot():
    #Import

    try:
        df=pd.read_csv('D:\\Database\\import_file.csv',
                       header=None)

    except OSError:
        messagebox.showinfo('File Read Error',
                            'Please put the file in the director above and as such that name! Thanks!')
    else:
        xvalue=len(df.columns)
        yvalue=len(df.index)

        product=xvalue*yvalue

        #Recombinate the dataframe
        df1d=df.stack().reset_index()

        df1d.columns=['y','x','vaules']

        #Create the figure object
        fig=plt.figure()

        plt.axis([0,xvalue+1,yvalue+1,0])

        #Subplot ax
        ax=fig.add_subplot(1,1,1)

        #Normalization
        normalized=2*df.max().max()

        #Plot
        for i in range(product):
            circle=plt.Circle((df1d.x.ix[i]+1,df1d.y.ix[i]+1),
                              radius=df1d.icol(2).irow(i)/normalized,
                              color='r')
            ax.add_patch(circle)

        #plt.grid()
        plt.title('Matrix Plot')
        plt.show()

        #Export
        fig.savefig('D:\\Database\\export_image.png',dpi=600)

#///////////////////Main//////////////////////////////////
#///////////////////tk////////////////////////////////
    
#Window
root=tk.Tk()
root.geometry('400x200+120+80')
root.title('MatrixPlot')

#///////////////////widgets/////////////////////////////
#Label
label=tk.Label(root, text='Please put the raw data file here:',
               font=20)
label.place(x=50,y=20)

label=tk.Label(root, text='D:\\Database\\import_file.csv',
               font=20)
label.place(x=80,y=50)

#Button
button=tk.Button(root, text='Import & Plot',
                 command=matrixplot,
                 width=20, height=2,
                 font=20)
button.place(x=100,y=100)

root.mainloop()


    
