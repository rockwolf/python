from flask import Flask, render_template, request
#from app import Views #TODO: move all the routes to views.py
from forms import FormLeveragedContracts
import sys

app = Flask(__name__)

@app.route('/')
@app.route('/home')
@app.route('/home/')
def render_home():
    """
        Renders the index page.
    """
    l_user = 'admin'
    l_message = 'Welcome!'
    return render_template('index.tpl', p_user = l_user, p_message = l_message)

@app.route('/leverage', methods = ['GET', 'POST'])
@app.route('/leverage/', methods = ['GET', 'POST'])
def render_leverage():
    """
        Renders the leverage page.
    """
    l_form = FormLeveragedContracts()
    #l_leveraged_contracts = request.form['txt_contracts']
    return render_template('leverage.tpl', p_form = l_form)
    #return render_template('leverage.tpl', p_leveraged_contracts = l_leveraged_contracts)

def adjust_system_path():
        """
            Adjust the system path, so we can search in custom dirs for modules.
        """
        sys.path.append('fade/')
        sys.path.append('fade/static/')
        sys.path.append('fade/static/img/')
        sys.path.append('fade/static/js/')
        sys.path.append('fade/static/css/')
        sys.path.append('fade/templates/')
        sys.path.append('instance/')
        
if __name__ == '__main__':
    adjust_system_path()
    app.run(debug=True)
