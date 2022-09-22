import sqlite3


conn = sqlite3.connect('EppingFreeLibrary.db')


def add_staff(ID, name, password, contact):
    c = conn.cursor()
    c.execute("INSERT INTO staffs VALUES (?,?,?,?)", (ID, name, password, contact))
    conn.commit()

def delete_staff(ID, name, password):
    c = conn.cursor()
    c.execute("DELETE from staffs WHERE (ID=? AND name=?) AND password=?", (ID, name, password))
    conn.commit()

def check_staff(id, name, password):
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM staffs WHERE (ID=? AND name=?) AND password=?", (id, name, password))
    conn.commit()
    return c.fetchone()

def check_staff_login(name, password):
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM staffs WHERE name=? AND password=?", (name, password))
    conn.commit()
    return c.fetchone()

def staffs_list():
    c = conn.cursor()
    c.execute("SELECT * FROM staffs")
    conn.commit()
    return c.fetchall()

def get_id():
    c = conn.cursor()
    c.execute("SELECT * FROM staffs WHERE ID=(SELECT max(ID) FROM staffs)")
    conn.commit()
    last_id = c.fetchone()
    if last_id == None:
        return 1
    return last_id[0] + 1

# add_staff(2,"Ali","babi")
# delete_staff(2,"Ali","babi")