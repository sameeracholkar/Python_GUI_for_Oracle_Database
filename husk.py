"""
Author:- Sameer Acholkar

User can use this utility to connect to any database on Pelican network
And take actions on that Database.
A user can
1. Insert into database
2. Search an entry into database
3. update Database
4. Delete Database
"""

from tkinter import *
import oracleend

window=Tk()

window.wm_title("Husk")

def get_selected_row(event):
    global selected_tuple
    if list1.curselection():
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        e6.delete(0,END)
        e6.insert(END, selected_tuple[0])
        e7.delete(0,END)
        e7.insert(END, selected_tuple[1])
        e8.delete(0,END)
        e8.insert(END, selected_tuple[2])
        e9.delete(0,END)
        e9.insert(END, selected_tuple[3])
        e10.delete(0,END)
        e10.insert(END, selected_tuple[4])
        e11.delete(0,END)
        e11.insert(END, selected_tuple[5])
        e12.delete(0,END)
        e12.insert(END, selected_tuple[6])
        
    
def view_command():
    oracleend.view(schema_name_text.get(), schema_password_text.get(), server_id_text.get(), container_db_text.get(), table_name_text.get())
    list1.delete(0,END)
    for row in oracleend.view(schema_name_text.get(), schema_password_text.get(), server_id_text.get(), container_db_text.get(), table_name_text.get()):
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in oracleend.search(schema_name_text.get(), schema_password_text.get(), server_id_text.get(), container_db_text.get(), table_name_text.get(), LANGCODE_text.get(), MODULECODE_text.get(), ITEMNO_text.get(), LANGDESC1_text.get(), LANGDESC2_text.get(), LANGDESC3_text.get(), LANGDESC4_text.get()):
        list1.insert(END,row)

def add_command():
    oracleend.insert(schema_name_text.get(), schema_password_text.get(), server_id_text.get(), container_db_text.get(), table_name_text.get(), LANGCODE_text.get(), MODULECODE_text.get(), ITEMNO_text.get(), LANGDESC1_text.get(), LANGDESC2_text.get(), LANGDESC3_text.get(), LANGDESC4_text.get())
    list1.delete(0,END)
    list1.insert(END,(LANGCODE_text.get(), MODULECODE_text.get(), ITEMNO_text.get(), LANGDESC1_text.get(), LANGDESC2_text.get(), LANGDESC3_text.get(), LANGDESC4_text.get()))
    
def delete_command():
    oracleend.delete(schema_name_text.get(), schema_password_text.get(), server_id_text.get(), container_db_text.get(), table_name_text.get(), LANGCODE_text.get(), MODULECODE_text.get(), ITEMNO_text.get(), LANGDESC1_text.get(), LANGDESC2_text.get(), LANGDESC3_text.get(), LANGDESC4_text.get())

def update_command():
    oracleend.update(schema_name_text.get(), schema_password_text.get(), server_id_text.get(), container_db_text.get(), table_name_text.get(), MODULECODE_text.get(), ITEMNO_text.get(), LANGDESC1_text.get(), LANGDESC2_text.get(), LANGDESC3_text.get(), LANGDESC4_text.get())

l1=Label(window, text='Server_ID :', bg='lightblue')
l1.grid(row=0 , column=0 )

l2=Label(window, text='Container_db :', bg='lightblue')
l2.grid(row=0 , column=2 )

l3=Label(window, text='Schema_name :', bg='lightblue')
l3.grid(row=1 , column=0 )

l4=Label(window, text='Schema_Password :', bg='lightblue')
l4.grid(row=1 , column=2 )

l5=Label(window, text='Table_name :', bg='lightblue')
l5.grid(row=2 , column=0 )

l6=Label(window, text='LANGCODE :', bg='lightblue')
l6.grid(row=2 , column=2 )

l7=Label(window, text='MODULECODE :', bg='lightblue')
l7.grid(row=3 , column=0 )

l8=Label(window, text='ITEMNO :', bg='lightblue')
l8.grid(row=3 , column=2 )

l9=Label(window, text='LANGDESC1 :', bg='lightblue')
l9.grid(row=4 , column=0 )

l10=Label(window, text='LANGDESC2 :', bg='lightblue')
l10.grid(row=4 , column=2 )

l11=Label(window, text='LANGDESC3 :', bg='lightblue')
l11.grid(row=5 , column=0 )

l12=Label(window, text='LANGDESC4 :', bg='lightblue')
l12.grid(row=5 , column=2 )

server_id_text=StringVar()
e1=Entry(window, textvariable=server_id_text)
e1.grid(row=0 , column=1)

container_db_text=StringVar()
e2=Entry(window, textvariable=container_db_text)
e2.grid(row=0 , column=3)

schema_name_text=StringVar()
e3=Entry(window, textvariable=schema_name_text)
e3.grid(row=1 , column=1)

schema_password_text=StringVar()
e4=Entry(window, textvariable=schema_password_text)
e4.grid(row=1 , column=3)

table_name_text=StringVar()
e5=Entry(window, textvariable=table_name_text)
e5.grid(row=2 , column=1)

LANGCODE_text=StringVar()
e6=Entry(window, textvariable=LANGCODE_text)
e6.grid(row=2 , column=3)

MODULECODE_text=StringVar()
e7=Entry(window, textvariable=MODULECODE_text)
e7.grid(row=3 , column=1)

ITEMNO_text=StringVar()
e8=Entry(window, textvariable=ITEMNO_text)
e8.grid(row=3 , column=3)

LANGDESC1_text=StringVar()
e9=Entry(window, textvariable=LANGDESC1_text)
e9.grid(row=4 , column=1)

LANGDESC2_text=StringVar()
e10=Entry(window, textvariable=LANGDESC2_text)
e10.grid(row=4 , column=3)

LANGDESC3_text=StringVar()
e11=Entry(window, textvariable=LANGDESC3_text)
e11.grid(row=5 , column=1)

LANGDESC4_text=StringVar()
e12=Entry(window, textvariable=LANGDESC4_text)
e12.grid(row=5 , column=3)

list1=Listbox(window, height=8, width=50)
list1.grid(row=7, column=0, rowspan=6, columnspan=3)

sb1=Scrollbar(window)
sb1.grid(row=7, column=2, rowspan=6, columnspan=5, sticky='NS')

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(window, text="View All", fg='red', bg='pink', activebackground='yellow', width=12, command=view_command)
b1.grid(row=7 , column=3)

b2=Button(window, text="Search", fg='red', bg='pink', activebackground='yellow', width=12, command=search_command)
b2.grid(row=8 , column=3)

b3=Button(window, text="Insert", fg='red', bg='pink', activebackground='yellow', width=12, command=add_command)
b3.grid(row=9 , column=3)

b4=Button(window, text="Update", fg='red', bg='pink', activebackground='yellow', width=12, command=update_command)
b4.grid(row=10 , column=3)

b5=Button(window, text="Delete", fg='red', bg='pink', activebackground='yellow', width=12, command=delete_command)
b5.grid(row=11 , column=3)

b6=Button(window, text="Close", fg='red', bg='pink', activebackground='yellow', width=12, command=window.destroy)
b6.grid(row=12 , column=3)

window.configure(background='lightblue')
window.mainloop()
