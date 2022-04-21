class Book: 
    def __init__(self, title, release_year, author, id = None):
        self.title = title
        self.release_year = release_year
        self.author = author
        self.id = id