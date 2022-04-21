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




# DELETE
# DELETE '/books/<id>/delete'
@books_blueprint.route("/books/<id>/delete", methods=['POST'])
def delete_book(id):
    book_repository.delete(id)
    return redirect('/books')