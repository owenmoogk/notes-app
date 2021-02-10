# different pages for the authorization process
# login, logout, signup

from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint("auth", __name__)

@auth.route("/login", methods = ['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get('password')

        # finding the user
        user = User.query.filter_by(email = email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in successfully", category="success")
                login_user(user, remember=True)
                return(redirect(url_for('views.home')))
            else:
                flash("Incorrect password", category="error")
        else:
            flash("Email is not registered", category="error")

    return(render_template("login.html", user = current_user))

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return(redirect(url_for("auth.login")))

@auth.route("/sign-up", methods = ['GET', 'POST'])
def signUp():
    if request.method == "POST":
        email = request.form.get('email')
        firstName = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        # checking if the user exists
        user = User.query.filter_by(email = email).first()
        if user:
            flash("Email already registered", category="error")

        elif len(email) < 4:
            flash("Email must be greater than 3 characters", category="error")

        elif len(firstName) < 2:
            flash("First name must be greater than one character", category="error")

        elif password1 != password2:
            flash("Passwords do not match", category="error")

        elif len(password1) < 4:
            flash("Password must be at least 4 characters", category="error")

        else:
            newUser = User(email = email, firstName = firstName, password = generate_password_hash(password1, method='sha256'))
            db.session.add(newUser)
            db.session.commit()
            login_user(newUser, remember=True)

            flash("Account Created!", category="success")
            # redirects to home, putting a slash would also work, but is less dynamic than url for
            return(redirect(url_for('views.home')))



    return(render_template("signup.html", user = current_user))