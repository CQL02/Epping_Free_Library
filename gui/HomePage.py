from tkinter import *

home_page = Tk()

def add_member_handler():
    home_page.destroy()
    import AddMember

def borrow_book_handler():
    home_page.destroy()
    import BorrowBook

def return_book_handler():
    home_page.destroy()
    import ReturnBook

def availability_handler():
    home_page.destroy()
    import BookAvailability

def donate_book_handler():
    home_page.destroy()
    import DonateBook

def check_member_handler():
    home_page.destroy()
    import CheckMember

def manage_staff_handler():
    home_page.destroy()
    import ManageStaff


header_label = Label(home_page, text="Welcome!").grid(row=5,column=5)

add_member_button = Button(home_page, text= 'Add Member', width=20, command=add_member_handler).grid(row=10,column=5)
borrow_book_button = Button(home_page, text= 'Borrow Book', width=20).grid(row=11,column=5)
return_book_button = Button(home_page, text= 'Return Book', width=20).grid(row=12,column=5)
availability_button = Button(home_page, text= 'Book Availability', width=20).grid(row=13,column=5)
donate_book_button = Button(home_page, text= 'Donate Book', width=20).grid(row=14,column=5)
check_member_button = Button(home_page, text= 'Check Member', width=20, command=check_member_handler).grid(row=15,column=5)
manage_staff_button = Button(home_page, text= 'Manage Staff', width=20, command=manage_staff_handler).grid(row=16,column=5)



home_page.mainloop()