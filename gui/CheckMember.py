from tkinter import *
import member


check_member = Tk()

# bug at id_entry
def search_handler():
    list_page = Tk()
    lists = member.members_list(id_entry.get(), name_entry.get())
    for list in lists:
        Label(list_page, text=list).pack()
    list_page.mainloop()


Label(check_member, text="Member's ID: ").grid(row=1, column=1)
id_entry = Entry(check_member, width=50)
id_entry.grid(row=1, column=2)

Label(check_member, text="Member's Name: ").grid(row=2, column=1)
name_entry = Entry(check_member, width=50)
name_entry.grid(row=2, column=2)

Button(check_member, text="Search", width=15, command=search_handler).grid(row=3, column=1)

check_member.mainloop()