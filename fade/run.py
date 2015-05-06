from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    l_user = 'admin'
    l_message = 'Welcome!'
    return render_template('index.tpl', p_user = l_user, p_message = l_message)

if __name__ == '__main__':
    app.run()
