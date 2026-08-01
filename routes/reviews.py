from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

from flask_login import login_required
from flask_login import current_user

from models.review import Review
from models.user import db

reviews_bp = Blueprint(
    "reviews",
    __name__
)

@reviews_bp.route(
    "/review/<int:user_id>",
    methods=["GET", "POST"]
)
@login_required
def review(user_id):

    if request.method == "POST":

        review_obj = Review(
            reviewer_id=current_user.id,
            reviewed_user_id=user_id,
            rating=int(
                request.form["rating"]
            ),
            comment=request.form["comment"]
        )

        db.session.add(review_obj)

        db.session.commit()

        return redirect(
            url_for("dashboard")
        )

    return render_template(
        "review.html"
    )