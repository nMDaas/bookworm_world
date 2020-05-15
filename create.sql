--> NOTE: I need something to link in order to check whether a user has submitted
--> a review or not

CREATE TABLE users(
   username VARCHAR UNIQUE,
   password VARCHAR NOT NULL --> Currently on VARCHAR, so NOT secret
 );


 CREATE TABLE books(
   ISBN VARCHAR PRIMARY KEY,
   title VARCHAR NOT NULL,
   author VARCHAR NOT NULL,
   publication_year INTEGER NOT NULL
 );

 CREATE TABLE reviews(
   book_reviewed VARCHAR NOT NULL,
   by_user VARCHAR NOT NULL, --> Linked to username
   review VARCHAR NOT NULL
 );


--> Test insertions run in terminal
 INSERT INTO users (username, password) VALUES('Alice', 'cat');
 INSERT INTO users (username, password) VALUES('Bob', 'dog');

 INSERT INTO books (ISBN, title, author, publication_year) VALUES(0380795272, 'Krondor: The Betrayal', 'Raymond E. Feist', 1998);
 INSERT INTO books (ISBN, title, author, publication_year) VALUES(1416949658, 'The Dark Is Rising', 'Susan Cooper', 1973);
 INSERT INTO books (ISBN, title, author, publication_year) VALUES(1857231082, 'The Black Unicorn','Terry Brooks', 1987);

INSERT INTO reviews (book_reviewed, by_user, review) VALUES('The Dark Is Rising', 'Alice', 'Great Book!');
INSERT INTO reviews (book_reviewed, by_user, review) VALUES('The Black Unicorn', 'Alice', 'Not great');
INSERT INTO reviews (book_reviewed, by_user, review) VALUES('The Black Unicorn', 'Bob', 'Horrible plot!');

--> Test Queries run in terminal
SELECT * FROM reviews WHERE by_user = 'Alice';

--> Joint query by foreign key
SELECT book_reviewed, review, username FROM reviews JOIN users ON users.username = reviews.by_user;
