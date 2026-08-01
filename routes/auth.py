from flask_login import current_user
from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required

from werkzeug.security import check_password_hash
from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

from werkzeug.security import generate_password_hash

from models.user import User
from models.user import db

auth_bp = Blueprint(
    "auth",
    __name__
)


@auth_bp.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]

        password = generate_password_hash(
            request.form["password"]
        )

        user = User(
            name=name,
            email=email,
            password=password
        )

        db.session.add(user)
        db.session.commit()

        return redirect(
            url_for("auth.login")
        )

    return render_template(
        "register.html"
    )


@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(
            email=email
        ).first()

        if user and check_password_hash(
                user.password,
                password):

            login_user(user)

            return redirect(
                url_for("dashboard")
            )

    return render_template(
        "login.html"
    )


@auth_bp.route("/logout")
@login_required
def logout():

    logout_user()

    return redirect(
        url_for("auth.login")
    )