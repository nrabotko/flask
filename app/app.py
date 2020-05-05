from flask import render_template, flash, redirect, url_for
from flask_wtf import form

from app import app
from app.forms import LoginForm, RegisterForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'Юля'},
            'body': 'Что-то написано'
        },
        {
            'author': {'username': 'Игорь'},
            'body': 'Еще что-то написано'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/reg', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    return 'тут должна быть регистрация'


if __name__ == '__main__':
    app.run()
