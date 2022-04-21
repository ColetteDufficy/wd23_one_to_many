from db.run_sql import run_sql

from models.book import Book #importing the class of Book
import repositories.author_repository as author_repository #import everthing under the name 'author_repository'


#SAVE
def save(book):
    sql = """
        INSERT INTO books (title, release_year, author_id ) 
        VALUES ( %s, %s, %s ) 
        RETURNING *
    """
    values = [
        book.title, 
        book.release_year,
        book.author.id #this is the id column frm the author table, in the book table
        ]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book



#SELECT_ALL
def select_all():  
    books = [] 

    sql = "SELECT * FROM books"
    results = run_sql(sql)

    for row in results:
        author = author_repository.select(row['author_id'])
        book = Book(
            row['title'], 
            row['release_year'], 
            author,
            row['id']
            )
        books.append(book)
    return books 



#SELECT
def select(id):
    book = None
    sql = """
        SELECT * FROM books 
        WHERE id = %s
    """ 
    values = [id] 
    result = run_sql(sql, values)[0]
    
    if result is not None:
        author = author_repository.select(result['author_id']) 
        book = Book(
            result['title'], 
            result['release_year'], 
            author,
            result['id']
            )
    return book



#DELETE ALL
def delete_all():
    sql = "DELETE FROM books" 
    run_sql(sql)
    


#DELETE
def delete(id):
    sql = """
        DELETE FROM books 
        WHERE id = %s
    """ 
    values = [id]
    run_sql(sql, values)
    
    
    
#UPDATE 
def update(book):
    sql = """
        UPDATE books 
        SET (title, release_year, author_id) = (%s, %s, %s ) 
        WHERE id = %s
    """
    values = [
        book.title, 
        book.release_year, 
        book.author.id,
        book.id
        ]
    run_sql(sql, values) 

    