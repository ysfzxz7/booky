from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Homepage - Display a welcome message or featured books
    return render_template('index.html')

@app.route('/books')
def all_books():
    # Display all books available on the website
    return render_template('books.html')

@app.route('/books/<int:book_id>')
def book_details(book_id):
    # Display details of a specific book based on its ID
    return render_template('book_details.html', book_id=book_id)

@app.route('/authors')
def all_authors():
    # Display all authors
    return render_template('authors.html')

@app.route('/authors/<int:author_id>')
def author_details(author_id):
    # Display details of a specific author based on their ID
    return render_template('author_details.html', author_id=author_id)

if __name__ == '__main__':
    app.run(debug=True)