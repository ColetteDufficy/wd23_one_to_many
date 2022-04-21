from flask import Flask, Blueprint, render_template, redirect, request
from repositories import book_repository
from repositories import author_repository
from models.book import Book


books_blueprint = Blueprint("books", __name__)

# RESTful CRUD Routes - 7 of them:
# 1. INDEX
# 2. NEW
# 3. CREATE
# 4. SHOW
# 5. EDIT
# 6. UPDATE
# 7. DELETE


# INDEX
# GET '/tasks'
@books_blueprint.route("/books")
def books():
    books = book_repository.select_all() #the way to access the DB is via the task_respoitory
    return render_template("books/index.html", all_books = books)



# NEW (NEW and CREATE are combined, because we need to create but we also need to post it back to the DB
# this is the first step. See CREATE for the second step)
# GET '/books/new'
#get a form to fill
@books_blueprint.route("/books/new", methods={'GET'})
def new_book():
    authors = author_repository.select_all()
    return render_template("/books/new.html", all_authors=authors)

    
    
# CREATE
# POST '/books'
# post the form to fill the database
@books_blueprint.route("/books", methods=['POST'])
def create_book():
    title = request.form['title']
    release_year = request.form['release_year']
    author_id = request.form['author_id']
    
    author = author_repository.select(author_id) # this line is accessing the DB to find the exact author, by using the id number. The Author variable needs to be defined first, before the python objevt is created. 
    book = Book(title, release_year, author) #this line is creating the object in python
    book_repository.save(book)
    return redirect('/books')





# DELETE
# DELETE '/books/<id>/delete'
@books_blueprint.route("/books/<id>/delete", methods=['POST'])
def delete_book(id):
    book_repository.delete(id)
    return redirect('/books')