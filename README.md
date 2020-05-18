# Bookworm World 

# Video Presentation

YouTube Link - https://youtu.be/UX7rjQzKAbg

# Summary 

This Application was made with Flask, PostgreSQL, Python and a little of Javascript. This is an application that allows users to search for books and their reviews and even add their own reviews. 

## Sign Up

The user can sign up for Bookworm World by entering a username or password. However, the password is not kept discrete for learning purposes. There is an error if the username is NOT unique and if username and password is appropriate, the user is notified of the successful registration and given the opportunity to register again.

## Sign In 

Users can sign into their accounts using their created username and password. 

## Homepage

After log in, users are taken to their home page where they can look at the library of books or can look for a book. 

## Library of Books

Within the library of books is a list of almost 5000 books. For each, the user can check information and the review of the book by clicking 'Check Review'. 

### Book Page and Review

This consists of generic information about the book - title, author, year of publication and ISBN number. 

The user also has the opportunity to write a review for the book. Once the 'Submit' button is clicked, if the user is submitting a review for the first time, they will be notified of a successful addition of a review. The added review will show up on the book's Book Page. However, if the user is attempting to review the book more than once, they will be notified and stopped. 

The Book Page also features reviews of other users. 

## Search 

Within the Search application, the user can look for a book by entering the title, author or ISBN number of the book. If such a book does not exist, an error message will pop up, notifying the user that no book exists. 

If the book does exist, the Search Results will pop out, informing that a book has been found. The user is given the chance to check the review of the book, taking them back to the Book Page

## Log Out 

The option to log out is given in many stages of the application. The user may log out whenever they wish to, taking them back to the first page which prompts the user to log in
