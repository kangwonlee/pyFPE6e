#  Figure 3.14     Feedback Control of Dynamic Systems, 6e
#                        Franklin, Powell, Emami
#
#  fig3_14.m

import pylab as pl

import control

pl.clf()
num=[2, 1]
den=[1, 3, 2]
pl.axis ('square')
ax = control.pzmap(num, den)
ax.grid(True)

pl.show()
