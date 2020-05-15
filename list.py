import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

dburl = 'postgresql://natasha:natasha@localhost:5432/mydb'
engine = create_engine(dburl)
db = scoped_session(sessionmaker(bind=engine))

def main():
    users = db.execute("SELECT username, password FROM users").fetchall()
    for user in users:
        print(f"{user.username} with password {user.password}.")

if __name__ == "__main__":
    main()
