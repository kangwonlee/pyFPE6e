import scipy.signal as ss
import pylab as pl


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
