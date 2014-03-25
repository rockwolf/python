#!/usr/env/python
"""
    See LICENSE file for copyright and license details.
"""
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from decimal import Decimal

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

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

    ax1.clear()
    ax1.plot(x_array, y_array)

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
