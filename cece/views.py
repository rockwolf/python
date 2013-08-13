"""
See LICENSE file for copyright and license details.
"""

from app import app
from flask import render_template, flash, redirect
#from forms import LoginForm
from app.modules.constant import *

@app.route("/")
@app.route("/index")
@app.route("/index/<app_profile>")
def index(app_profile = AppProfile.PERSONAL):
    """
        Index page
    """
    user = { 'login': 'rockwolf' } # fake user
    return render_template("index.html",
        title = 'Central command entity',
        user = user,
        app_profile = app_profile)

@app.route("/report_finance")
@app.route("/report_finance/<app_profile>")
def report_finance(app_profile = AppProfile.PERSONAL):
    """
        Financial reports.
    """
    # Make reports per year in pdf (gnucash) and put links to them here.
    return('TBD');

@app.route("/trading_journal")
@app.route("/trading_journal/<app_profile>")
def report_finance(app_profile = AppProfile.PERSONAL):
    """
        Trading Journal
    """
    if app_profile == AppProfile.ZIVLE:
        return render_template("trading_journal.html",
            title = 'Trading Journal',
            user = user,
            app_profile = app_profile)
    else:
        return render_template("404.html",
                title = '404')

@app.route("/contact")
@app.route("/contact/<app_profile>")
def contact(app_profile = AppProfile.PERSONAL):
    """
       Address book. 
    """
    # Try to sync this with abook? Can abook export them?
    return('TBD');

@app.route("/task")
@app.route("/task/<app_profile>")
def task(app_profile = AppProfile.PERSONAL):
    """
        Task and schedule information.
    """
    # TODO: generate output of reminders and put it in a new text-file,
    # e.g. remind ~/.reminders -c etc.
    # TODO: where to schedule the reminders.txt generation?
    if app_profile == AppProfile.ZIVLE:
        task_file = TaskFile.ZIVLE
        reminder_file = ReminderFile.ZIVLE
    elif app_profile == AppProfile.PERSONAL:
        task_file = TaskFile.PERSONAL
        reminder_file = ReminderFile.PERSONAL
    else:
        error = true

    if not error:
        return render_template("task.html",
            title = 'Tasks',
            user = user,
            app_profile = app_profile,
            tasks = load_lines(task_file),
            reminders = load_lines(reminder_file)
            )
    else:
        return render_template("404.html",
                title = '404')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', 
        title = 'Sign In',
        form = form)


def load_lines(text_file):
    """
        Reads the text file and returns a list of lines.
    """
    lines = []
    with open(text_file, encoding='utf-8') as text:
        for line in text:
            lines.append(line)
    return lines
