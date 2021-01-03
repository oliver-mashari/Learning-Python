class Book():

    def __init__(self,title,author,pages):

        self.title = title
        self.author = author
        self.pages = pages

    # Special method for using str with methods
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __len__(self):
        return self.pages

book = Book('Python Rocks', 'Oliver', 200)
print(book)
print(len(book))