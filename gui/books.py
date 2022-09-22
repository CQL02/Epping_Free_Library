import sqlite3


conn = sqlite3.connect('EppingFreeLibrary.db')


def add_book(id, name, genre1, genre2):
    c = conn.cursor()
    c.execute("INSERT INTO books VALUES (?,?,?,?,?,?)", (id, name, "TRUE", None, genre1, genre2))
    conn.commit()


def delete_book(ID, name):
    c = conn.cursor()
    c.execute("DELETE from books WHERE ID=? AND name=?", (ID, name))
    conn.commit()


def update_book(customer_id, availbility, book_id):
    c = conn.cursor()
    c.execute("UPDATE books SET borrowed_customer_id=?, availability=? WHERE ID=?",
            (
                customer_id,
                availbility,
                book_id)
        )
    conn.commit()

def book_availabilty(id):
    c = conn.cursor()
    c.execute("SELECT * FROM books WHERE ID=?", (id,))
    conn.commit()
    return c.fetchone()[2]

def book_exist(id):
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM books WHERE ID=?", (id,))
    conn.commit()
    return c.fetchone()[0]

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


def get_id():
    c = conn.cursor()
    c.execute("SELECT * FROM books WHERE ID=(SELECT max(ID) FROM books)")
    conn.commit()
    last_id = c.fetchone()
    if last_id == None:
        return 1
    return last_id[0] + 1

def get_borrowed_id(id):
    c = conn.cursor()
    c.execute("SELECT * FROM books WHERE id=?", (id,))
    conn.commit()
    return c.fetchone()[3]

def search_genre(genre):
    c = conn.cursor()
    c.execute("SELECT * FROM books WHERE genre1=? OR genre2=?", (genre, genre))
    conn.commit()
    return c.fetchall()


# add_book(get_id(), "Jian Meng UGLY!!!","Thrillers and horror","Biography, autobiography, and memoir")
# delete_book(5,"Jian Meng UGLY!!!")
# update_book(None,"TRUE",2)
# print(book_availabilty(1))
# print(book_exist(3))