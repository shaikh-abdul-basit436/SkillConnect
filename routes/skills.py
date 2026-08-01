from collections import defaultdict

from flask import Blueprint, render_template, request
from flask_login import login_required, current_user

from models.user import db
from models.skill import Skill
from models.student_skill import StudentSkill

skills_bp = Blueprint(
    "skills",
    __name__
)


@skills_bp.route("/skills", methods=["GET", "POST"])
@login_required
def skills():

    if request.method == "POST":

        StudentSkill.query.filter_by(
            user_id=current_user.id
        ).delete()

        teach = request.form.getlist("teach_skills")

        learn = request.form.getlist("learn_skills")

        for sid in teach:

            db.session.add(

                StudentSkill(

                    user_id=current_user.id,

                    skill_id=int(sid),

                    skill_type="teach"

                )

            )

        for sid in learn:

            db.session.add(

                StudentSkill(

                    user_id=current_user.id,

                    skill_id=int(sid),

                    skill_type="learn"

                )

            )

        db.session.commit()

    all_skills = Skill.query.order_by(

        Skill.category,

        Skill.skill_name

    ).all()

    grouped = defaultdict(list)

    for skill in all_skills:

        grouped[skill.category].append(skill)

    teach_ids = {

        s.skill_id

        for s in StudentSkill.query.filter_by(

            user_id=current_user.id,

            skill_type="teach"

        ).all()

    }

    learn_ids = {

        s.skill_id

        for s in StudentSkill.query.filter_by(

            user_id=current_user.id,

            skill_type="learn"

        ).all()

    }

    return render_template(

        "skills.html",

        grouped_skills=grouped,

        teach_ids=teach_ids,

        learn_ids=learn_ids

    )