from flask import Flask, jsonify

app = Flask(__name__)


books = [
    {
        'id': 1,
        'title': 'Domain-Driven Design: Tackling Complexity in the Heart of Software',
        'author': 'Eric Evans',
        'cover': 'Hardcover'
    },
    {
        'id': 2,
        'title': 'Gödel, Escher, Bach: An Eternal Golden Braid',
        'author': 'Douglas Hofstadter',
        'cover': 'Paperback'
    },
    {
        'id': 3,
        'title': 'Thinking in Systems',
        'author': 'Donella H. Meadows',
        'cover': 'Paperback'
    }
]


@app.route('/library/api/v1.0/books')
def get_books():
    return jsonify({'books': books})


if __name__ == '__main__':
    app.run(debug=True)