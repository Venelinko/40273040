from flask import render_template, flash, redirect, url_for, request
from app import main, db
from app.forms import LoginForm, RegistrationForm, NewLogForm, EditProfileForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Log
from werkzeug.urls import url_parse
from sqlalchemy import desc

@main.route('/')
@main.route('/index')
def index():
    articles = [
        {
            'author': "David",
            'title': "Artiicle Title",
            'body': "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras magna felis, ullamcorper at lobortis eu, congue non mi. "
        },
        {
            'author': {'username': 'Michael'},
            'content': 'Second post'
        }
    ]
    return render_template('index.html', title='Home', articles=articles)

@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    formIn = LoginForm()
    if formIn.validate_on_submit():
        user = User.query.filter_by(username=formIn.username.data).first()

        if user is None or not user.check_password(formIn.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))

        login_user(user, remember=formIn.remember_me.data)

        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=formIn)

@main.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@main.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@main.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    logs = Log.query.filter_by(logauthor=user)
    return render_template('user.html', user=user, logs=logs)

@main.route('/logbook')
def logbook():
    if current_user.is_anonymous:
        return redirect(url_for('login'))
    user = current_user
    logs = Log.query.order_by(desc(Log.timestamp)).all()
    return render_template('logbook.html', logs=logs, user=user)

@main.route('/newlog', methods=['GET', 'POST'])
@login_required
def newlog():
    form = NewLogForm()
    if form.validate_on_submit():
        log = Log(destination=form.destination.data, difficulty=form.difficulty.data,
        body=form.body.data, logauthor=current_user)
        db.session.add(log)
        db.session.commit()
        flash('New log created.')
        return redirect(url_for('logbook'))
    return render_template('newlog.html', title='New log', form=form)

@main.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def editprofile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.username.data
        db.session.commit()
        flash('Profile succesfully updated')
        return redirect(url_for('user'))
    elif request.method == 'GET':
            form.username.data = current_user.username
            form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', form=form)