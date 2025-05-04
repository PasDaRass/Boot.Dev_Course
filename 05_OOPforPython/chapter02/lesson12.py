class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        pass


class Library:
    def __init__(self, name):
        self.name = name
        self.books = [] 
        pass

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        for i in self.books:
            if (i.title.lower() == book.title.lower() and i.author.lower() == book.author.lower()):
                self.books.remove(i)

    def search_books(self, search_string):
        search_arr = []
        for i in self.books:
            query_title = i.title.lower().split()
            query_author = i.author.lower().split()
            if (search_string.lower() in query_title or search_string.lower() in query_author):
                search_arr.append(i)
        return search_arr
