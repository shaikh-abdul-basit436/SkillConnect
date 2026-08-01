from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user

from models.learning_request import LearningRequest
from models.user import User, db
from models.student_skill import StudentSkill
from models.skill import Skill

match_bp = Blueprint(
    "match",
    __name__
)


@match_bp.route("/matches")
@login_required
def matches():

    matches = []

    current_learn = db.session.query(
        StudentSkill.skill_id
    ).filter(
        StudentSkill.user_id == current_user.id,
        StudentSkill.skill_type == "learn"
    ).all()

    current_learn = [x.skill_id for x in current_learn]

    users = User.query.filter(
        User.id != current_user.id
    ).all()

    for user in users:

        teach = db.session.query(
            Skill
        ).join(
            StudentSkill,
            Skill.id == StudentSkill.skill_id
        ).filter(
            StudentSkill.user_id == user.id,
            StudentSkill.skill_type == "teach"
        ).all()

        teach_ids = [s.id for s in teach]

        common = len(
            set(current_learn) &
            set(teach_ids)
        )

        if common == 0:
            continue

        percentage = round(
            (common / max(len(current_learn),1))*100
        )

        request = LearningRequest.query.filter_by(
            sender_id=current_user.id,
            receiver_id=user.id
        ).first()

        matches.append({

            "user":user,

            "percentage":percentage,

            "teach":teach,

            "status":request.status if request else None

        })

    matches.sort(
        key=lambda x:x["percentage"],
        reverse=True
    )

    return render_template(
        "matches.html",
        matches=matches
    )


@match_bp.route("/send_request/<int:user_id>")
@login_required
def send_request(user_id):

    check = LearningRequest.query.filter_by(
        sender_id=current_user.id,
        receiver_id=user_id
    ).first()

    if check:
        return redirect(
            url_for("match.matches")
        )

    db.session.add(

        LearningRequest(

            sender_id=current_user.id,

            receiver_id=user_id

        )

    )

    db.session.commit()

    return redirect(
        url_for("match.matches")
    )