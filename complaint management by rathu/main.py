from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import Project

db=Project("complaint.db")
root=Tk()
root.title("Complaint Management")
root.geometry("1366x768+0+0")
root.config(bg="lightblue")
root.state("zoomed")

name = StringVar
gender = StringVar


#entries frame

entries_frame = Frame(root,bg="lightblue")
entries_frame.pack(side=TOP,fill=X)
title=Label(entries_frame,text="COMPLAINT MANAGEMENT",font=("Ariel",16,"bold"),bg="orange",fg="black")
title.grid(row=0,columnspan=2,padx=10,pady=10,sticky="w")

lblname=Label(entries_frame,text="Name",font=("Ariel",16),bg="lightblue",fg="black")
lblname.grid(row=1,column=0,padx=10,pady=10,sticky="w")
txtname=Entry(entries_frame,textvariable=name,font=("Ariel",16),width=20)
txtname.grid(row=1,column=1,sticky="w")

lblgender=Label(entries_frame,text="Gender",font=("Ariel",16),bg="lightblue",fg="black")
lblgender.grid(row=2,column=0,padx=10,pady=10,sticky="w")
combogender=ttk.Combobox(entries_frame,textvariable=gender,font=("Ariel",16),width=20,state="readonly")
combogender["values"]=("Male","Female","Others")
combogender.grid(row=2,column=1,sticky="w")

lblcomment=Label(entries_frame,text="Comment",font=("Ariel",16),bg="lightblue",fg="black")
lblcomment.grid(row=3,column=0,padx=10,pady=10,sticky="w")
txtcomment=Text(entries_frame,font=("Ariel",16),width=85,height=5)
txtcomment.grid(row=3,column=1,padx=10,pady=10,sticky="w")


def displayall():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("",END,values=row)

def view():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("", END, values=row)


def submit():
    if txtname.get()=="" or combogender.get()=="" or txtcomment.get("1.0",END)=="":
       messagebox.showerror("Error in Input","Please fill all the details")
       return
    db.insert(txtname.get(),combogender.get(),txtcomment.get("1.0",END))
    messagebox.showinfo("Success","Data Inserted")


btn_frame=Frame(entries_frame,bg="lightblue")
btn_frame.grid(row=4,column=0,columnspan=2,padx=10,pady=10,sticky="w")

btnview=Button(btn_frame,command=view,text="View",font=("Ariel",16,"bold"),width=15,bg="yellow",fg="red",bd=0)
btnview.grid(row=0,column=0,padx=10,pady=10,sticky="w")

btnsubmit=Button(btn_frame,command=submit,text="Submit Now",font=("Ariel",16,"bold"),width=15,bg="yellow",fg="red",bd=0)
btnsubmit.grid(row=0,column=1,padx=40,pady=10,sticky="w")


#table frame

tree_frame=Frame(root,bg="white")
tree_frame.place(x=0,y=380,width=1400,height=500)
#style
style=ttk.Style()
style.configure("mystyle.Treeview",font=("Calibri",16),rowheight=50)
style.configure("mystyle.Treeview.Heading",font=("Ariel",15))

tv=ttk.Treeview(tree_frame,columns=(1,2,3,4),style="mystyle.Treeview")
tv.heading("1",text="ID")
tv.column("1",width=10)
tv.heading("2",text="Name")
tv.heading("3",text="Gender")
tv.heading("4",text="Comment")
tv["show"]="headings"
tv.pack(fill=X)


view()
displayall()
root.mainloop()