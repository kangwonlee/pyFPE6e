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

    h_axes = pl.gca() #pl.findobj(pl.get(pl.gcf(), 'Children'), 'Type', 'axes')
    grey = [0.7, 0.7, 0.7]
    pl.set(h_axes,
           'xcolor', grey,
           'ycolor', grey,
           'GridLineStyle', '-',
           'MinorGridLineStyle', '-',
           'Units', 'pixels')
    pl.grid(True)

    '''
    c11 = copyobj(h_axes, pl.gcf())
    pl.set(c11,
           'color', 'none',
           'xcolor', 'k',
           'xgrid', 'off',
           'ycolor', 'k',
           'ygrid', 'off')'''
