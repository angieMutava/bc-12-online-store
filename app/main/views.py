# Imports
from flask import render_template, request, Blueprint
from flask_login import current_user


# Config
main_blueprint = Blueprint(
    'main', __name__,
    template_folder='templates'
)


@main_blueprint.route('/', methods=['GET'])
def index():
    """
    Landing page when app url is keyed in browser
    """
    return render_template('index.html')


@main_blueprint.errorhandler(403)
def not_allowed(e):
    return render_template('403.html'), 403


@main_blueprint.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@main_blueprint.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500
