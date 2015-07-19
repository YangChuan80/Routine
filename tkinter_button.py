import tkinter as tk

root=tk.Tk()

def inputaction():
        
    tx=inputtx.get()
    tx=tx**2
    #label2=Label(root,text=tx,font=20).place(x=20,y=140)

    tex.delete('1.0',tk.END)
    tex.insert('1.0',tx)
    
    


inputtx=tk.IntVar()

root.geometry("700x500+100+50")
root.title("Hello World")

tex=tk.Text(root,width=40, height=1,font=20)
tex.place(x=20,y=160)

label1=tk.Label(root,
             text='This is my first dialog-based Python programm:',
             font=20)
label1.place(x=20,y=30)

displaybox=tk.Entry(root,textvariable=inputtx,font=20)
displaybox.place(x=20,y=60)

button1=tk.Button(root,text='Hello',font=20,command=inputaction)
button1.place(x=20,y=100)







root.mainloop()

