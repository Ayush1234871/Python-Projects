from tkinter import *
from PIL import Image,ImageTk
import tkinter.messagebox
import sqlite3
window = Tk()
window.geometry("500x500")
window.title("Registration Form")

#phot part if want to insert
#image=Image.open("D:\images.png")
#photo=ImageTk.PhotoImage(image)
#lab=Label(image=photo)
#lab.place(x=50,y=60)


fn=StringVar()
ln=StringVar()
var=StringVar()
var_c1="Java"
var_c2="Python"
radio_var=StringVar()

def getdetails():
    first=fn.get()
    sec=ln.get()
    country1=var.get()
    l1="Java"
    l1="Python"
    m1=radio_var.get()
    print(f"Full Name:{first} {sec}")
    print(f"Country:{country1}")
    print(f"Language:{l1}")
    print(f"Gender:{m1}")
    tkinter.messagebox.showinfo("Welcome","Thanku!!for submitting the Details")

def exit1():
    exit()

def database():
    name1=fn.get()
    last1=ln.get()
    country=var.get()
    prog=var_c2
    gender=radio_var.get()
    con=sqlite3.connect("Registration Form.db")
    with con:
        cursor=con.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS Student (Name TEXT,Last TEXT,country TEXT,Programming TEXT,Gender TEXT)')
    cursor.execute('INSERT INTO Student(Name,Last,country,Programming,Gender) VALUES(?,?,?,?,?)',(name1,last1,country,prog,gender))
    con.commit()




menu=Menu(window)
window.config(menu=menu)

subm1=Menu(menu)
menu.add_cascade(label="Help",font=('ariel',18),menu=subm1), 
subm1.add_command(label="Try checking for the internet")  

subm2=Menu(menu)
menu.add_cascade(label="Contact Us",font=('ariel',18),menu=subm2), 
subm2.add_command(label="Phone Number:+919368017831")   
subm2.add_command(label="Email Add:agarwalayu2711@gmail.com")


Label1 = Label(window, text="Registration Form", relief="solid", width=20, font=("arial", 19, "bold"))
Label1.place(x=90, y=53)

label2 = Label(window, text="First Name", width=20, font=("arial", 10, "bold"))
label2.place(x=80, y=130)

entry1=Entry(window,textvariable=fn)
entry1.place(x=220, y=130)

label3 = Label(window, text="Last Name", width=20, font=("arial", 10, "bold"))
label3.place(x=80, y=179)

entry2=Entry(window,textvariable=ln)
entry2.place(x=220, y=180)

label4 = Label(window, text="Country", width=20, font=("arial", 10, "bold"))
label4.place(x=80, y=230)

label5 = Label(window, text="Language", width=20, font=("arial", 10, "bold"))
label5.place(x=80, y=280)
c1=Checkbutton(window,text="Java",variable=var_c1).place(x=220,y=280)
c1=Checkbutton(window,text="Python",variable=var_c2).place(x=280,y=280)

label6 = Label(window, text="Gender", width=20, font=("arial", 10, "bold"))
label6.place(x=80, y=330)
r1=Radiobutton(window,text="Male",variable=radio_var,value="Male").place(x=220,y=330)
r2=Radiobutton(window,text="Female",variable=radio_var,value="Female").place(x=280,y=330)

list1=['Nepal','India','Canada','USA']
droplist=OptionMenu(window,var,*list1)
var.set("select country")
droplist.config(width=15)
droplist.place(x=220,y=220)

button1=Button(window,text="Submit",width=12,bg="brown",fg="white",command=lambda: [getdetails(), database()])
button1.place(x=150,y=380)
window.bind("<Return>",database)

button2=Button(window,text="Exit",width=12,bg="brown",fg="white",command=exit1)
button2.place(x=280,y=380)

window.mainloop()
