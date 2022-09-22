import sqlite3

conn = sqlite3.connect('EppingFreeLibrary.db')

c = conn.cursor()
# c.execute("""
#     CREATE TABLE members (
#         ID integer,
#         name text,
#         contact integer,
#         loan real,
#         borrowed_book_id integer,
#         borrowed_book text
#     )""")

# c.execute("""
#     CREATE TABLE stuffs (
#         ID integer,
#         name text,
#         password text,
#         contact text
#     )""")

# c.execute("""
#     CREATE TABLE books (
#         ID integer,
#         name text,
#         availability text,
#         borrowed_customer_id integer,
#         borrowed_customer_name text
#     )""")

# c.execute("""
#     INSERT INTO stuffs VALUES(
#         1,
#         'Hi',
#         123456
#     )""")

c.execute("ALTER TABLE books ADD genre text")

conn.commit()
conn.close()