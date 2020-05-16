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
    books = db.execute("SELECT * FROM books").fetchall()
    return render_template("index.html", books=books)

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

    return render_template("search.html", foundtitle=foundtitle, foundauthor=foundauthor, foundisbn=foundisbn)
