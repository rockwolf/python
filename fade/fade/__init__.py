from flask import Flask, render_template, request
#from app import Views #TODO: move all the routes to views.py
from forms import FormLeveragedContracts
import sys

app = Flask(__name__)
app.config.from_object('config')

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
    if l_form.validate_on_submit():
        return render_template('leverage.tpl', p_form = l_form, p_leveraged_contracts = l_leveraged_contracts)
    return render_template('leverage.tpl', p_form = l_form)

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

@app.before_request
def csrf_protect():
    if request.method == "POST":
        token = session.pop('_csrf_token', None)
        if not token or token != request.form.get('_csrf_token'):
            abort(403)

# TODO: create a random string function?
def generate_csrf_token():
    if '_csrf_token' not in session:
        session['_csrf_token'] = some_random_string()
    return session['_csrf_token']

if __name__ == '__main__':
    adjust_system_path()
    app.jinja_env.globals['csrf_token'] = generate_csrf_token
    app.run(debug=True)
