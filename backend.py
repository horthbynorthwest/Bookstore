import sqlite3

def connect():
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    conn.commit()
    conn.close()

def add(title, author, year, isbn):
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title, author, year, isbn))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()   
    cursor.execute("SELECT * FROM book")
    all_books = cursor.fetchall()
    conn.close()
    return all_books

def search(title="", author="", year="", isbn=""):
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()   
    cursor.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
    search_books = cursor.fetchall()
    conn.close()
    return search_books

connect()
add("The Earth","John Smith", 1918, 180982)
print(view())
print(search(author="John Smith"))