from flask import render_template, redirect, request, url_for, flash
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
    return render_template('manager/import.html', form=form)