from mylibrary.library import Library

print("""
 ____    ____   _
| |\ \  / /| | | |
| | \ \/ / | | | |____
|_|  \__/  |_| |______|
\n""")

print("Welcome to mylibrary!\n\n")

library = Library()
while True:
    print("""
    1. Add book
    2. Remove book
    3. Search book
    4. Show books
    5. Exit
    """)

    request = input("Enter a number from menu: ")

    if request == '1':
        title = input("Title: ")
        author = input("Author: ")
        print(library.add_book(title, author))
    elif request == '2':
        title = input("Title: ")
        print(library.remove_book(title))
    elif request == '3':
        title = input("Title: ")
        print(library.search_book(title))
    elif request == '4':
        print(library.show_books())
    elif request == '5':
        break
    else:
        continue