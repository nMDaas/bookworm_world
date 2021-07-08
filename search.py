#This is a search engine through which a user can search by title/ISBN/author

import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

dburl = 'postgresql://natasha:natasha@localhost:5432/mydb'
engine = create_engine(dburl)
db = scoped_session(sessionmaker(bind=engine))

def main():

    # List all books.
    books = db.execute("SELECT isbn, title, author, publication_year FROM books").fetchall()
    for book in books:
        print(f"{book.title}")

    #search option
    searchmethod = input("Search by (title/ISBN/author): ")

    #search by title
    if (searchmethod == "title"):

        # Prompt user to find book via its title.
        title = (input("\nTitle: "))
        print("SEARCH RESULTS:")
        findbook = db.execute("SELECT isbn, title, author, publication_year FROM books WHERE title = :title",
                            {"title": title}).fetchone()
        #Make sure title is valid
        if findbook is None:
            print(f"Error: No book with title {title} exists.")
            return
        else:
            print(f"{findbook.title}")

    #search by ISBN
    if (searchmethod == "ISBN"):

        # Prompt user to find book via its title.
        ISBN = (input("\nISBN: "))
        print("SEARCH RESULTS:")
        findbook = db.execute("SELECT isbn, title, author, publication_year FROM books WHERE ISBN = :ISBN",
                            {"ISBN": ISBN}).fetchone()
        #Make sure ISBN is valid
        if findbook is None:
            print(f"Error: No book with ISBN number {ISBN} exists.")
            return
        else:
            print(f"({findbook.isbn}) {findbook.title}")

    #search by Author
    if (searchmethod == "author"):

        # Prompt user to find book via its title.
        author = (input("\aauthor: "))
        print("SEARCH RESULTS:")
        findbook = db.execute("SELECT isbn, title, author, publication_year FROM books WHERE author = :author",
                            {"author": author}).fetchone()
        #Make sure author is valid
        if findbook is None:
            print(f"Error: No book by {author} exists.")
            return
        else:
            print(f"{findbook.title} by {findbook.author}")

if __name__ == "__main__":
    main()
