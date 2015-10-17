import sqlite3, hashlib

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

def getPosts():
    conn = sqlite3.connect("bloginator9000.db")
    c = conn.cursor()
    c.execute("select rowid,* from post order by timestamp")
    data = c.fetchall()
    data.reverse()
    data = [dict(zip(['rowid','blogtext','postid','username','date'], each)) for each in data]
    return data

def getPost(postid):
    conn = sqlite3.connect("bloginator9000.db")
    c = conn.cursor()
    c.execute("select rowid,* from post where rowid = " + postid)
    data = c.fetchall()
    data = [dict(zip(['rowid','blogtext','postid','username','date'], each)) for each in data]
    print data[0]
    return data[0]

def editPost(newtext, postid):
    conn = sqlite3.connect("bloginator9000.db")
    c = conn.cursor()
    c.execute("update post set body='{}' where id='{}'".format(newtext, postid))
    return c.fetchall()

def addComment(body, commentid, replyid, userid):
    conn = sqlite3.connect("bloginator9000.db")
    c = conn.cursor()
    c.execute("insert into comment values ('{}', '{}', '{}', '{}', datetime(CURRENT_TIMESTAMP))".format(body, commentid, replyid, userid))
    conn.commit()

def getComments():
    conn = sqlite3.connect("bloginator9000.db")
    c = conn.cursor()
    c.execute("select * from comment order by timestamp")
    data = c.fetchall()
    data.reverse()
    return data

def editComment(newtext, commentid):
    conn = sqlite3.connect("bloginator9000.db")
    c = conn.cursor()
    c.execute("update comment set body='{}' where id='{}'".format(newtext, commentid))
    data = c.fetchone()
    conn.commit()
    
def newUser(username, password):
    conn = sqlite3.connect("bloginator9000.db")
    c = conn.cursor()
    isTaken = "SELECT username FROM user WHERE username=\"%s\" LIMIT 1" % (username)
    c.execute(isTaken)
    data = c.fetchone()
    print "B"
    if data is None :
        print "A"
        m = hashlib.sha224(password)
        u = hashlib.sha224(username)
        query = "INSERT INTO user VALUES (\"%s\", \"%s\", \"%s\")" % (username, m.hexdigest(), u.hexdigest())
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
