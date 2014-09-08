from app import app, db, login_manager
from flask import render_template, flash, redirect, session, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from app.forms import LoginForm, RegistrationForm
from app.models import User, ROLE_ADMIN, ROLE_TUTOR, ROLE_USER


@app.route('/index')
def index():
    user = {'nickname': 'Chris'}
    return render_template("index.html", title = "Home", user = user)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        login_user(form.username)
        flash("Logged in successfully.")
        session['remember_me'] = form.remember_me.data

        return redirect(url_for('/index'))

    return render_template('login.html', title = 'Login', form = form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('/'))


@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User()
        form.populate_obj(user)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('/index'))
    return render_template('register.html', title = 'Register', form = form)


@app.route('/')
def home():
    return render_template("home.html", title = "Home")
