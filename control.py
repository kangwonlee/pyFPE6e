import pylab as pl
import scipy.signal as ss


def bode(system, freq_rad_list, n=10000):
    """

    :param an instance of the lti class or a tuple describing the system. system:
    :param ndarray freq_rad_list:
    :param int n:
    :return:
    :rtype: Tuple(ndarray, ndarray)
    """

    freq_out_rad_list, resp_list = ss.freqresp(system, freq_rad_list, n=n)
    mag = pl.absolute(resp_list)
    phase_rad = pl.angle(resp_list, deg=1)

    return mag, phase_rad


def bodegrid():
    figure = pl.gcf()

    axes_list = figure.axes

    [axes.grid(True, which='both', ls='-', color='0.7') for axes in axes_list]


def nicegrid():
    pl.grid(True, ls='-', color='0.7')


def pzmap(num, den):
    # http://matplotlib.org/1.2.1/examples/pylab_examples/polar_demo.html
    zeros = pl.roots(num)
    poles = pl.roots(den)

    zeros_angle_rad = pl.angle(zeros)
    zeros_mag = pl.absolute(zeros)

    poles_angle_rad = pl.angle(poles)
    poles_mag = pl.absolute(poles)

    fig = pl.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8], polar=True)
    ax.plot(zeros_angle_rad, zeros_mag, 'o')
    ax.plot(poles_angle_rad, poles_mag, 'x')
    return ax
