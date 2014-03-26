#!/usr/env/python
"""
    See LICENSE file for copyright and license details.
"""
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from decimal import Decimal


def animate(i):
    """
        Animate
    """
    print "test: "
    var_data = open('test.dat', 'r').read()
    var_data_array = var_data.split('\n')
    x_array = []
    y_array = []
    i = 0
    for line in var_data_array:
        i += 1
        print "test:", line
        # skip the last 2 lines of the output
        if (len(line)>1) and (i<len(var_data_array) - 2):
            x_array.append(Decimal(line.split(' ')[0]))
            y_array.append(i)


years = np.arange(2004, 2009)
heights = np.random.random(years.shape) * 7000 + 3000

box_colors = brewer2mpl.get_map('Set1', 'qualitative', 5).mpl_colors    

plt.bar(years - .4, heights, color=box_colors)
plt.grid(axis='y', color='white', linestyle='-', lw=1)
plt.yticks([2000, 4000, 6000, 8000])

fmt = plt.ScalarFormatter(useOffset=False)
plt.gca().xaxis.set_major_formatter(fmt)
plt.xlim(2003.5, 2008.5)
remove_border(left=False)

for x, y in zip(years, heights):
    plt.annotate("%i" % y, (x, y + 200), ha='center')

