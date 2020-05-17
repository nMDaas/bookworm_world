import os

from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

dburl = 'postgresql://natasha:natasha@localhost:5432/mydb'
engine = create_engine(dburl)
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home", methods=["POST"])
def home():
    username = request.form.get("username")
    password = request.form.get("password")
    founduser = db.execute("SELECT username, password FROM users WHERE username = :username",
                        {"username": username, "password": password}).fetchone()
    if (founduser.password == password):
        return render_template("home.html", founduser=founduser)
    else:
        return render_template("incorrect.html")

@app.route("/library", methods=["POST"])
def library():
    print("*** library() was called ***")
    books = db.execute("SELECT * FROM books").fetchall()
    return render_template("library.html", books=books)

@app.route("/searchbook", methods=["POST"])
def searchbook():
    return render_template("searchbook.html")

#-----

@app.route("/library/<book_title>")
def book(book_title):
    print("*** library(book_title) was called ***")
    
    """List details about a single book."""

    reviewbook = db.execute("SELECT title, isbn, author, publication_year FROM books WHERE title = :title",
                {"title": book_title}).fetchone()

    return render_template("reviewbook.html", reviewbook=reviewbook)

#-----

@app.route("/search", methods=["POST"])
def search():
    """Find a book."""

    # Get title information.
    title = request.form.get("title")
    foundtitle = db.execute("SELECT isbn, title, author, publication_year FROM books WHERE title = :title",
                        {"title": title}).fetchone()

    # Get author information.
    author = request.form.get("author")
    foundauthor = db.execute("SELECT isbn, title, author, publication_year FROM books WHERE author = :author",
                        {"author": author}).fetchone()

    # Get ISBN information.
    isbn = request.form.get("isbn")
    foundisbn = db.execute("SELECT isbn, title, author, publication_year FROM books WHERE isbn = :isbn",
                        {"isbn": isbn}).fetchone()

    if (foundtitle != None):
        foundbook = foundtitle
    elif (foundauthor != None):
        foundbook = foundauthor
    elif(foundisbn != None):
        foundbook = foundisbn
    else:
        return render_template("failed_search.html")

    return render_template("search.html", foundbook=foundbook)
