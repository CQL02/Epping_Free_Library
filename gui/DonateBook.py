from tkinter import *
from tkinter.ttk import Combobox
import books

donate_book = Tk()


def add_handler():
    if len(name_entry.get())==0 or len(genre1_entry.get())==0 or len(genre2_entry.get())==0:
        validation_label.configure(text="Do not leave field empty!", fg='red')
    else:
        books.add_book(books.get_id(), name_entry.get(), genre1_entry.get(), genre2_entry.get())
        validation_label.configure(text="Successfully Added", fg='green')



genre = [
    'Romance', 
    'Mystery', 
    'Fantasy and science fiction', 
    'Thrillers and horror', 
    'Young adult', 
    'Children\'s fiction', 
    'Inspirational, self-help, and religious', 
    'Biography, autobiography, and memoir'
    ]

Label(donate_book, text="Name: ").grid(row=2,column=1)
name_entry = Entry(donate_book, width=50)
name_entry.grid(row=2, column=2)

Label(donate_book, text="Genre #1: ").grid(row=3,column=1)
genre1_entry = Combobox(donate_book, values=genre, width=47)
genre1_entry.grid(row=3, column=2)

Label(donate_book, text="Genre #2: ").grid(row=4,column=1)
genre2_entry = Combobox(donate_book, values=genre, width=47)
genre2_entry.grid(row=4, column=2)

validation_label = Label(donate_book, text="")
validation_label.grid(row=5, column=2)

Button(donate_book, text="Add", command=add_handler).grid(row=6,column=1)

donate_book.mainloop()

