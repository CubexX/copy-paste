from flask import Flask

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder='../static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../db.sqlite'

EXP_TIME = 300

db = SQLAlchemy(app)

from .models.note import Note

db.create_all()

from .views import index


if __name__ == '__main__':
    app.run()
