from models.user import db


class StudentSkill(db.Model):

    __tablename__ = "student_skills"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        nullable=False
    )

    skill_id = db.Column(
        db.Integer,
        nullable=False
    )

    skill_type = db.Column(
        db.String(20),
        nullable=False
    )