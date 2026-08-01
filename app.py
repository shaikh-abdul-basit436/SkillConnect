from flask import render_template
from flask_login import login_required
from flask_login import current_user
from flask import redirect
from flask import url_for
from models.student_skill import StudentSkill
from models.skill import Skill
from routes.match import match_bp
from routes.requests import requests_bp
from routes.sessions import sessions_bp
from routes.reviews import reviews_bp
from routes.profile import profile_bp

from flask import Flask
from flask_login import LoginManager

from models.user import db
from models.user import User

from routes.auth import auth_bp
from routes.skills import skills_bp

app = Flask(__name__)

app.config.from_object("config.Config")

db.init_app(app)

login_manager = LoginManager()

login_manager.init_app(app)

login_manager.login_view = "auth.login"


@login_manager.user_loader
def load_user(user_id):

    return User.query.get(
        int(user_id)
    )


app.register_blueprint(auth_bp)
app.register_blueprint(skills_bp)
app.register_blueprint(match_bp)
app.register_blueprint(requests_bp)
app.register_blueprint(
    sessions_bp
)
app.register_blueprint(
    reviews_bp
)
app.register_blueprint(profile_bp)

@app.route("/")
def home():

    return redirect(
        url_for("dashboard")
    )

from sqlalchemy import func
from models.learning_request import LearningRequest
from models.session import Session
from models.review import Review


@app.route("/dashboard")
@login_required
def dashboard():

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

    request_count = LearningRequest.query.filter(
        (LearningRequest.sender_id == current_user.id) |
        (LearningRequest.receiver_id == current_user.id)
    ).count()

    pending_requests = LearningRequest.query.filter(
        LearningRequest.receiver_id == current_user.id,
        LearningRequest.status == "Pending"
    ).count()

    session_count = Session.query.filter(
        (Session.sender_id == current_user.id) |
        (Session.receiver_id == current_user.id)
    ).count()

    avg_rating = db.session.query(
        func.avg(Review.rating)
    ).filter(
        Review.reviewed_user_id == current_user.id
    ).scalar()

    if avg_rating is None:
        avg_rating = 0

    recent_reviews = Review.query.filter_by(
        reviewed_user_id=current_user.id
    ).order_by(
        Review.id.desc()
    ).limit(5).all()

    return render_template(

        "dashboard.html",

        teach_skills=teach_skills,

        learn_skills=learn_skills,

        teach_count=len(teach_skills),

        learn_count=len(learn_skills),

        request_count=request_count,

        pending_requests=pending_requests,

        session_count=session_count,

        average_rating=round(avg_rating,1),

        recent_reviews=recent_reviews

    )

if __name__ == "__main__":

    with app.app_context():
        db.create_all()

    app.run(debug=True)