"""
This program allows for simple book management as well as exception handling,
with two classes, BOOK and bookmanage

"""


class BOOK:
    def __init__(self, title, author):              #initialize the class of BOOK
        self.title = title
        self.author = author


class bookmanage:

    def add_book(self, booklist, title, author):                      #add a book to book list
        for book in booklist:
            if book.title == title and book.author == author:
                print(f"book already exists: {title}")
                return
        new_book = BOOK(title, author)
        booklist.append(new_book)
        print(f"book added: {new_book}")

    def remove_book(self, booklist,title):                            #remove a book from book list
        for book in booklist:
            if book.title == title:
                booklist.remove(book)
                print(f"book removed: {title}")
            else:
                print(f"book not existed: {title}")

    def search_book(self, booklist,title):                            #search a book in book list
        for book in booklist:
            if book.title == title:
                print(f"book found：{book}")
                return
        print(f"book not found：{title}")

def main():
    management = bookmanage()

    booklist = []                               #initialize a book list

    while True:
        command = input("enter command ADD, REMOVE, SEARCH or EXIT").strip().upper()
        if command == 'EXIT':                   #when input exit, stop the book management
            break
        elif command == 'ADD':                  #add operation
            title = input("please enter the titleof the book: ")
            author =input("please enter the name of the author: ")
            management.add_book(booklist, title,author)

        elif command == 'REMOVE':               #remove operation
            title = input("please enter the title of the book you want to remove: ")
            management.remove_book(booklist, title)

        elif command == 'SEARCH':               #search operation
            title = input("please enter the title of the book you want to search: ")
            management.search_book(booklist, title)

        else:
            print("invalid input, please enter ADD, REMOVE, SEARCH or EXIT")

main()