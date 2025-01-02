from source.app.__init__ import create_app
from source.app.config import db
from source.app.models.authors import Author
from source.app.models.books import Book

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)