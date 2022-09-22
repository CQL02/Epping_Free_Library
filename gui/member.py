import sqlite3

conn = sqlite3.connect('EppingFreeLibrary.db')


def add_member(id, name, contact):
    c = conn.cursor()
    c.execute("INSERT INTO members VALUES (?,?,?,?,?,?)",(id, name, contact,0,0,""))
    conn.commit()
    

def delete_member(ID,name):
    c = conn.cursor()
    c.execute("DELETE FROM members WHERE ID=? AND name=?",(ID,name))
    conn.commit()
    

def update_member(customer_id, customer_name, borrowed_book_id, borrowed_book_name):
    c = conn.cursor()
    c.execute("UPDATE members SET borrowed_book_id=?, borrowed_book_name=? WHERE customer_id=? AND customer_name=?",
            (borrowed_book_id,
            borrowed_book_name,
            customer_id,
            customer_name)
        )
    conn.commit()
    

def get_id():
    c = conn.cursor()
    c.execute("SELECT * FROM members WHERE ID=(SELECT max(ID) FROM members)")
    conn.commit()
    last_id = c.fetchone()
    if last_id == None:
        return 1
    return last_id[0] + 1


def members_list(id, name):
    c = conn.cursor()
    if id == None and name == None:
        c.execute("SELECT * FROM members")
    elif name==None:
        c.execute("SELECT * FROM members WHERE ID=?",(id,))
    elif id==None:
        c.execute("SELECT * FROM members WHERE name LIKE ?",('%'+name+'%',))
    else:
        c.execute("SELECT * FROM members WHERE name LIKE ? OR ID=?",('%'+name+'%',id))
    conn.commit()
    return c.fetchall()


def check_member(id, name):
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM members WHERE ID=? AND name=?", (id, name))
    conn.commit()
    return c.fetchone()

# print(members_list(3,None))

