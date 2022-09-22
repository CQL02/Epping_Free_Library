from tkinter import *
import member


delete_member = Tk()

def delete_button_handler():
    if member.check_member(id_entry.get(), name_entry.get())[0] == 1:
        member.delete_member(id_entry.get(), name_entry.get())
        alert_text.configure(text="Successfuly Deleted!", fg="green")
    else:
        alert_text.configure(text="Member ID/Name is wrong/does not exist!",fg="red")



Label(delete_member, text="Delete Member: ").grid(row=1,column=1)

Label(delete_member, text="Member's ID:").grid(row=2,column=1)
id_entry = Entry(delete_member, width=20)
id_entry.grid(row=2, column=2)

Label(delete_member, text="Member's Name: ").grid(row=3,column=1)
name_entry = Entry(delete_member, width=20)
name_entry.grid(row=3, column=2)

Button(delete_member, text="Delete", command=delete_button_handler).grid(row=4,column=1)
alert_text = Label(delete_member, text="")
alert_text.grid(row=4,column=2)

delete_member.mainloop()