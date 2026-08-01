from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import url_for

from flask_login import login_required
from flask_login import current_user

from models.learning_request import LearningRequest
from models.user import db

requests_bp = Blueprint(
    "requests",
    __name__
)


@requests_bp.route("/requests")
@login_required
def requests():

    all_requests = LearningRequest.query.filter_by(
        receiver_id=current_user.id
    ).all()

    return render_template(
        "requests.html",
        requests=all_requests
    )


@requests_bp.route("/accept/<int:req_id>")
@login_required
def accept_request(req_id):

    print("CURRENT USER =", current_user.id)
    req = LearningRequest.query.get(
        req_id
    )

    req.status = "Accepted"

    db.session.commit()

    return redirect(
        url_for("requests.requests")
    )


@requests_bp.route("/reject/<int:req_id>")
@login_required
def reject_request(req_id):

    req = LearningRequest.query.get(
        req_id
    )

    req.status = "Rejected"

    db.session.commit()

    return redirect(
        url_for("requests.requests")
    )