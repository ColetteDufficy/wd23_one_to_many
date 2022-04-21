from models.book import Book
from models.author import Author

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository


book_repository.delete_all() 
author_repository.delete_all()


#SAVE
author1 = Author("Bill Bryson")
author_repository.save(author1)
print(f"Bill Bryson has an id of {author1.id}")

#SAVE
author2 = Author("Terry Pratchett")
author_repository.save(author2)
print(f"Terry Pratchett has an id of {author2.id}")

# breakpoint()

#SAVE
book1 = Book("A Short History of Nearly Everything", 2003, author1)
book_repository.save(book1)
print(f"{book1.title}  has a book id {book1.id}")

#SAVE
book2 = Book("Notes From A Small Island", 1995, author1)
book_repository.save(book2)
print(f"{book2.title} has a book id {book2.id}")

#SAVE
book3 = Book("Good Omens", 1990, author2)
book_repository.save(book3)
print(f"{book3.title} has a book id {book2.id}")

#SELECT ALL
authors = author_repository.select_all()

books = book_repository.select_all()