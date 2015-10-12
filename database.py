import sqlite3

conn = sqlite3.connect("bloginator9000.db")

c = conn.cursor()

q = "create table post (body text, id text, userid integer)"
c.execute(q)

q = "create table comment (body text, id text, replyid text, userid integer)"
c.execute(q)

q = "create table user (username text, password text, id integer)"
c.execute(q)

conn.commit()
