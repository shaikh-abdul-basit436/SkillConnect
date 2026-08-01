from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

from flask_login import login_required
from flask_login import current_user

from sqlalchemy import func

from models.user import db
from models.user import User
from models.skill import Skill
from models.student_skill import StudentSkill
from models.review import Review
from models.session import Session

profile_bp = Blueprint(
    "profile",
    __name__
)


@profile_bp.route("/profile")
@login_required
def profile():

    teach_skills = db.session.query(
        Skill
    ).join(
        StudentSkill,
        Skill.id == StudentSkill.skill_id
    ).filter(
        StudentSkill.user_id == current_user.id,
        StudentSkill.skill_type == "teach"
    ).all()

    learn_skills = db.session.query(
        Skill
    ).join(
        StudentSkill,
        Skill.id == StudentSkill.skill_id
    ).filter(
        StudentSkill.user_id == current_user.id,
        StudentSkill.skill_type == "learn"
    ).all()

    session_count = Session.query.filter(
        (Session.sender_id == current_user.id) |
        (Session.receiver_id == current_user.id)
    ).count()

    average_rating = db.session.query(
        func.avg(Review.rating)
    ).filter(
        Review.reviewed_user_id == current_user.id
    ).scalar()

    if average_rating is None:
        average_rating = 0

    recent_reviews = Review.query.filter_by(
        reviewed_user_id=current_user.id
    ).order_by(
        Review.id.desc()
    ).limit(5).all()

    return render_template(
        "profile.html",
        teach_skills=teach_skills,
        learn_skills=learn_skills,
        teach_count=len(teach_skills),
        learn_count=len(learn_skills),
        session_count=session_count,
        average_rating=round(average_rating, 1),
        recent_reviews=recent_reviews
    )


@profile_bp.route(
    "/profile/update",
    methods=["POST"]
)
@login_required
def update_profile():

    user = User.query.get(current_user.id)

    user.name = request.form["name"]
    user.department = request.form["department"]
    user.year = request.form["year"]
    user.bio = request.form["bio"]

    db.session.commit()

    return redirect(
        url_for("profile.profile")
    )