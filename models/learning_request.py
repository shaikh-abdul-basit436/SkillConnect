from models.user import db


class LearningRequest(db.Model):

    __tablename__ = "learning_requests"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    sender_id = db.Column(
        db.Integer,
        nullable=False
    )

    receiver_id = db.Column(
        db.Integer,
        nullable=False
    )

    status = db.Column(
        db.String(20),
        default="Pending"
    )