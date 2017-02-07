""" Fig. 2.3  Feedback Control of Dynamic Systems, 6e
             Franklin, Powell, Emami
"""
import pylab as pl
import scipy.signal as ss

# clear all;
# close all;
pl.close('all')
# clf
pl.clf()
# hold off
pl.hold(False)
# num = 1/1000;
num = 1.0 / 1000
# den = [1 50/1000];
den = [1, 50 / 1000]
# sys = tf(num,den);
sys = ss.TransferFunction(num, den)
# t = 0:100;
t = pl.arange(0, 100 + 1)
# y = step(num*500,den,t);
tout, yout = ss.step(sys, T=t)
# plot(t,y),grid
pl.plot(tout, yout)
pl.grid(True)
# xlabel('Time (sec)')
pl.xlabel('Time (sec)')
# ylabel('Amplitude')
pl.ylabel('Amplitude')
# title('Fig. 2.3')
pl.title('Fig. 2.3')
# nicegrid

pl.show()
