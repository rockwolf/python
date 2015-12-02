"""
    Usage:
        ledgerpump [options]
    
    Options:
        --file=<FILE>
        -V, --version
"""

"""
See LICENSE.txt file for copyright and license details.
"""

from docopt import docopt
from modules.pump import ledger_to_csv, csv_to_db

#__all__ = ['ledgerpump']
__version__ = 'v0.1'


def adjust_system_path():
    """
        Adjust the system path, so we can search in custom dirs for modules.
    """
    sys.path.append('modules')
    
if __name__ == "__main__":
    adjust_system_path()
    l_args = docopt(__doc__, help=True, version=__version__)
    
    l_file = ''
    if l_args['--file']:
        l_file = l_args['--file']
        print 'Using ledger file {}'.format(l_file)
        
    csv_to_db(ledger_to_csv(l_file))
    sys.exit(0)
