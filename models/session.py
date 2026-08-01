from models.user import db


class Session(db.Model):

    __tablename__ = "sessions"

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

    session_date = db.Column(
        db.Date
    )

    session_time = db.Column(
        db.String(20)
    )

    mode = db.Column(
        db.String(20)
    )

    status = db.Column(
        db.String(20),
        default="Scheduled"
    )