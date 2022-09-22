from tkinter import *
import books
import member

return_book = Tk()



def return_handler():
    if len(id_entry.get())==0:
        validation_text.configure(text="Please enter book's ID!", fg="red")
    elif books.book_exist(id_entry.get()) == 0:
        validation_text.configure(text="Book does not exist!", fg ="red")
    elif books.book_availabilty(id_entry.get()) == "TRUE":
        validation_text.configure(text="Book did not borrow out", fg="red")
    else:
        payment_window = Tk()

        def pay_handler():
            member.update_member(books.get_borrowed_id(id_entry.get()), 0, None)
            books.update_book(None, "TRUE", id_entry.get())
            payment_window.destroy()

        Label(payment_window, text="TOTAL: $" +str(member.get_loan(books.get_borrowed_id(id_entry.get()))) +"0").grid(row=1, column=1)
        Button(payment_window, text="Pay", command=pay_handler).grid(row=2, column=1)
        Button(payment_window, text="Cancel", command=payment_window.destroy).grid(row=2, column=2)
        payment_window.mainloop()



Label(return_book, text="RETURN BOOK: ").grid(row=1,column=1)

Label(return_book, text="Book's ID: ").grid(row=2, column=1, sticky=W)
id_entry = Entry(return_book, width=50)
id_entry.grid(row=2, column=2, sticky=E)

validation_text = Label(return_book, text="")
validation_text.grid(row=3, column=2)

Button(return_book, text="Return", command=return_handler).grid(row=4, column=1)

return_book.mainloop()