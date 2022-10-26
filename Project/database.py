import psycopg2
import hashlib

def init_connection():
    return psycopg2.connect(database="userdetails", user='pavan', password='Pavan1997', host='database-1.cj4jm1b9clx6.ap-northeast-1.rds.amazonaws.com', port= '5432')

conn = init_connection()

cur = conn.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS public."User"(id int PRIMARY KEY,username TEXT,email TEXT,password TEXT)')

def fetch_email(email):
    cur.execute('SELECT email FROM public."User" WHERE public."User".email=%s',(email,))
    data = cur.fetchone()
    return data

def add_user(username,email,password):
    cur.execute('INSERT INTO public."User" (username,email,password) VALUES(%s,%s,%s)',(username,email,password))
    conn.commit()

def email_login_check(email,password):
    try:
        cur.execute('SELECT * FROM public."User" WHERE public."User".email =%s AND public."User".password = %s',(email,password))
        data = cur.fetchone()
        return data
    except psycopg2.ProgrammingError as exc:
        print(exc.message)
        conn.rollback()
    except psycopg2.InterfaceError as exc:
        print(exc.message)
        conn = psycopg2.connect(database="userdetails", user='pavan', password='Pavan1997', host='database-1.cj4jm1b9clx6.ap-northeast-1.rds.amazonaws.com', port= '5432')
        cursor = conn.cursor()


def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False