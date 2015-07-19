import tkinter as tk
from tkinter import messagebox

def convert_c2f():

    gotten=tex_cel.get('1.0', tk.END)
    c=float(gotten)
    
    f=c*1.8+32
    tex_fah.delete('1.0', tk.END)
    tex_fah.insert('1.0',f)

def convert_f2c():

    gotten=tex2_fah.get('1.0', tk.END)
    f2=float(gotten)
    
    c2=(f2-32)/1.8
    tex2_cel.delete('1.0', tk.END)
    tex2_cel.insert('1.0',c2)

def about_conversion():
    messagebox.showinfo('About this program','Author: Chuan Yang')

    
def exit_conversion():
    root.destroy()
    
#Instance root is generated from the class Tk
root=tk.Tk()

root.geometry('705x320+180+80')
root.title('Conversion between Celcius and Fahrenheit')

#Image Implantation, which is very exciting!!!!!!!!
photo=tk.PhotoImage(file='D:\\PySource\\Routine\\gauge.png')
label_photo=tk.Label(root, image=photo)
label_photo.place(x=300,y=5)

#Celcium to Fahrenheit
label_cel=tk.Label(root,text='Celcius:', font=20)
label_cel.place(x=50,y=40)


tex_cel=tk.Text(root,width=10,height=1, font=20)
tex_cel.place(x=160,y=45)

tex_cel.delete('1.0', tk.END)
tex_cel.insert('1.0', 0)

#Button
button_c2f=tk.Button(root, width=23, height=2,
                     text='Convert',
                     font=20,
                     
                     command=convert_c2f)
button_c2f.place(x=50, y=85)


label_fah=tk.Label(root,text='Fahrenheit:', font=20)
label_fah.place(x=50,y=160)

tex_fah=tk.Text(root,width=10,height=1, font=20)
tex_fah.place(x=160,y=165)

#////////////////////////////////////////////

#Fahrenheit to Celcius
label2_fah=tk.Label(root,text='Fahrenheit:', font=20)
label2_fah.place(x=450,y=40)


tex2_fah=tk.Text(root,width=10,height=1, font=20)
tex2_fah.place(x=560,y=45)

tex2_fah.delete('1.0', tk.END)
tex2_fah.insert('1.0', 0)

#Button
button2_f2c=tk.Button(root, width=23, height=2,
                     text='Convert',
                     font=20,                     
                     command=convert_f2c)
button2_f2c.place(x=450, y=85)


label2_cel=tk.Label(root,text='Celcius:', font=20)
label2_cel.place(x=450,y=160)

tex2_cel=tk.Text(root,width=10,height=1, font=20)
tex2_cel.place(x=560,y=165)

#////////////////////////////////////////////////

#About
button_about=tk.Button(root, text='About',
                       width=20,
                       height=2,
                       font=20,
                       command=about_conversion)
button_about.place(x=80, y=240)

#Quit
button_quit=tk.Button(root, text='Exit',
                      width=20,
                      height=2,
                      font=20,
                      command=exit_conversion)
button_quit.place(x=450, y=240)



root.mainloop()
