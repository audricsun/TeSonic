from flask import render_template, redirect, request, url_for, flash ,jsonify
from flask.ext.login import login_user, logout_user, login_required
from . import manager
from ..models import User
from .forms import ImportForm


@manager.route('/import',methods=['GET', 'POST'])
def importFile():
    form = ImportForm()
    if form.validate_on_submit():
        flash("importing file")
        flash(form.file.data)
        print form.file
    return render_template('manager/import.html', form=form)


@manager.route('/ajax')
def y():
   if request.is_xhr:
       return jsonify({'count':'5'})
   return render_template('manager/ajax.html')


@manager.route('/bootstrap')
def bootstrapDemo():
   return render_template('manager/bootstrap.html')