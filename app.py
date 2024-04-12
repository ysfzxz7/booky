from flask import Flask, render_template # type: ignore
import requests # type: ignore
import json
app = Flask(__name__)

@app.route('/')
def home():
    # Homepage - Display a welcome message or featured books
    return render_template('index.html')

@app.route('/books')
def all_books():
    # Display all books available on the website
    url = "http://127.0.0.2:5000/api/books"
    res = requests.get(url)
    if res.status_code == 200:
        books = res.json()
    else:
        books = "Eroor"
    return render_template('books.html', books = books)

@app.route('/books/<int:book_id>')
def book_details(book_id):
    # Display details of a specific book based on its ID
    return render_template('book_details.html', book_id=book_id)

@app.route('/authors')
def all_authors():
    
    writers =  [
        {
        "id": "1",
        "name": "John Doe",
        "age": "35",
        "nationality": "American",
        "genre": ["Mystery", "Thriller"],
        "awards": ["Best Mystery Novel 2020", "Thriller Writer of the Year 2018"],
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQfl1KISFTuTCjxvA5agScS7B2I912I0I2yzgS65qJQyw&s"
        },
        {
        "id": "2",
        "name": "Emma Smith",
        "age": "42",
        "nationality": "British",
        "genre": ["Romance", "Historical Fiction"],
        "awards": ["Best Romance Novel 2019", "Historical Fiction Writer of the Year 2021"],
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQfl1KISFTuTCjxvA5agScS7B2I912I0I2yzgS65qJQyw&s"
        },
        {
        "id": "3",
        "name": "Carlos Hernandez",
        "age": "29",
        "nationality": "Mexican",
        "genre": ["Science Fiction", "Fantasy"],
        "awards": ["Best Science Fiction Novel 2022", "Fantasy Writer of the Year 2023"],
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQfl1KISFTuTCjxvA5agScS7B2I912I0I2yzgS65qJQyw&s"
        },
        {
        "id": "4",
        "name": "Sophie Martin",
        "age": "38",
        "nationality": "French",
        "genre": ["Contemporary", "Drama"],
        "awards": ["Best Contemporary Novel 2017", "Drama Writer of the Year 2019"],
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQfl1KISFTuTCjxvA5agScS7B2I912I0I2yzgS65qJQyw&s"
        },
        {
        "id": "5",
        "name": "Hiroshi Tanaka",
        "age": "45",
        "nationality": "Japanese",
        "genre": ["Historical Fiction", "Mystery"],
        "awards": ["Best Historical Fiction Novel 2016", "Mystery Writer of the Year 2014"],
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQfl1KISFTuTCjxvA5agScS7B2I912I0I2yzgS65qJQyw&s"
        },
        {
        "id": "6",
        "name": "Luisa Rossi",
        "age": "31",
        "nationality": "Italian",
        "genre": ["Romance", "Drama"],
        "awards": ["Best Romance Novel 2023", "Drama Writer of the Year 2020"],
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQfl1KISFTuTCjxvA5agScS7B2I912I0I2yzgS65qJQyw&s"
        },
        {
        "id": "7",
        "name": "Michael Andersen",
        "age": "48",
        "nationality": "Danish",
        "genre": ["Thriller", "Crime"],
        "awards": ["Best Thriller Novel 2015", "Crime Writer of the Year 2013"],
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQfl1KISFTuTCjxvA5agScS7B2I912I0I2yzgS65qJQyw&s"
        },
        {
        "id": "8",
        "name": "Maria Garcia",
        "age": "37",
        "nationality": "Spanish",
        "genre": ["Fantasy", "Young Adult"],
        "awards": ["Best Fantasy Novel 2018", "Young Adult Writer of the Year 2022"],
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQfl1KISFTuTCjxvA5agScS7B2I912I0I2yzgS65qJQyw&s"
        },
        {
        "id": "9",
        "name": "Andreas Müller",
        "age": "41",
        "nationality": "German",
        "genre": ["Science Fiction", "Thriller"],
        "awards": ["Best Science Fiction Novel 2019", "Thriller Writer of the Year 2016"],
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQfl1KISFTuTCjxvA5agScS7B2I912I0I2yzgS65qJQyw&s"
        },
        {
        "id": "10",
        "name": "Catherine Leblanc",
        "age": "33",
        "nationality": "Canadian",
        "genre": ["Mystery", "Historical Fiction"],
        "awards": ["Best Mystery Novel 2021", "Historical Fiction Writer of the Year 2017"],
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQfl1KISFTuTCjxvA5agScS7B2I912I0I2yzgS65qJQyw&s"
        }
    ]
    # Display all authors
    
    return render_template('authors.html',authors = writers)

@app.route('/authors/<int:author_id>')
def author_details(author_id):
    au = {
        "id": "1",
        "name" : "jhon Doe",
        "age" : "15/02/2002",
        "nationality": "Moroccan",
        "image": "http://exemple.com/img.png",
        "bio": """John Smith is an acclaimed contemporary writer known for his captivating storytelling and rich character development. Born and raised in a small town, John developed an early passion for literature and writing. He pursued his dreams and obtained a Bachelor's degree in Creative Writing from a prestigious university.
                With a unique blend of imagination and introspection, John's writing transports readers to vivid worlds, where they become deeply immersed in the lives and experiences of his characters. His works explore a wide range of genres, including mystery, romance, and science fiction, showcasing his versatility as a writer.
                John's writing style is characterized by meticulous attention to detail and a keen sense of atmosphere. Through his vivid descriptions and evocative prose, he paints a vivid picture that allows readers to feel as if they are right alongside the characters, experiencing their triumphs and struggles firsthand.
                In addition to his talent for storytelling, John is known for his thought-provoking themes and insightful social commentary. His works often delve into complex issues of identity, human relationships, and the human condition, making readers reflect on their own lives and the world around them.
                John's literary accomplishments have garnered critical acclaim, earning him several prestigious awards and nominations. His novels have topped bestseller lists and have been translated into multiple languages, captivating readers around the globe.
                When he's not engrossed in the world of writing, John enjoys traveling, exploring new cultures, and drawing inspiration from the diverse experiences he encounters. He is an avid reader and believes that continuous learning and exploration are essential for nurturing creativity.
                With his unwavering passion for storytelling, John Smith continues to enchant readers with his captivating narratives, leaving a lasting impact on the literary world.""",
        "genre": ["horror","fiction", "kids", "games","sport"]
    }

    # Display details of a specific author based on their ID
    return render_template('author_details.html',  authors = au)

if __name__ == '__main__':
    app.run(debug=True)