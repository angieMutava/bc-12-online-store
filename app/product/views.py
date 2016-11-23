from flask import flash, redirect, render_template, request, url_for, Blueprint
from forms import ProductForm
from app import db
from app.models import Store, Product, User
from flask_login import login_required, current_user


# Config
product_blueprint = Blueprint(
    'product', __name__,
    template_folder='templates'
)


###### ROUTES ######

# Add product route
@product_blueprint.route('/product/addproduct', methods=['GET', 'POST'])
@login_required
def product():
    "Creates a new product in a store"
    form = ProductForm()
    if request.method == "GET":
        return render_template('addproduct.html', form=form)
    elif request.method == "POST":
        if form.validate_on_submit():
            store = Store.query.filter_by(id=current_user.id).first()
            created_products = Product(product_name=form.product_name.data, product_description=form.product_desc.data, store_home=store.id, product_image=form.product_img.data)

            db.session.add(created_products)
            db.session.commit()
            flash("Product added successfully!")
            return redirect(url_for('store.overview'))

        store = Store.query.filter_by(id=current_user.id).first()
        display_product = store.store_product.all()
        all_products = 0
        for i in display_product:
            all_products += 1

        return render_template('addproduct.html', form=form, display_products=display_product, all_products=all_products)


@product_blueprint.route('/overview', methods=['GET', 'POST'])
@login_required
def overview():
    store = Store.query.filter_by(store_owner=current_user.id).first()
    display_product = store.store_product.all()

    all_products = 0
    for i in display_product:
        all_products += 1
    return render_template('viewstore.html', display_products=display_product, all_products=all_products)


# Custom store url route
@product_blueprint.route('/product/<username>/<int:storeid>', methods=['GET', 'POST']])
def store_url(username, storeid):
    user = User.query.filter_by(id=current_user.id)
    username = user.username
    store = Store.query.filter_by(store_owner=current_user).first()
    storeid = store.id
    with product.test_request_context():
        return render_template('overview.html', username=username, storeid=storeid)
