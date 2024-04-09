from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_mysqldb import MySQL
import random 

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'  # MySQL host
app.config['MYSQL_USER'] = 'root'  # MySQL username
app.config['MYSQL_PASSWORD'] = 'toor'  # MySQL password
app.config['MYSQL_DB'] = 'library'  # MySQL database name


mysql = MySQL(app)

@app.route('/api/books')
def books():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM books")
    result = cur.fetchall()
    cur.close()
    return jsonify(result)    

@app.route('/api/book/<int:book_id>')
def book(book_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM books WHERE id = %s", (book_id,))
    result = cur.fetchall()
    cur.close()
    return str(result)

@app.route('/add_book', methods=['POST'])
def add_book():
    name = request.form['title']
    writer = request.form['author']
    date = request.form['date']
    link = request.form['link']
    download = 0
    likes = 0
    id = random.randint(2,9999999999)
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO books (id, name, date, link, likes, downloads, writer) VALUES (%s, %s, %s, %s, %s, %s, %s)", (id, name,date, link, likes, download, writer))
    mysql.connection.commit()
    cur.close()

@app.route('/delete_book/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM books WHERE id = %s", (book_id,))
    mysql.connection.commit()
    cur.close()

@app.route('/update_book/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    name = request.form['title']
    writer = request.form['author']
    
    cur = mysql.connection.cursor()
    cur.execute("UPDATE books SET name = %s, writer = %s WHERE id = %s", (name, writer, book_id))
    mysql.connection.commit()
    cur.close()


CORS(app)

if __name__ == "__main__":
    app.run(host='127.0.0.2', debug=True)
