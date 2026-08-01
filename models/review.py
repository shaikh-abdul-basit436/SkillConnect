from models.user import db

class Review(db.Model):

    __tablename__ = "reviews"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    reviewer_id = db.Column(
        db.Integer,
        nullable=False
    )

    reviewed_user_id = db.Column(
        db.Integer,
        nullable=False
    )

    rating = db.Column(
        db.Integer,
        nullable=False
    )

    comment = db.Column(
        db.Text
    )