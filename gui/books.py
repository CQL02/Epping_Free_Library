import sqlite3


conn = sqlite3.connect('EppingFreeLibrary.db')


def add_book(new_book):
    c = conn.cursor()
    c.execute("INSERT INTO books VALUES (?,?,?,?,?)",new_book)
    conn.commit()
    conn.close()

def delete_book(ID, name):
    c = conn.cursor()
    c.execute("DELETE from books WHERE ID=? AND name=?", ID, name)
    conn.commit()
    conn.close()

def update_book(customer_id, customer_name, availbility, book_id, book_name):
    c = conn.cursor()
    c.execute("UPDATE members SET borrowed_customer_id=?, borrowed_customer_name=?, availability WHERE book_id=? AND book_name=?",
            customer_id,
            customer_name,
            availbility,
            book_id,
            book_name
        )
    conn.commit()
    conn.close()

def book_list():
    c = conn.cursor()
    books = c.fetchall()
    for book in books:
        print(book)

def available_books():
    c = conn.cursor()
    c.execute("SELECT * FROM books WHERE availability = 'TRUE'")
    books = c.fetchall()
    for book in books:
        print(book)