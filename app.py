from flask import Flask
from flask_restful import reqparse, abort, Resource, Api
from http import HTTPStatus

app = Flask(__name__)
api = Api(app)

books = {
    '1': {
        'title': 'Domain-Driven Design: Tackling Complexity in the Heart of Software',
        'author': 'Eric Evans',
        'cover': 'Hardcover'
    },
    '2': {
        'title': 'Goedel, Escher, Bach: An Eternal Golden Braid',
        'author': 'Douglas Hofstadter',
        'cover': 'Paperback'
    },
    '3': {
        'title': 'Thinking in Systems',
        'author': 'Donella H. Meadows',
        'cover': 'Paperback'
    }
}


def abort_if_book_does_not_exist(book_id):
    if book_id not in books:
        abort(HTTPStatus.NOT_FOUND, message="Book {} does not exit".format(book_id))


parser = reqparse.RequestParser()
parser.add_argument('title', type=str, help='title of the book')
parser.add_argument('author', type=str, help='author of the book')
parser.add_argument('cover', type=str, help='cover type: Paperback / Hardcover')


class Book(Resource):
    def get(self, book_id):
        abort_if_book_does_not_exist(book_id)
        return {book_id: books[book_id]}

    def delete(self, book_id):
        abort_if_book_does_not_exist(book_id)
        del books[book_id]
        return '', HTTPStatus.NO_CONTENT

    def put(self, book_id):
        args = parser.parse_args(strict=True)
        book = {'title': args['title'],
                'author': args['author'],
                'cover': args['cover']}
        books[book_id] = book
        return book, HTTPStatus.CREATED


class BookList(Resource):
    def get(self):
        return books

    def post(self):
        args = parser.parse_args(strict=True)
        book = {'title': args['title'],
                'author': args['author'],
                'cover': args['cover']}
        todo_id = str(int(max(books.keys())) + 1)
        books[todo_id] = book
        return book, HTTPStatus.CREATED


api.add_resource(Book, '/library/api/v1.0/book/<string:book_id>')
api.add_resource(BookList, '/library/api/v1.0/books')

if __name__ == '__main__':
    app.run(debug=True)
