import os

from flask import Flask, render_template, request, make_response
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

dburl = 'postgresql://natasha:natasha@localhost:5432/mydb'
engine = create_engine(dburl)
db = scoped_session(sessionmaker(bind=engine))

#Default first screen - takes you to log in
@app.route("/")
def index():
    return render_template("index.html")

#Login screen - option to log in or sign up
@app.route("/login", methods=["POST"])
def login():
    return render_template("login.html")

#Sign up
@app.route("/signup", methods=["POST"])
def signup():
    return render_template("signup.html")

#From Sign up - Takes you if Successful registration
@app.route("/registered", methods=["POST"])
def registered():
    new_username = request.form.get("new_username")
    new_password = request.form.get("new_password")
    db.execute("INSERT INTO users (username, password) VALUES (:username, :password)",
            {"username": new_username, "password": new_password})
    db.commit()
    return render_template("success.html")

#Takes you to Home, then login
@app.route("/home", methods=["POST"])
def home():
    username = request.form.get("username")
    password = request.form.get("password")
    founduser = db.execute("SELECT username, password FROM users WHERE username = :username",
                        {"username": username, "password": password}).fetchone()
    html = render_template("home.html", founduser=founduser)
    response = make_response(html)
    response.set_cookie('theUserName', username)
    if (founduser.password == password):
        return response
    else:
        return render_template("incorrect.html")

#Takes you to library of books
@app.route("/library", methods=["POST"])
def library():
    print("*** library() was called ***")
    books = db.execute("SELECT * FROM books").fetchall()
    return render_template("library.html", books=books)

#Takes you to search screen
@app.route("/searchbook", methods=["POST"])
def searchbook():
    return render_template("searchbook.html")

@app.route("/logout", methods=["POST"])
def logout():
    return render_template("index.html")

#Takes you to book page of a book
@app.route("/library/<book_title>")
def book(book_title):

    """List details about a single book."""
    current_user = request.cookies.get('theUserName')
    reviews = db.execute("SELECT by_user, review, book_reviewed FROM reviews WHERE book_reviewed = :book_reviewed",
                {"book_reviewed": book_title}).fetchall()
    reviewbook = db.execute("SELECT title, isbn, author, publication_year FROM books WHERE title = :title",
                            {"title": book_title}).fetchone()
    books = db.execute("SELECT * FROM books").fetchall()
    html2 = render_template("reviewbook.html", reviews=reviews, reviewbook=reviewbook, books=books, current_user=current_user)
    response2 = make_response(html2)
    response2.set_cookie('theBook', book_title)
    return response2


#add a review
@app.route("/addreview", methods=["POST"])
def addreview():
    review = request.form.get("review")
    by_user = request.cookies.get('theUserName')
    book_reviewed = request.cookies.get('theBook')
    check = db.execute("SELECT book_reviewed, by_user, review FROM reviews WHERE book_reviewed = :book_reviewed and by_user = :by_user",
                        {"book_reviewed": book_reviewed, "by_user": by_user}).fetchone()

    if (check == None):
        db.execute("INSERT INTO reviews (book_reviewed, by_user, review) VALUES (:book_reviewed, :by_user, :review)",
                {"book_reviewed": book_reviewed, "by_user": by_user, "review": review})
        db.commit()
        return render_template("reviewdone.html", book_reviewed=book_reviewed)
    else:
        return render_template("badreview.html", book_reviewed=book_reviewed)

#search engine
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
