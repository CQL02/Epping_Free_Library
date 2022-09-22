from tkinter import *
import books
import member

borrow_book = Tk()

def confirm_handler():
    if len(book_id_entry.get())==0:
        validation_label1.configure(text="Do not leave this field EMPTY!", fg="red")
    elif books.book_exist(book_id_entry.get()) ==0:
        validation_label1.configure(text="Book does not exist!", fg="red")
    elif books.book_availabilty(book_id_entry.get()) == "FALSE":
        validation_label1.configure(text="Book not available!", fg="red")
    else:
        validation_label1.configure(text="")
        if len(member_id_entry.get())==0:
            validation_label2.configure(text="Do not leave this field EMPTY!", fg="red")
        elif member.member_exist(member_id_entry.get()) ==0:
            validation_label2.configure(text="Please register as member before borrow", fg="red")
        elif member.get_borrowed_book_id(member_id_entry.get()) != None:
            validation_label2.configure(text="Please return book before borrow", fg="red")
        else:
            loan = int(days_entry.get()) * 0.5
            books.update_book(member_id_entry.get(),"FALSE",book_id_entry.get())
            member.update_member(member_id_entry.get(),loan,book_id_entry.get())
            loan_window = Tk()
            Label(loan_window, text="Please pay $" +str(loan) +"0 when return book").pack()
            loan_window.mainloop()



Label(borrow_book, text="Borrow Book:").grid(row=1, column=1, sticky=E)

Label(borrow_book, text="Book's ID: ").grid(row=2, column=1, sticky=E)
book_id_entry = Entry(borrow_book, width=50)
book_id_entry.grid(row=2, column=2)

validation_label1 = Label(borrow_book, text="")
validation_label1.grid(row=3, column=2)

Label(borrow_book, text="Member's ID: ").grid(row=4, column=1, sticky=E)
member_id_entry = Entry(borrow_book, width=50)
member_id_entry.grid(row=4,column=2)

validation_label2 = Label(borrow_book, text="")
validation_label2.grid(row=5, column=2)

Label(borrow_book, text="Days to borrow: ").grid(row=6, column=1)
days_entry = Spinbox(borrow_book, from_=1, to=14)
days_entry.grid(row=6, column=2, sticky=W)

Button(borrow_book, text="Confirm",command=confirm_handler).grid(row=7, column=1)

borrow_book.mainloop()