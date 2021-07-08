#Called test, but really the actual import file to import mediumbooks.csv, a copy of books.csv

import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

dburl = 'postgresql://natasha:natasha@localhost:5432/mydb'
engine = create_engine(dburl)
db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("mediumbooks.csv")
    reader = csv.reader(f)
    for ISBN, title, author, publication_year in reader:
        db.execute("INSERT INTO books(ISBN, title, author, publication_year) VALUES (:ISBN, :title, :author, :publication_year)",
            {"ISBN":ISBN, "title":title, "author":author, "publication_year":publication_year})
        print(f"Added book {title} by {author} with ISBN {ISBN}, published in {publication_year}.")
        db.commit()

if __name__ == "__main__":
    main()
