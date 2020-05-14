class Users:

    def __init__(self, username, password):
        self.username = username
        self.password = password

class Books:

    def __init__(self, ISBN, title, author, publication_year):
        self.ISBN = ISBN
        self.title = title
        self.author = author
        self.publication_year = publication_year

# To print book details on Book Page
    def book_page(self):
        print(f"ISBN: {self.ISBN}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Publication Year: {self.publication_year}")

# To print book titles based on search parameter
    def book_list(self):
        print(f"Title: {self.title}")

class Reviews:

    def __init__(self, book_review):
        self.book_review = book_review

# List of users who have submitted a review
    self.users = []

    def add_user(self, username):
        self.users.append(p) #user added to list
        username.username = self.by_user
