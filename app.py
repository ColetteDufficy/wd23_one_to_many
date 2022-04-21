from flask import Flask, render_template
from controllers.books_controller import books_blueprint

app = Flask(__name__)

app.register_blueprint(books_blueprint)
#blueprint is a place to store lots of routes. ie @app.routes

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)