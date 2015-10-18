import sqlite3, hashlib

def makeTables():
    conn = sqlite3.connect("bloginator9000.db")
    c = conn.cursor()
    c.execute("create table if not exists post (title text NOT NULL, body text NOT NULL, postid INTEGER PRIMARY KEY, userid text, timestamp DATETIME)")
    c.execute("create table if not exists comment (body text NOT NULL, id INTEGER PRIMARY KEY, postid int, userid text, timestamp DATETIME)")
    c.execute("create table if not exists user (username text, password text, id text)")
    conn.commit()

def addPost(title, body, userid):
    conn = sqlite3.connect("bloginator9000.db")
    c = conn.cursor()
    c.execute("insert into post values ('{}', '{}', NULL, '{}', datetime(CURRENT_TIMESTAMP))".format(title, body, userid))
    conn.commit()

def getPosts():
    conn = sqlite3.connect("bloginator9000.db")
    c = conn.cursor()
    c.execute("select * from post order by timestamp")
    data = c.fetchall()
    data.reverse()
    data = [dict(zip(['title','blogtext','postid','username','date'], each)) for each in data]
    return data

def getPost(key, postid):
    conn = sqlite3.connect("bloginator9000.db")
    c = conn.cursor()
    c.execute("select * from post where {} = '{}'".format(key,postid))
    data = c.fetchall()
    data = [dict(zip(['title','blogtext','postid','username','date'], each)) for each in data]
    return data

def addComment(body, replyid, userid):
    conn = sqlite3.connect("bloginator9000.db")
    c = conn.cursor()
    c.execute("insert into comment values ('{}', NULL, '{}', '{}', datetime(CURRENT_TIMESTAMP))".format(body, replyid, userid))
    conn.commit()

def getComments(key, postid):
    conn = sqlite3.connect("bloginator9000.db")
    c = conn.cursor()
    c.execute("select * from comment where {} = '{}' order by timestamp".format(key,postid))
    data = c.fetchall()
    data.reverse()
    data = [dict(zip(['commenttext','commentid','postid','username','date'], each)) for each in data]    
    return data

def newUser(username, password):
    conn = sqlite3.connect("bloginator9000.db")
    c = conn.cursor()
    isTaken = "SELECT username FROM user WHERE username=\"%s\" LIMIT 1" % (username)
    c.execute(isTaken)
    data = c.fetchone()
    if data is None :
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
