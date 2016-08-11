from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField ,TextAreaField,FileField
from wtforms.validators import Required, Length, Email,Regexp

class ImportForm(Form):
    title = StringField('Test Case Title', validators=[Required(), Length(1, 64)])
    description = TextAreaField('a simple test case')
    file = FileField('')
    enable = BooleanField('Publish After Import')
    submit = SubmitField('Import')
