from tkinter import *
from tkinter.ttk import Combobox
import books

search_book = Tk()

def search_button():
    if len(genre_entry.get())==0:
        validation_text.configure(text="Please Enter Genre!", fg="red")
    else:
        book_list = Tk()

        Label(book_list, text="ID", width=5, fg="white", bg="black").grid(row=1,column=1, sticky=W)
        Label(book_list, text="NAME", width=20, fg="white", bg="black").grid(row=1,column=2, sticky=W)
        Label(book_list, text="AVAILABILITY", width=10, fg="white", bg="black").grid(row=1,column=3)
        Label(book_list, text="GENRE #1", width=30, fg="white", bg="black").grid(row=1,column=4, sticky=W)
        Label(book_list, text="GENRE #2", width=30, fg="white", bg="black").grid(row=1,column=5, sticky=W)

        lists = books.search_genre(genre_entry.get())
        i=2
        for list in lists:
            Label(book_list, text=list[0], width=5).grid(row=i,column=1, sticky=W)
            Label(book_list, text=list[1], width=20).grid(row=i,column=2, sticky=W)
            Label(book_list, text=list[2], width=10).grid(row=i,column=3)
            Label(book_list, text=list[4], width=30).grid(row=i,column=4, sticky=W)
            Label(book_list, text=list[5], width=30).grid(row=i,column=5, sticky=W)
            i+=1
        book_list.mainloop()


genres = [
    'Romance', 
    'Mystery', 
    'Fantasy and science fiction', 
    'Thrillers and horror', 
    'Young adult', 
    'Children\'s fiction', 
    'Inspirational, self-help, and religious', 
    'Biography, autobiography, and memoir'
    ]

Label(search_book, text="SEARCH BOOK: ").grid(row=1, column=1)

Label(search_book, text="Genre: ").grid(row=2, column=1,sticky=E)
genre_entry = Combobox(search_book, values= genres, width=50)
genre_entry.grid(row=2, column=2)

Button(search_book, text="Search", command=search_button).grid(row=3, column=1, sticky=E)

validation_text = Label(search_book, text="")
validation_text.grid(row=3,column=2)

search_book.mainloop()