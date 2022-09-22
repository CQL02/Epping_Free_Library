from tkinter import *
import staff
login_page = Tk()


def login_handler():
    if staff.check_staff_login(name_entry.get(), password_entry.get())[0] >= 1:
        login_page.destroy()
        import HomePage
    else:
        Label(login_page, text='Wrong ID/Password. Please Type Again!', fg='red').grid(row=7, column=6)
        
name_label = Label(login_page, text="Name: ").grid(row=5,column=5)
name_entry = Entry(login_page, width=50)
name_entry.grid(row=5, column=6)

password_label = Label(login_page, text="Password: ").grid(row=6, column=5)
password_entry = Entry(login_page, width=50, show="*")
password_entry.grid(row=6,column=6)

login_button = Button(login_page, text="login", command=login_handler).grid(row=7,column=5)
login_page.mainloop()