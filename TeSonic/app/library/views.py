from flask import render_template, redirect, request, url_for, flash, jsonify, abort
from flask.ext.login import login_user, logout_user, login_required
from . import library
from ..models import Product
from .forms import ImportForm,NewProduct


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
    products = Product.query.order_by(Product.ctime.desc()).all()
    form = NewProduct()
    return render_template('library/productListPage.html', products=products,form = form)


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
