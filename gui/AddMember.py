from tkinter import *
import member

add_member = Tk()
add_member.geometry("500x500")


def add_handler():
    if len(name_entry.get())==0 or len(contact_entry.get())==0:
        validation_label.configure(text="Do not leave field empty!", fg='red')
    else:
        member.add_member(member.get_id(), name_entry.get(), contact_entry.get())
        validation_label.configure(text="Successfully Added", fg='green')


Label(add_member, text="Register New Member:").grid(column=5,row=1)

name_label = Label(add_member, text="Name: ").grid(row=5,column=5)
name_entry = Entry(add_member, width=50)
name_entry.grid(row=5, column=6)

contact_label = Label(add_member, text="Contact: ").grid(row=6, column=5)
contact_entry = Entry(add_member, width=50)
contact_entry.grid(row=6,column=6)

validation_label = Label(add_member, text="")
validation_label.grid(row=7, column=6)

add_button = Button(add_member, text="Add", command=add_handler).grid(row=7,column=5)

add_member.mainloop()