#!/usr/bin/env python
"""
    Usage:
        ledgerplot [options]
    
    Options:
        --income_vs_expenses ledgerfile [<year>|<start date> <end date> [total]]
        -V, --version
        --python
"""

"""
See LICENSE.txt file for copyright and license details.
"""

from docopt import docopt
import sys


__all__ = ['ledgerplot']
__version__ = 'v0.1'

def main():
    print "-main()-"
    pass
    
if __name__ == "__main__":
    args = docopt(__doc__, help=True, version=__version__)
    if args['--export'] == Export.LEDGER:
        export_type = Export.LEDGER
    elif args['--export'] == Export.CSV:
        export_type = Export.CSV
    else:
        print "Error: wrong export type (" + \
            args['--export'] + \
        "), falling back on the default (" + \
        Export.CSV + \
        ")!"
        export_type = Export.CSV
    elif args['--python']:
    print 'Python', sys.version
    sys.exit(0)
    main()
