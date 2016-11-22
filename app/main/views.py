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
