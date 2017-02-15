import re
import sys
import os


def get_pattern_semi_colon_followed_by_space_comment():
    return re.compile(r';\s*#')


def get_pattern_semi_colon_followed_by_space():
    return re.compile(r';\s*')


def handle_semi_colon(stage_00):
    stage_10 = stage_00.replace(';', '#;\n')
    stage_20 = stage_10.replace('#;\n\n', '#;\n')
    stage_30 = stage_20.replace('#;\n\n', '#;\n')
    stage_40 = stage_30.replace('#;', '')
    return stage_40


def handle_semi_colon_followed_by_space(txt, new_text='#;\n'):
    pattern = get_pattern_semi_colon_followed_by_space()
    replaced, count = pattern.subn (new_text, txt)
    return replaced


def get_pattern_space_equal_space():
    return re.compile(r'\s*=\s*')


def replace_txt_pattern_new(txt, pattern, new_text):
    replaced, count = pattern.subn(new_text, txt)
    return replaced


def handle_equal(txt, new_text=' = '):
    pattern = get_pattern_space_equal_space()
    return replace_txt_pattern_new(txt, pattern, new_text)


def get_pattern_bracket_string():
    return re.compile(r'\[(.+)?\]')
#    return re.compile(r'\[[a-zA-Z0-9_]+(\s+)\]')


def find_bracket_string(txt):
    pattern = get_pattern_bracket_string()
    result = []
    for match in pattern.finditer(txt):
        result.append((match.start(), match.end(), match.group()))

    return tuple(result)


def get_pattern_space():
    return re.compile('\s+')


def replace_space_with_comma(txt, new_text=','):
    pattern = get_pattern_space()
    return replace_txt_pattern_new(txt, pattern, new_text=new_text)


def replace_multicomma_to_comma(txt):
    return re.subn(',+', ',', txt)[0]


def convert_bracket_string(br_txt_br):
    br_space_to_comma_br = replace_space_with_comma(br_txt_br)
    br_multicomma_to_comma_br = replace_multicomma_to_comma(br_space_to_comma_br)
    br_comma_space_br = br_multicomma_to_comma_br.replace(',', ', ')
    return br_comma_space_br


def process_bracket_string(txt):
    start_end_text_tuple = find_bracket_string(txt)
    i_from = 0
    new_text = ''
    for i_start, i_end, text in start_end_text_tuple:
        new_text += txt[i_from:i_start]
        br_comma_br = convert_bracket_string(text)
        new_text += br_comma_br
        i_from = i_end
    new_text += txt[i_from:]

    return new_text


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


def read_txt(filename):
    with open(filename, 'r') as f:
        txt = f.read()
        f.close()
    return txt


def write_txt(filename, txt):
    with open(filename, 'w') as f:
        f.write(txt)
        f.close()


def m_filename_2_py_filename(m_filename, new_extension='.py'):
    split_filename_tuple = os.path.splitext(m_filename)
    new_filename = ''.join(split_filename_tuple[:-1] + (new_extension,))

    return new_filename


def convert_matlab_2_python(matlab_script):
    txt_comment = matlab_script.replace('%', '#')
    txt_newline = handle_semi_colon_followed_by_space(txt_comment, '\n')
    txt_insert_import = insert_imports(txt_newline)
    txt_equal = handle_equal(txt_insert_import)
    txt_list = process_bracket_string(txt_equal)

    return txt_list


def convert_m_2_py(m_filename):
    matlab_script = read_txt(m_filename)
    python_script = convert_matlab_2_python(matlab_script)
    write_txt(m_filename_2_py_filename(m_filename), python_script)


def main(argv):
    if 1 < len(argv):
        convert_m_2_py(argv[1])


if __name__ == '__main__':
    main(sys.argv)
