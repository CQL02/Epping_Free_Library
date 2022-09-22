from tkinter import *
from unicodedata import name
import staff

manage_staff = Tk()


def add_handler():
    if len(name_entry.get())==0 or len(password_entry.get())==0 or len(contact_entry.get())==0:
        validation_label.configure(text="Do not leave Name, password OR contact empty!", fg='red')
    else:
        staff.add_staff(staff.get_id(), name_entry.get(), password_entry.get(), contact_entry.get())
        validation_label.configure(text="Successfully Added", fg='green')

def delete_handler():
    if staff.check_staff(id_entry.get(), name_entry.get(),password_entry.get())[0] == 1:
        staff.delete_staff(id_entry.get(), name_entry.get(), password_entry.get())
        validation_label.configure(text="Successfuly Deleted!", fg="green")
    else:
        validation_label.configure(text="Member ID/Name/Password is wrong/does not exist!",fg="red")

def check_handler():
    list_page = Tk()
    lists = staff.staffs_list()
    for list in lists:
        Label(list_page, text=list).pack()
    list_page.mainloop()


Label(manage_staff, text="ID: ").grid(row=2,column=1)
id_entry = Entry(manage_staff, width=50)
id_entry.grid(row=2,column=2)

Label(manage_staff, text="Name: ").grid(row=3,column=1)
name_entry = Entry(manage_staff, width=50)
name_entry.grid(row=3,column=2)

Label(manage_staff, text="Password: ").grid(row=4,column=1)
password_entry = Entry(manage_staff, width=50, show="*")
password_entry.grid(row=4,column=2)

Label(manage_staff, text="Contact: ").grid(row=5,column=1)
contact_entry = Entry(manage_staff, width=50, show="*")
contact_entry.grid(row=5,column=2)

validation_label = Label(manage_staff, text="")
validation_label.grid(row=6,column=2)

Button(manage_staff, text="Add Staff", width=20,command=add_handler).grid(row=7, column=1)
Button(manage_staff, text="Delete Staff", width=20, command=delete_handler).grid(row=7, column=2)
Button(manage_staff, text="List Of Staff", width=20, command=check_handler).grid(row=8, column=1)

manage_staff.mainloop()




