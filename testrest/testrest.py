#!/usr/bin/env python
"""
    testrest: A simple script to test the communication with
    a rest api.

    Usage:
        testrest <url-with-parms>
"""
from docopt import docopt
import requests, json

__version__ = 'v1.0'

import sys

def test_url(a_url):
    """
        Function to retreive a response and print it.
    """
    r = requests.post(a_url)
    print("Rest api server data:", r.headers)
    print("Data returned by api:", r.text)
    print("Url from data:", r.url)
    print("Encoding:", r.encoding)
    print("Status-code:", r.status_code)


if __name__ == "__main__":
    args = docopt(__doc__, help=True, version=__version__)

    if args['<url-with-parms>']:
        print("Url entered:", args['<url-with-parms>'].strip())
        test_url(args['<url-with-parms>'].strip())
        
