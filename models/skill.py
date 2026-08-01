from models.user import db


class Skill(db.Model):

    __tablename__ = "skills"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    category = db.Column(
        db.String(100),
        nullable=False
    )

    skill_name = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    description = db.Column(
        db.String(255)
    )

    icon = db.Column(
        db.String(100),
        default="fa-code"
    )