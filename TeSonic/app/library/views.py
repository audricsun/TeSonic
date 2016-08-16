from flask import render_template, redirect, request, url_for, flash, jsonify, abort
from flask.ext.login import login_user, logout_user, login_required
from . import library
from ..models import Product,db
from .forms import ImportForm,NewProductForm


@library.route('/import', methods=['GET', 'POST'])
def importFile():
    form = ImportForm()
    if form.validate_on_submit():
        print form.title
        flash("importing file")
        flash(form.file.data)
        print form.file
    return render_template('library/import.html', form=form)


@library.route('/product_list', methods=['GET', 'POST'])
def productPage():
    from sqlalchemy.exc import IntegrityError
    if request.is_xhr:
        productName = request.form.get('name')
        print productName
        product = Product.query.filter_by(productName=productName).first()
        p = Product(productName=request.form.get('name'),
                    desc=request.form.get('desc'),
                    type=request.form.get('type'),
                    owner=request.form.get('owner'))
        db.session.add(p)
        try:
            db.session.commit()
            flash("Product is created")
            return jsonify({'message': 'success'})
        except IntegrityError:
            db.session.rollback()
            flash("Create Product Failed. Already Existed")
            return jsonify({'message': 'Already Existed'}),403

    products = Product.query.order_by(Product.ctime.desc()).all()
    return render_template('library/productListPage.html', products=products)

@library.route('/create_product', methods=['POST'])
def createProductByAjax():
    form = NewProductForm()
    print request.form.get('name')
    if form.validate_on_submit():
        flash("Form")
    elif request.is_xhr:
        flash("Have to do something")

    else:
        flash("nothing")
    return "success",200



@library.route('/productDetail/', methods=['GET', 'POST'])
def productDetail():
    productName = request.args.get('productName')
    product = Product.query.filter_by(productName=productName).first()
    if product is None:
        abort(404)
    return render_template('library/productDetailPage.html', product=product)


@library.route('/request', methods=['GET', 'POST'])
def requestPage():
    return render_template('library/requestListPage.html')


@library.route('/strategy', methods=['GET', 'POST'])
def strategyPage():
    return render_template('library/strategyListPage.html')


@library.route('/ajax')
def y():
    if request.is_xhr:
        return jsonify({'count': '5'})
    return render_template('library/ajax.html')


@library.route('/bootstrap')
def bootstrapDemo():
    return render_template('library/bootstrap.html')
