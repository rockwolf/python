#!/usr/bin/python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    """
        Index page
    """
    return('Command center')

@app.route("/report_finance")
def report_finance():
    """
        Financial reports.
    """
    return('TBD');

if __name__ == "__main__":
    app.debug = True
    app.run(port=9876)
