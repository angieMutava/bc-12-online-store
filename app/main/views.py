from flask import flash, redirect, render_template, request, url_for, Blueprint
from flask_login import login_user, login_required, logout_user, current_user
from flask import render_template, Blueprint


# Config

main_blueprint = Blueprint(
    'main', __name__,
    template_folder='templates'
)


# Routes
@main_blueprint.route('/', methods=['GET'])
def index():
    """
    Landing page when app url is keyed in browser
    """
    return render_template('index.html')


@main_blueprint.route('/overview', methods=['GET'])
@login_required
def overview():
    """
    Landing page when user logs in
    """
    return render_template('overview.html')
