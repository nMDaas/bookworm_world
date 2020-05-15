#This is a search engine through which a user can search by title/ISBN/author

import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

dburl = 'postgresql://natasha:natasha@localhost:5432/mydb'
engine = create_engine(dburl)
db = scoped_session(sessionmaker(bind=engine))

def main():

    #this comes after the search and the user chooses to view details about one book
    bookpage_title = (input("\aTitle of Book Page: "))
    bookpage = db.execute("SELECT isbn, title, author, publication_year FROM books where title = :title",
            {"title": bookpage_title}).fetchone()

    print(bookpage.title)
    print("")
    print("Author: ", bookpage.author)
    print("Year of publication: ", bookpage.publication_year)
    print("ISBN number: ", bookpage.isbn)

if __name__ == "__main__":
    main()
