import unittest
import auto_m_2_py as m2py


class TestM2Py(unittest.TestCase):
    def test_get_pattern_semi_colon_followed_by_space(self):
        # test if pattern is correct
        pattern = m2py.get_pattern_semi_colon_followed_by_space()
        input_txt = '''figure(); plot(t,y1);  xlabel('Time (sec)');   ylabel('\theta (deg)');
'''
        result = pattern.findall(input_txt)
        expected = ['; ', ';  ', ';   ', ';\n']

        self.assertSequenceEqual(expected, result)

    def setUp(self):
        self.txt = '''%  Figure 3.6     Feedback Control of Dynamic Systems, 6e
%                        Franklin, Powell, Emami
% script to generate Fig. 3.6
%% fig3_06.m
% Satellite Pulse response Example. 3.19
clf;
numG=[0 0 0.0002];
denG=[1 0 0];
sysG=tf(numG,denG);
t=0:0.01:10;
%pulse input
u1=[zeros(1,500) 25*ones(1,10) zeros(1,491)];
[y1]=lsim(sysG,u1,t);
figure();
plot(t,u1);
xlabel('Time (sec)');
ylabel('Thrust Fc');
title('Fig. 3.6(a): Thrust input')
axis([0 10 0 26]);
% grid
nicegrid
pause;
% conversion to degrees
ff=180/pi;
y1=ff*y1;
figure(); plot(t,y1);xlabel('Time (sec)');
ylabel('\theta (deg)');
title('Fig. 3.6(b): Satellite attitude')
% grid
nicegrid

'''

    def tearDown(self):
        del self.txt

    def test_handle_semi_colon_followed_by_space_00(self):
        input_txt = '''figure(); plot(t,y1);xlabel('Time (sec)');
'''

        result = m2py.handle_semi_colon_followed_by_space(input_txt, '\n')
        expected = '''figure()
plot(t,y1)
xlabel('Time (sec)')
'''
        self.assertEqual(expected, result)

    def test_handle_semi_colon_followed_by_space_10(self):
        input_txt = '''num=[a];              # form numerator
den=[1 a];            # form denominator
t=0:0.01:4;           # form time vector
sys=tf(num,den);      # form system
h=impulse(sys,t);     # compute impulse response
figure();
plot(t,h);            # plot impulse response
y=step(sys,t);        # compute step response
'''

        result = m2py.handle_semi_colon_followed_by_space(input_txt, '\n')
        expected  = '''num=[a]               # form numerator
den=[1 a]             # form denominator
t=0:0.01:4            # form time vector
sys=tf(num,den)       # form system
h=impulse(sys,t)      # compute impulse response
figure()
plot(t,h)             # plot impulse response
y=step(sys,t)         # compute step response
'''
        self.assertEqual(expected, result)

    def test_insert_import(self):
        input_txt = '''#  Figure 3.14     Feedback Control of Dynamic Systems, 6e
#                        Franklin, Powell, Emami
#
#  fig3_14.m

pl.clf()
num=[2, 1]
den=[1, 3, 2]
'''
        result = m2py.insert_imports(input_txt)
        expected = '''#  Figure 3.14     Feedback Control of Dynamic Systems, 6e
#                        Franklin, Powell, Emami
#
#  fig3_14.m

import pylab as pl
import scipy.signal as ss

import control

pl.clf()
num=[2, 1]
den=[1, 3, 2]
'''
        self.assertEqual(expected, result)

    def test_m_filename_2_py_filename(self):
        m_filename = 'fig1_10b.m'
        result = m2py.m_filename_2_py_filename(m_filename)
        expected = 'fig1_10b.py'

        self.assertEqual(expected, result)

    def test_convert_matlab_2_python(self):
        maxDiff_backup = self.maxDiff
        self.maxDiff = None
        input_txt = '''%  Figure 3.4      Feedback Control of Dynamic Systems, 6e
%                        Franklin, Powell, Emami
% script to generate Fig. 3.4
%% fig3_04.m    Example 3.5
clf;
k=1;
num=1;                        % form numerator
den=[1 k];                    % form denominator
% sinusoidal input signal
deltaT = 0.001;
t=0:deltaT:10;                % form time vector
u=sin(10*(t));                % form input
sys=tf(num,den);              % form system
[y]=lsim(sys,u,t);            % linear simulation
% plot response
figure();
plot(t,y);
xlabel('Time (sec)');
ylabel('Output');
title('Fig. 3.4 (a): transient response');
pause;
hold on;
y1=(10/101)*exp(-t);
phi=atan(-10);
y2=(1/sqrt(101))*sin(10*t+phi);
plot(t,y1,t,y2,t,y1+y2);
% grid
nicegrid
hold off;
pause;
figure();
ii=[9001:10001];
plot(t(ii),y(ii),t(ii),u(ii));
xlabel('Time (sec)');
ylabel('Output, input');
title('Fig. 3.4 (b): Steady-state response');
text(9.4,0.65,'u(t)');
text(9.24,0.12,'y(t)');
% grid
nicegrid
'''
        result = m2py.convert_matlab_2_python(input_txt)
        expected = '''#  Figure 3.4      Feedback Control of Dynamic Systems, 6e
#                        Franklin, Powell, Emami
# script to generate Fig. 3.4
## fig3_04.m    Example 3.5
import pylab as pl
import scipy.signal as ss

import control


pl.clf()
k = 1
num = 1                                 # form numerator
den = [1, k]                            # form denominator
# sinusoidal input signal
deltaT = 0.001
t = pl.arange(0, 10+deltaT*0.5, deltaT) # form time vector
u = pl.sin(10*(t))                      # form input
sys = ss.TransferFunction(num,den)      # form system
t_out, y_out, x_out = ss.lsim(sys,u,t)  # linear simulation
# plot response
pl.figure();
pl.plot(t_out, y_out);
pl.xlabel('Time (sec)');
pl.ylabel('Output');
pl.title('Fig. 3.4 (a): transient response')
pl.show()

pl.hold(True)
y1 = (10/101) * pl.exp(-t);
phi = pl.arctan(-10);
y2 = (1/pl.sqrt(101))*pl.sin(10*t+phi);
pl.plot(t,y1,t,y2,t,y1+y2);
# grid
control.nicegrid()
pl.show()

pl.hold(False)
pl.figure()
ii = pl.arange(9001, 10001)
pl.plot(t_out[ii], y_out[ii],
        t[ii], u[ii])

pl.xlabel('Time (sec)')
pl.ylabel('Output, input')
pl.title('Fig. 3.4 (b): Steady-state response')
pl.text(9.4,0.65,'u(t)')
pl.text(9.24,0.12,'y(t)')
# grid
control.nicegrid()

pl.show()
'''
        self.assertEqual(expected, result)
        self.maxDiff = maxDiff_backup

    def test_space_equal_space(self):
        # test if pattern is correct
        pattern = m2py.get_pattern_space_equal_space()
        input_txt = '''num=[2 1]
den =[1 3 2]
t= 0:0.1:6
y = impulse(num,den,t)
'''
        result = pattern.findall(input_txt)
        expected = ['=', ' =', '= ', ' = ']

        self.assertEqual(expected, result)

    def test_handle_equal(self):
        input_txt = '''num=[2 1]
den =[1 3 2]
t= 0:0.1:6
y = impulse(num,den,t)
'''
        result = m2py.handle_equal(input_txt, '*=*=*')
        expected = '''num*=*=*[2 1]
den*=*=*[1 3 2]
t*=*=*0:0.1:6
y*=*=*impulse(num,den,t)
'''

        self.assertEqual(expected, result)

    def test_get_pattern_bracket_string(self):
        pattern = m2py.get_pattern_bracket_string()
        input_txt = '''1   2    3     [1 3  2]
den = [2 1]
'''
        result = pattern.findall(input_txt)
        expected = ['1 3  2', '2 1']
        self.assertSequenceEqual(expected, result)

    def test_replace_bracket_string(self):
        input_text = '''clf
num = [2 1]
den = [1 3 2]
t = 0:0.1:6
y = impulse(num,den,t)
'''
        result = m2py.find_bracket_string(input_text)
        expected = ((10, 15, '[2 1]'), (22, 29, '[1 3 2]'))
        self.assertSequenceEqual(expected, result)

    def test_get_pattern_space(self):
        input_txt = '[1 3  2]'
        pattern = m2py.get_pattern_space()
        result = pattern.findall(input_txt)
        expected = [' ', '  ']
        self.assertSequenceEqual(expected, result)

    def test_replace_space_with_comma(self):
        input_txt = '[1 3  2]'
        result = m2py.replace_space_with_comma(input_txt)
        expected = '[1,3,2]'
        self.assertEqual(expected, result)

    def test_replace_multicomma_to_comma(self):
        input_txt = '[1,,3,,,2]'
        result = m2py.replace_multicomma_to_comma(input_txt)
        expected = '[1,3,2]'
        self.assertEqual(expected, result)

    def test_convert_bracket_string_00(self):
        input_txt = '[2 1]'
        result = m2py.convert_bracket_string(input_txt)
        expected = '[2, 1]'
        self.assertEqual(expected, result)

    def test_convert_bracket_string_01(self):
        input_txt = '[1 2, 1]'
        result = m2py.convert_bracket_string(input_txt)
        expected = '[1, 2, 1]'
        self.assertEqual(expected, result)

    def test_process_bracket_string(self):
        input_txt = '''clf
num = [2 1]
den = [1 3,    2]
t = 0:0.1:6
y = impulse(num,den,t)
'''
        result = m2py.process_bracket_string(input_txt)
        expected = '''clf
num = [2, 1]
den = [1, 3, 2]
t = 0:0.1:6
y = impulse(num,den,t)
'''
        self.assertEqual(expected, result)
