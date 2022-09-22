from tkinter import *


home_page = Tk()

def add_member_handler():
    import AddMember

def borrow_book_handler():
    import BorrowBook

def return_book_handler():
    import ReturnBook

def search_book_handler():
    import SearchBook

def donate_book_handler():
    import DonateBook

def check_member_handler():
    import CheckMember

def manage_staff_handler():
    import ManageStaff

def logout_handler():
    home_page.destroy()
    import LoginPage

header_label = Label(home_page, text="Welcome!").grid(row=5,column=5)

add_member_button = Button(home_page, text= 'Add Member', width=20, command=add_member_handler).grid(row=10,column=5)
borrow_book_button = Button(home_page, text= 'Borrow Book', width=20, command=borrow_book_handler).grid(row=11,column=5)
return_book_button = Button(home_page, text= 'Return Book', width=20, command=return_book_handler).grid(row=12,column=5)
search_book_button = Button(home_page, text= 'Search Book', width=20, command=search_book_handler).grid(row=13,column=5)
donate_book_button = Button(home_page, text= 'Donate Book', width=20, command=donate_book_handler).grid(row=14,column=5)
check_member_button = Button(home_page, text= 'Check Member', width=20, command=check_member_handler).grid(row=15,column=5)
manage_staff_button = Button(home_page, text= 'Manage Staff', width=20, command=manage_staff_handler).grid(row=16,column=5)
logout_button = Button(home_page, text="Log Out", width=20, command=logout_handler).grid(row=16, column=5)



home_page.mainloop()