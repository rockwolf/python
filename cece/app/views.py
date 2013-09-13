"""
See LICENSE file for copyright and license details.
"""

from app import app
from flask import render_template, flash, redirect
#from app.forms import LoginForm

from app.modules.constant import *

@app.route("/")
@app.route("/index")
@app.route("/index/")
@app.route("/<app_profile>/index")
@app.route("/<app_profile>/index/")
@app.route("/<app_profile>")
@app.route("/<app_profile>/")
def index(app_profile = AppProfile.PERSONAL):
    """
        Index page
    """
    user = { 'login': 'rockwolf' } # fake user
    if app_profile == '':
        app_profile = 'personal'
    return render_template("index.html",
        title = 'Central command entity',
        user = user,
        app_profile = app_profile.lower())

@app.route("/report_finance")
@app.route("/report_finance/")
@app.route("/<app_profile>/report_finance")
@app.route("/<app_profile>/report_finance/")
def report_finance(app_profile = AppProfile.PERSONAL):
    """
        Financial reports.
    """
    # Make reports per year in pdf (gnucash) and put links to them here.
    return('TBD');

@app.route("/trading_journal")
@app.route("/trading_journal/")
@app.route("/<app_profile>/trading_journal")
@app.route("/<app_profile>/trading_journal/")
def trading_journal(app_profile = AppProfile.PERSONAL):
    """
        Trading Journal
    """
    if app_profile == AppProfile.ZIVLE:
        return render_template("trading_journal.html",
            title = 'Trading Journal',
            user = user,
            app_profile = app_profile.lower())
    else:
        return render_template("404.html",
                title = '404')

@app.route("/contact")
@app.route("/contact/")
@app.route("/<app_profile>/contact")
@app.route("/<app_profile>/contact/")
def contact(app_profile = AppProfile.PERSONAL):
    """
       Address book. 
    """
    # Try to sync this with abook? Can abook export them?
    return('TBD');

@app.route("/task")
@app.route("/task/")
@app.route("/<app_profile>/task")
@app.route("/<app_profile>/task/")
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
            app_profile = app_profile.lower(),
            tasks = load_lines(task_file),
            reminders = load_lines(reminder_file)
            )
    else:
        return render_template("404.html",
                title = '404')

@app.route('/login', methods = ['GET', 'POST'])
@app.route('/login/', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', 
        title = 'Sign In',
        form = form)

@app.route("/links")
@app.route("/links/")
@app.route("/<app_profile>/links")
@app.route("/<app_profile>/links/")
def links(app_profile = AppProfile.PERSONAL):
    """
       Link bookmarks.
    """
    user = { 'login': 'rockwolf' } # fake user
    # Try to read from text-files and build links dynamically
    # Format: data/<profile>/links.txt
    # Textfile format: <url>;<name>;<description>
    #TODO: put links_file in constant.py
    #or find a more general way to configure files?
    #links_file = 'C:\\Users\\AN\\home\\other\\Dropbox\\cece\\app\\data\\' + app_profile + '\\links.txt'
    links_file = '/home/rockwolf/Dropbox/cece/app/data/' + app_profile + '/links.txt'
    links_full = load_lines(links_file)
    links = []
    for link_full in links_full:
        links.append(link_full.split(';'))
    links.sort(key=lambda k: k[1])
    categories = []
    for link in links:
        if link[1] not in categories:
            categories.append(link[1])
    return render_template("links.html",
        title = 'Bookmarks',
        user = user,
        app_profile = app_profile.lower(),
        categories = categories,
        total = len(links),
        links = links
        )

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html',
	title = '404'), 404

def load_lines(text_file):
    """
        Reads the text file and returns a list of lines.
    """
    lines = []
    with open(text_file, encoding='utf-8') as text:
        for line in text:
            lines.append(line.strip())
    return lines
