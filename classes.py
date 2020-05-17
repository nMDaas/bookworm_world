class User:

    counter = 1
    def __init__(self, id, username, password):

    self.id = User.counter
    User.counter += 1

    self.id = id
    self.username = username
    self.password = password

class Review:

    def __init__ (self, username, password)

    self.username = username
    self.password = password
