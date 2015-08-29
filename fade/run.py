#!/usr/bin/env python
"""
    See LICENSE.txt file for copyright and license details.
"""
from src import app
import sys

def adjust_system_path():
        """
            Adjust the system path, so we can search in custom dirs for modules.
        """
        sys.path.append('src/')
        sys.path.append('src/static/')
        sys.path.append('src/static/img/')
        sys.path.append('src/static/js/')
        sys.path.append('src/static/css/')
        sys.path.append('src/templates/')
        sys.path.append('src/views/')
        sys.path.append('instance/')


if __name__ == '__main__':
    adjust_system_path()
    app.run(debug=True)
