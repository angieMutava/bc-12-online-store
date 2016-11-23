from flask import flash, redirect, render_template, request, url_for, Blueprint
from forms import ProductForm
from app import db
from app.models import Store, Product, User
from flask_login import login_required, current_user


# Config
product_blueprint = Blueprint(
    'product', __name__
)


###### ROUTES ######


@product_blueprint.route('/overview/<int:id>', methods=['GET', 'POST'])
def overview(id):
    # store = Store.query.filter_by(store_owner=current_user.id).first()
    store = Store.query.get(id)
    display_product = Product.query.filter_by(store_home=store.id).all()  # store.store_product.all()
    all_products = len(display_product)

    return render_template('/product/overview.html', display_products=display_product, all_products=all_products)


# Custom store url route
# @product_blueprint.route('/product/<username>/<int:storeid>', methods=['GET', 'POST'])
# def store_url(store_username, storeid):
# user = User.query.filter_by(id=current_user.id)
# store_username = user.username
# store = Store.query.filter_by(store_owner=current_user).first()
# storeid = store.id
#  with product.test_request_context():
#  return render_template('/store/overview.html', store_username=store_username, storeid=storeid)


# Add product route
@product_blueprint.route('/product/addproduct', methods=['GET', 'POST'])
@login_required
def product():
    "Creates a new product in a store"
    form = ProductForm()
    if request.method == "GET":
        return render_template('product/addproduct.html', form=form)
    elif request.method == "POST":
        if form.validate_on_submit():
            store = Store.query.filter_by(store_owner=current_user.id).first()
            created_products = Product(product_name=form.product_name.data, product_description=form.product_desc.data, store_home=store.id, product_image=form.product_img.data)

            db.session.add(created_products)
            db.session.commit()
            flash("Product added successfully!")
            return redirect(url_for('product.overview', id=store.id))

        return render_template('product/overview.html')

        # display_product = Product.query.filter_by(store_home=store.id).all()
        # all_products = len(display_product)

        # return render_template('product/overview.html', display_products=display_product, all_products=all_products)
