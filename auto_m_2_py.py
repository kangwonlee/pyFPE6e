import re


def get_pattern_semi_colon_followed_by_space():
    return re.compile(r';\s+')


def handle_semi_colon(stage_00):
    stage_10 = stage_00.replace(';', '#;\n')
    stage_20 = stage_10.replace('#;\n\n', '#;\n')
    stage_30 = stage_20.replace('#;\n\n', '#;\n')
    stage_40 = stage_30.replace('#;', '')
    return stage_40


def handle_semi_colon_followed_by_space(txt):
    pattern = get_pattern_semi_colon_followed_by_space()
    replaced, count = pattern.subn ('#;\n', txt)
    return replaced


def insert_imports(txt):
    lines = txt.splitlines()
    import_string = '''import pylab as pl
import scipy.signal as ss

import control
'''

    # locate first line after header comment

    result_line = None
    for i, line in enumerate(lines):
        if line:
            if '#' != line[0]:
                result_line = i
                break

    if result_line is not None:
        lines.insert(result_line, import_string)

    result_txt = '\n'.join(lines)
    result_txt += '\n'
    return result_txt
