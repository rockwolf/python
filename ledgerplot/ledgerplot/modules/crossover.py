#!/usr/bin/env python
"""
    See LICENSE.txt file for copyright and license details.
"""


"""
    A plot that shows when break even is reached.
"""
import numpy as np
import matplotlib.pyplot as plt
from decimal import Decimal
import sys

x_array = []
y_array = []

def load_data():
    """
        Load data
    """
    var_data = open(sys.argv[1].strip(), 'r').read()
    var_data_array = var_data.split('\n')
    i = 0
    for line in var_data_array:
        i += 1
        # skip the last 2 lines of the output
        if (len(line)>1) and (i<len(var_data_array) - 2):
            x_array.append(abs(float(line.strip().split(' ')[0].strip())))
            y_array.append(i)

