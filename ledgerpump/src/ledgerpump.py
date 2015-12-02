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

#__all__ = ['ledgerpump']
__version__ = 'v0.1'


def adjust_system_path():
    """
        Adjust the system path, so we can search in custom dirs for modules.
    """
    sys.path.append('modules')
    
if __name__ == "__main__":
    adjust_system_path()
    args = docopt(__doc__, help=True, version=__version__)
