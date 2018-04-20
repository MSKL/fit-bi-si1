class User:
    id = 1

    def __init__(self, name, email):
        self.id = User.id
        self.name = name
        self.email = email
        User.id += 1
