# student management system
import tkinter as tk
from tkinter import messagebox
from mysql import connector
from datetime import datetime
main_window=tk.Tk()
main_window.minsize(1000,500)
main_window.maxsize(1000,500)
date=datetime.now()
# table
# sql_create_table="""create table sectiona(
#                     rollnumber int(12) PRIMARY KEY,
#                     firstname varchar(10) NOT NULL,
#                     lastname varchar(10) NOT NULL,
#                     course varchar(10) NOT NULL,
#                     branch varchar(10) NOT NULL,
#                     year int(10) NOT NULL,
#                     age int(2) NOT NULL,
#                     gender varchar(10) NOT NULL,
#                     dob date NOT NULL,
#                     contact text(10) NOT NULL,
#                     email varchar(30) NOT NULL
# )"""

# variables
rollnumber=tk.IntVar()
course=tk.StringVar()
year=tk.IntVar()
gender=tk.StringVar()
contact=tk.StringVar()
fname=tk.StringVar()
lname=tk.StringVar()
branch=tk.StringVar()
age=tk.IntVar()
dob=tk.StringVar()
email=tk.StringVar()
# frames
f1=tk.Frame(main_window,width=600,height=500,bg="orange")
f2=tk.Frame(main_window,width=400,height=500,bg="grey")
f2.grid(row=0,column=1)
f3=tk.Frame(main_window,width=600,height=500,bg="orange")
f4=tk.Frame(main_window,width=600,height=500,bg="orange")
f5=tk.Frame(main_window,width=600,height=500,bg="orange")
def create_label_entries(frame,text,texttype,xl,y,xe):
    fnl=tk.Label(frame,text=text,font="halvetica 15",bg="orange")
    fnl.place(x=xl,y=y)
    fne=tk.Entry(frame,textvariable=texttype,font="halvetica 12 ",fg="blue")
    fne.place(x=xe,y=y)

def clear_entries():
    fname.set("")
    lname.set("")
    course.set("")
    branch.set("")
    year.set("")
    age.set("")
    contact.set("")
    email.set("")
    gender.set("")
    dob.set("")
def create_button(frame,text,y,function):
    button=tk.Button(f2,text=text,width=20,command=function)
    button.place(x=200,y=y)
def save_records():
    con=connector.connect(host="localhost",user="root",database="cs3rdyear")
    cur=con.cursor()
    data=(fname.get(),lname.get(),course.get(),branch.get(),year.get(),age.get(),gender.get(),dob.get(),contact.get(),email.get())
    sql_insert_query='''INSERT INTO sectiona(firstname,lastname,course,branch,year,age,gender,dob,contact,email)
            Values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s )
    '''
    cur.execute(sql_insert_query,data)
    con.commit()
    con.close()
    cur.close()
    clear_entries()
def get_data():
    found=0
    con=connector.connect(host="localhost",user="root",database="cs3rdyear")
    cur=con.cursor()    
    sql_select=''' SELECT rollnumber FROM sectiona'''
    cur.execute(sql_select)
    lst=cur.fetchall()
    for i in lst:
        for j in i:
            if(j==rollnumber.get()):
                found=1
    if(found==1):
        f3.grid_forget()
        f1.grid(row=0,column=0)
        sql_select2=f''' SELECT * FROM sectiona WHERE rollnumber={rollnumber.get()}'''
        cur.execute(sql_select2)
        tup=cur.fetchone()
        fname.set(tup[1])
        lname.set(tup[2])
        course.set(tup[3])
        branch.set(tup[4])
        year.set(tup[5])
        age.set(tup[6])
        gender.set(tup[7])
        dob.set(tup[8])
        contact.set(tup[9])
        email.set(tup[10])
        con.close()
        cur.close()
    else:
        messagebox.showerror("Error","No record found for this rollnumber")
def remove_data():
        found=0
        con=connector.connect(host="localhost",user="root",database="cs3rdyear")
        cur=con.cursor()
        sql_select=''' SELECT rollnumber FROM sectiona'''
        cur.execute(sql_select)
        lst=cur.fetchall()
        for i in lst:
            for j in i:
                if(j==rollnumber.get()):
                    found=1    
        if(found==1):
            sql_delete=f'''DELETE FROM sectiona WHERE rollnumber={rollnumber.get()}'''
            cur.execute(sql_delete)
            con.commit()
            con.close()
            cur.close()
        else:
            messagebox.showerror("Error","this rollnumber is not present so you cannot delete")
def update_data():
    found=0
    con=connector.connect(host="localhost",user="root",database="cs3rdyear")
    cur=con.cursor()
    sql_select=''' SELECT rollnumber FROM sectiona'''
    cur.execute(sql_select)
    lst=cur.fetchall()
    for i in lst:
        for j in i:
            if(j==rollnumber.get()):
                found=1    
    if(found==1):
        pass
    else:
        messagebox.showerror("Error","this rollnumber is not present so you cannot update")

def add_records():
    f3.grid_forget()
    f5.grid_forget()
    f4.grid_forget()
    f1.grid(row=0,column=0)
    clear_entries()
def view_records():
    rollnumber.set("")
    f1.grid_forget()
    f4.grid_forget()
    f5.grid_forget()
    f3.grid(row=0,column=0)
    l=tk.Label(f3,text="Enter your Roll number",font="halvetica 15 bold",bg="orange")
    l.place(x=230,y=200)
    e=tk.Entry(f3,textvariable=rollnumber,font="halvetica 12 ",fg="blue")
    e.place(x=250,y=230)
    tk.Button(f3,text="Submit",command=get_data).place(x=320,y=260)
def update_records():
    rollnumber.set("")
    f1.grid_forget()
    f3.grid_forget()
    f4.grid(row=0,column=0)
    l=tk.Label(f4,text="Enter your Roll number",font="halvetica 15 bold",bg="orange")
    l.place(x=230,y=200)
    e=tk.Entry(f4,textvariable=rollnumber,font="halvetica 12 ",fg="blue")
    e.place(x=250,y=230)
    tk.Button(f4,text="Submit",command=update_data).place(x=320,y=260)

def delete_records():
    rollnumber.set("")
    f1.grid_forget()
    f3.grid_forget()
    f4.grid_forget()
    f5.grid(row=0,column=0)
    l=tk.Label(f5,text="Enter your Roll number",font="halvetica 15 bold",bg="orange")
    l.place(x=230,y=200)
    e=tk.Entry(f5,textvariable=rollnumber,font="halvetica 12 ",fg="blue")
    e.place(x=250,y=230)
    tk.Button(f5,text="Submit",command=remove_data).place(x=320,y=260)
def exit_main_window():
    main_window.destroy()
create_label_entries(frame=f1,text="FirstName",texttype=fname,xl=0,y=0,xe=100)
create_label_entries(frame=f1,text="Course",texttype=course,xl=0,y=30,xe=100)
create_label_entries(frame=f1,text="Year",texttype=year,xl=0,y=60,xe=100)
create_label_entries(frame=f1,text="Gender",texttype=gender,xl=0,y=90,xe=100)
create_label_entries(frame=f1,text="Contact",texttype=contact,xl=0,y=120,xe=100)
create_label_entries(frame=f1,text="LastName",texttype=lname,xl=300,y=0,xe=400)
create_label_entries(frame=f1,text="Branch",texttype=branch,xl=300,y=30,xe=400)
create_label_entries(frame=f1,text="Age",texttype=age,xl=300,y=60,xe=400)
create_label_entries(frame=f1,text="DOB",texttype=dob,xl=300,y=90,xe=400)
create_label_entries(frame=f1,text="Email",texttype=email,xl=300,y=120,xe=400)
tk.Button(f1,text="Submit",command=save_records).place(x=250,y=180)
create_button(frame=f2,text="Add New",y=50,function=add_records)
create_button(frame=f2,text="View Details",y=80,function=view_records)
create_button(frame=f2,text="Update",y=110,function=update_records)
create_button(frame=f2,text="Delete",y=140,function=delete_records)
create_button(frame=f2,text="Exit",y=170,function=exit_main_window)
main_window.mainloop()