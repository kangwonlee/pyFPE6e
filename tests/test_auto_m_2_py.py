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

        self.assertEqual(expected, result)

