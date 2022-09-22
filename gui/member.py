from asyncio.windows_events import NULL
import sqlite3

conn = sqlite3.connect('EppingFreeLibrary.db')


def add_member(id, name, contact):
    c = conn.cursor()
    c.execute("INSERT INTO members VALUES (?,?,?,?,?,?)",(id, name, contact,0,None,""))
    conn.commit()
    

def delete_member(ID,name):
    c = conn.cursor()
    c.execute("DELETE FROM members WHERE ID=? AND name=?",(ID,name))
    conn.commit()
    

def update_member(id, loan, borrowed_book_id):
    c = conn.cursor()
    c.execute("UPDATE members SET borrowed_book_id=?, loan=? WHERE ID=?",(borrowed_book_id, loan, id))
    conn.commit()
    
def get_borrowed_book_id(id):
    c = conn.cursor()
    c.execute("SELECT * FROM members WHERE ID=?", (id,))
    conn.commit()
    return c.fetchone()[4]

def member_exist(id):
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM members WHERE ID=?", (id,))
    conn.commit()
    return c.fetchone()[0]

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
    if id == "" and name == "":
        c.execute("SELECT * FROM members")
    elif id==None:
        c.execute("SELECT * FROM members WHERE name LIKE ?",('%'+name+'%',))
    elif name=="":
        c.execute("SELECT * FROM members WHERE ID=?",(id,))
    else:
        c.execute("SELECT * FROM members WHERE name LIKE ? OR ID=?",('%'+name+'%',id))
    conn.commit()
    return c.fetchall()


def check_member(id, name):
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM members WHERE ID=? AND name=?", (id, name))
    conn.commit()
    return c.fetchone()

def get_loan(id):
    c = conn.cursor()
    c.execute("SELECT * FROM members WHERE ID=?", (id,))
    conn.commit()
    return c.fetchone()[3]

# print(members_list(3,None))
# update_member(9,0,None)
# print(get_borrowed_book_id(5))

