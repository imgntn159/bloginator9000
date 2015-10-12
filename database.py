import sqlite3

conn = sqlite3.connect("bloginator9000.db")

c = conn.cursor()

c.execute("create table if not exists post (body text, id text, userid integer)")

c.execute("create table if not exists comment (body text, id text, replyid text, userid integer)")

c.execute("create table if not exists user (username text, password text, id integer)")

def addPost(body, postid, userid):
    c.execute("insert into post values ('{}', '{}', {});".format(body, postid, userid))
    
def addComment(body, commentid, replyid, userid):
    c.execute("insert into comment values ('{}', '{}', '{}', {});".format(body, commentid, replyid, userid))
    
def addUser(username, password, userid):
    c.execute("insert into user values ('{}', '{}', {});".format(username, password, userid))

addPost("blablabla","P1",3)
addComment("very interesting","C1","P1",3)
addUser("abc","password",3)

conn.commit()
