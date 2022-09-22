from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

app = Flask(__name__)

app.config["SECRET_KEY"] = "example"
app.config["SQLALCHEMY_DATABASE_URI"] = "db:3306"
db = SQLAlchemy(app)

def testdb():
    try:
        db.session.query(text('1')).from_statement(text('SELECT 1')).all()
    except Exception as e:
        print('here')
        print(e)

testdb()