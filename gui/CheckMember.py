from tkinter import *
import member


check_member = Tk()

def search_handler():
    list_page = Tk()

    Label(list_page, text="ID", width=5, fg="white", bg="black").grid(row=1,column=1, sticky=W)
    Label(list_page, text="NAME", width=20, fg="white", bg="black").grid(row=1,column=2, sticky=W)
    Label(list_page, text="CONTACT", width=20, fg="white", bg="black").grid(row=1,column=3)
    Label(list_page, text="LOAN", width=10, fg="white", bg="black").grid(row=1,column=4, sticky=W)
    Label(list_page, text="B/ID", width=5, fg="white", bg="black").grid(row=1,column=5, sticky=W)

    lists = member.members_list(id_entry.get(), name_entry.get())
    i=2
    for list in lists:
        Label(list_page, text=list[0], width=5).grid(row=i,column=1, sticky=W)
        Label(list_page, text=list[1], width=20).grid(row=i,column=2, sticky=W)
        Label(list_page, text=list[2], width=20).grid(row=i,column=3)
        Label(list_page, text=list[3], width=10).grid(row=i,column=4, sticky=W)
        Label(list_page, text=list[4], width=5).grid(row=i,column=5, sticky=W)
        i+=1
    list_page.mainloop()


Label(check_member, text="Member's ID: ").grid(row=1, column=1)
id_entry = Entry(check_member, width=50)
id_entry.grid(row=1, column=2)

Label(check_member, text="Member's Name: ").grid(row=2, column=1)
name_entry = Entry(check_member, width=50)
name_entry.grid(row=2, column=2)

Button(check_member, text="Search", width=15, command=search_handler).grid(row=3, column=1)

check_member.mainloop()

