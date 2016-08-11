from flask import render_template, redirect, request, url_for, flash ,jsonify
from flask.ext.login import login_user, logout_user, login_required
from . import cycles
from ..models import User
from .forms import ImportForm


@cycles.route('/import',methods=['GET', 'POST'])
def importFile():
    form = ImportForm()
    if form.validate_on_submit():
        print form.title
        flash("importing file")
        flash(form.file.data)
        print form.file
    return render_template('manager/import.html', form=form)


@cycles.route('/ajax')
def y():
   if request.is_xhr:
       return jsonify({'count':'5'})
   return render_template('manager/ajax.html')


@cycles.route('/bootstrap')
def bootstrapDemo():
   return render_template('manager/bootstrap.html')