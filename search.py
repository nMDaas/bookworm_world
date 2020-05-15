#This is a mock search engine

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
        print(f"{book.title} ({book.isbn}) by {book.author} published in {book.publication_year}")

    #search option
    searchmethod = input("Search by (title/ISBN/author): ")

    #search by title
    if (searchmethod == "title"):

        # Prompt user to find book via its title.
        title = (input("\nTitle: "))
        findbook = db.execute("SELECT isbn, title, author, publication_year FROM books WHERE title = :title",
                            {"title": title}).fetchone()
        #Make sure title is valid
        if findbook is None:
            print(f"Error: No book with this {title} exists.")
            return
        else:
            print(f"{findbook.title} ({findbook.isbn}) by {findbook.author} published in {findbook.publication_year}")

    #search by ISBN
    if (searchmethod == "ISBN"):

        # Prompt user to find book via its title.
        ISBN = (input("\nISBN: "))
        findbook = db.execute("SELECT isbn, title, author, publication_year FROM books WHERE ISBN = :ISBN",
                            {"ISBN": ISBN}).fetchone()
        #Make sure ISBN is valid
        if findbook is None:
            print(f"Error: No book with this {ISBN} exists.")
            return
        else:
            print(f"{findbook.title} ({findbook.isbn}) by {findbook.author} published in {findbook.publication_year}")

    #search by Author
    if (searchmethod == "author"):

        # Prompt user to find book via its title.
        author = (input("\aauthor: "))
        findbook = db.execute("SELECT isbn, title, author, publication_year FROM books WHERE author = :author",
                            {"author": author}).fetchone()
        #Make sure author is valid
        if findbook is None:
            print(f"Error: No book by {author} exists.")
            return
        else:
            print(f"{findbook.title} ({findbook.isbn}) by {findbook.author} published in {findbook.publication_year}")


    # List passengers.
    #passengers = db.execute("SELECT name FROM passengers WHERE flight_id = :flight_id",
    #                        {"flight_id": flight_id}).fetchall()
    #print("\nPassengers:")
    #for passenger in passengers:
    #    print(passenger.name)
    #if len(passengers) == 0:
    #    print("No passengers.")

if __name__ == "__main__":
    main()
