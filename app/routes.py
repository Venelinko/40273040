from flask import render_template, flash, redirect, url_for
from app import main
from app.forms import LoginForm

@main.route('/')
@main.route('/index')
def index():
    user = {'username': 'Venelin'}
    posts = [
        {
            'author': {'username': 'Venelin'},
            'content': "New content"
        },
        {
            'author': {'username': 'Michael'},
            'content': 'Second post'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@main.route('/login', methods=['GET', 'POST'])
def login():
    formIn = LoginForm()
    if formIn.validate_on_submit():
        flash('Login request for use {}, remember_me={}'.format(formIn.username.data,
        formIn.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=formIn)