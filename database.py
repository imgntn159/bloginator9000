import sqlite3

def makeTables():
    conn = sqlite3.connect("bloginator9000.db")
    c = conn.cursor()
    c.execute("create table if not exists post (body text, id text, userid text, timestamp DATETIME)")
    c.execute("create table if not exists comment (body text, id text, replyid text, userid text, timestamp DATETIME)")
    c.execute("create table if not exists user (username text, password text, id text)")
    conn.commit()

def addPost(body, postid, userid):
    conn = sqlite3.connect("bloginator9000.db")
    c = conn.cursor()
    c.execute("insert into post values ('{}', '{}', '{}', datetime(CURRENT_TIMESTAMP))".format(body, postid, userid))
    conn.commit()
    
def deletePost(postid):
    conn = sqlite3.connect("bloginator9000.db")
    c = conn.cursor()
    c.execute("update post set body='{}' where id='{}'".format("This post has been deleted",postid))
    data = c.fetchone()
    conn.commit()

def addComment(body, commentid, replyid, userid):
    conn = sqlite3.connect("bloginator9000.db")
    c = conn.cursor()
    c.execute("insert into comment values ('{}', '{}', '{}', '{}', datetime(CURRENT_TIMESTAMP))".format(body, commentid, replyid, userid))
    conn.commit()

def deleteComment(commentid):
    conn = sqlite3.connect("bloginator9000.db")
    c = conn.cursor()
    c.execute("update comment set body='{}' where id='{}'".format("This comment has been deleted",commentid))
    data = c.fetchone()
    conn.commit()
    
def newUser(username, password):
    conn = sqlite3.connect("bloginator9000.db")
    c = conn.cursor()
    isTaken = "SELECT username FROM user WHERE username=:\"%s\" LIMIT 1" % (username)
    c.execute(isTaken)
    data = c.fetchone()
    if data is None :
        m = hashlib.sha224(password)
        u = hashlib.sha224(username)
        query = "INSERT INTO login VALUES (\"%s\", \"%s\", \"%s\")" % (username, m.hexdigest(), u.hexdigest())
        c.execute(query)
        conn.commit()
        return True
    return False

def authenticate(username, password):
    conn = sqlite3.connect("bloginator9000.db")
    c = conn.cursor()
    m = hashlib.sha224(password).hexdigest()
    query = "SELECT password FROM user WHERE username=\"%s\"" % (username)
    c.execute(query)
    s1 = c.fetchone()
    if s1 == None:
        return False
    s2 = s1[0]
    if s2 == m:
        return True
    return False
