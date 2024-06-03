class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def __str__(self) :
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"
    
    def check_out(self):
        self.is_available = False

    def return_book(self):
        self.is_available = True


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def __str__(self) -> str:
        return f"Member: {self.name} (ID: {self.member_id})"
    
    def borrow_book(self, book):
        if book.is_available:
            self.borrowed_books.append(book)
            book.check_out()
            return True
        return False
    
    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.return_book()
            return True
        return False

    
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            return True
        return False
    
    def register_member(self, member):
        self.members.append(member)

    def find_book_by_title(self, title):
        return [book for book in self.books if book.title == title]

    def find_book_by_author(self, author):
        return [book for book in self.books if book.author == author]

    def display_available_books(self):
        return [book for book in self.books if book.is_available]

    def __str__(self):
        books_list = "\n".join(str(book) for book in self.books)
        members_list = "\n".join(str(member) for member in self.members)
        return f"Library: {self.name}\nBooks:\n{books_list}\n\nMembers:\n{members_list}"


class Librarian(Member):
    def add_book_to_library(self, library, book):
        library.add_book(book)

    def remove_book_from_library(self, library, book):
        library.remove_book(book)


class Admin(Librarian):
    def view_all_members(self, library):
        return library.members

    def view_all_books(self, library):
        return library.books


def main():
    library = Library("Central Library")

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Register Member")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. View All Books")
        print("7. View Available Books")
        print("8. View All Members")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            book = Book(title, author, isbn)
            library.add_book(book)
            print("Book added successfully!")

        elif choice == "2":
            isbn = input("Enter book ISBN to remove: ")
            book_to_remove = None
            for book in library.books:
                if book.isbn == isbn:
                    book_to_remove = book
                    break
            if book_to_remove:
                library.remove_book(book_to_remove)
                print("Book removed successfully!")
            else:
                print("Book not found!")

        elif choice == "3":
            name = input("Enter member name: ")
            member_id = input("Enter member ID: ")
            member = Member(name, int(member_id))
            library.register_member(member)
            print("Member registered successfully!")

        elif choice == "4":
            member_id = int(input("Enter member ID: "))
            isbn = input("Enter book ISBN to borrow: ")
            member = next((m for m in library.members if m.member_id == member_id), None)
            book = next((b for b in library.books if b.isbn == isbn), None)
            if member and book:
                if member.borrow_book(book):
                    print("Book borrowed successfully!")
                else:
                    print("Book is not available!")
            else:
                print("Member or Book not found!")

        elif choice == "5":
            member_id = int(input("Enter member ID: "))
            isbn = input("Enter book ISBN to return: ")
            member = next((m for m in library.members if m.member_id == member_id), None)
            book = next((b for b in library.books if b.isbn == isbn), None)
            if member and book:
                if member.return_book(book):
                    print("Book returned successfully!")
                else:
                    print("Book was not borrowed by this member!")
            else:
                print("Member or Book not found!")

        elif choice == "6":
            print("\nAll Books in the Library:")
            for book in library.books:
                print(book)

        elif choice == "7":
            print("\nAvailable Books in the Library:")
            for book in library.display_available_books():
                print(book)

        elif choice == "8":
            print("\nAll Members in the Library:")
            for member in library.members:
                print(member)

        elif choice == "9":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()