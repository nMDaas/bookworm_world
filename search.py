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

    # Prompt user to find book via its title.
    title = (input("\nTitle: "))
    findbook = db.execute("SELECT isbn, title, author, publication_year FROM books WHERE title = :title",
                        {"title": title}).fetchone()

    print(f"{findbook.title} ({findbook.isbn}) by {findbook.author} published in {findbook.publication_year}")
    # Make sure flight is valid.
    #if flight is None:
    #    print("Error: No such flight.")
    #    return

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
