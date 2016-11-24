from flask import flash, redirect, render_template, request, url_for, Blueprint
from forms import LoginForm, SignupForm
from app import db
from app.models import User, bcrypt
from flask_login import login_user, login_required, logout_user, current_user


# Config
auth_blueprint = Blueprint(
    'auth', __name__,
    template_folder='templates'
    )


###### ROUTES ######
# Route for handling the login page logic
@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            email = form.email.data
            password = form.password.data

            user = User.query.filter_by(email=email).first()
            if user is not None and bcrypt.check_password_hash(user.password, request.form['password']):
                login_user(user)
                return redirect(url_for('store.overview'))
            else:
                error = 'Invalid credentials. Please try again.'
    return render_template('login.html', form=form, error=error)


@auth_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@auth_blueprint.route('/signup', methods=['GET', 'POST'])
def signup():
    error = None
    form = SignupForm()
    if request.method == "POST":
        if form.validate_on_submit():
            user = User(
                fname=form.fname.data,
                lname=form.lname.data,
                email=form.email.data,
                username=form.username.data,
                password=form.password.data
            )
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.login'))
        else:
            error = 'Invalid credentials. Please try again.'
    return render_template('signup.html', form=form)
