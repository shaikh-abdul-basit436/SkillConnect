from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(UserMixin, db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    email = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    password = db.Column(
        db.String(255),
        nullable=False
    )

    department = db.Column(db.String(100))

    year = db.Column(db.String(20))

    bio = db.Column(db.Text)

    rating = db.Column(
        db.Float,
        default=0
    )

    role = db.Column(
        db.String(20),
        default="student"
    )