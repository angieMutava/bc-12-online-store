from flask import flash, redirect, render_template, request, url_for, Blueprint
from forms import StoreForm
from app import db
from app.models import Store, User
from flask_login import login_required, current_user


# Config
store_blueprint = Blueprint(
    'store', __name__,
    template_folder='templates'
)


# Routes

@store_blueprint.route('/overview', methods=['GET'])
@login_required
def overview():
    """
    Landing page when user logs in

    Displays current_user's availbable stores if any
    """

    """user = User.query.filter_by(id=current_user.id).first()
    created_stores = user.store.all()
    all_stores = 0
    for i in created_stores:
        all_stores += 1

    return render_template('overview.html', store=created_stores, all_stores=all_stores)"""
    return render_template('overview.html')


@store_blueprint.route('/addstore', methods=['GET', 'POST'])
@login_required
def store():
    """
    Creates a new store
    """
    form = StoreForm()
    if form.validate_on_submit():
        user = User.query.filter_by(id=current_user.id).first()
        created_stores = Store(store_name=form.store_name.data, store_description=form.store_desc.data, store_image=form.store_img.data)

        user.store.append(created_stores)
        db.session.add(created_stores)
        db.session.commit()
        flash("Store added successfully!")

    user = User.query.filter_by(id=current_user.id).first()
    my_store = user.store.all()
    all_stores = 0
    for i in my_store:
        all_stores += 1

    return render_template('addstore.html', store=my_store, all_stores=all_stores)
