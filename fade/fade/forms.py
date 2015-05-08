from flask.ext.wtf import Form
from wtforms import IntegerField
from wtforms.validators import DataRequired

class FormLeveragedContracts(Form):
    l_contracts = IntegerField('contracts', validators=[DataRequired()], default=1)
