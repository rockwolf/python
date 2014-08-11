#!/usr/bin/env python
"""
    Usage:
        ledgerplot [options]
    
    Options:
        --ledger <ledger file>
        --income_vs_expenses [<year>|<start date> <end date> [total]]
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
    print '-TEST- main()'
    
if __name__ == "__main__":
    args = docopt(__doc__, help=True, version=__version__)
    ledger_file = args['--ledger']
    print 'Using ledger file %s'.format(ledger_file)
    
    if args['--income_vs_expenses']:
        arglen = len(args['--income_vs_expenses'])
        print '-TEST- len(args[--income_vs_expenses]=%d'.format(arglen)
        if arglen > 1:
            if arglen = 3:
                # plot data for a specific period, giving the total.
                plot_income_vs_expenses_total()
            else:
                # plot data for a specific period
                plot_income_vs_expenses()
    elif args['--python']:
        print 'Python %s'.format(sys.version)
    sys.exit(0)
    main()
