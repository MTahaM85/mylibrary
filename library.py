class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}"

class Library:
    books = []

    def add_book(self, title, author):
        self.books.append(Book(title, author))
        return f"'{title}' added."

    def remove_book(self, title):
        for b in self.books:
            if b.title == title:
                self.books.remove(b)
                return f"'{title}' removed."
        return f"{title} not found!"

    def search_book(self, title):
        for b in self.books:
            if title in b.title:
                return b

    def show_books(self):
        list_of_books = []
        for i in range(len(self.books)):
            list_of_books.append(f"{i + 1}\n{str(self.books[i])}")

        return "\n\n".join(list_of_books)