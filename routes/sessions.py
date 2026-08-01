from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

from flask_login import login_required
from flask_login import current_user

from models.session import Session
from models.user import db

sessions_bp = Blueprint(
    "sessions",
    __name__
)


@sessions_bp.route(
    "/book_session/<int:user_id>",
    methods=["GET", "POST"]
)
@login_required
def book_session(user_id):

    if request.method == "POST":

        session = Session(

            sender_id=current_user.id,

            receiver_id=user_id,

            session_date=request.form[
                "session_date"
            ],

            session_time=request.form[
                "session_time"
            ],

            mode=request.form[
                "mode"
            ]
        )

        db.session.add(session)

        db.session.commit()

        return redirect(
            url_for("sessions.my_sessions")
        )

    return render_template(
        "book_session.html"
    )


@sessions_bp.route("/sessions")
@login_required
def my_sessions():

    sessions = Session.query.filter(
        (Session.sender_id == current_user.id)
        |
        (Session.receiver_id == current_user.id)
    ).all()

    return render_template(
        "sessions.html",
        sessions=sessions
    )