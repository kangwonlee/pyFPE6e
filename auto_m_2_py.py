import re
import sys
import os


def get_pattern_semi_colon_followed_by_space_comment():
    return re.compile(r';\s*#')


def get_pattern_semi_colon_followed_by_space():
    return re.compile(r';\s*')


def get_pattern_arange():
    return re.compile(r'(?P<start>[\d.\w]+):(?P<interval>[\d.\w]+):(?P<end>[\d.\w]+)')


def replace_to_arange(matlab_array_text, pattern=get_pattern_arange()):
    match = pattern.match(matlab_array_text)
    match_dict = match.groupdict()
    new_text = 'arange({start}, {end} + 0.5*({interval}), {interval})'.format(**match_dict)
    module_new_text = '%s.%s' % ('pl', new_text)
    return module_new_text


def process_to_arange(txt):
    pattern = get_pattern_arange()
    new_text = apply_replace_to_matches(txt, pattern, replace_to_arange)
    return new_text


def handle_semi_colon(stage_00):
    stage_10 = stage_00.replace(';', '#;\n')
    stage_20 = stage_10.replace('#;\n\n', '#;\n')
    stage_30 = stage_20.replace('#;\n\n', '#;\n')
    stage_40 = stage_30.replace('#;', '')
    return stage_40


def process_semi_colon_followed_by_space_comment(txt):
    pattern = get_pattern_semi_colon_followed_by_space_comment()

    def replace_function(txt):
        return txt.replace(';', ' ')

    new_text = apply_replace_to_matches(txt, pattern, replace_function)
    return new_text


def apply_replace_to_matches(txt, pattern, replace_function):
    """

    :param string txt: source code
    :param __Regex pattern: regular expression to find
    :param func replace_function: generate string to replace the pattern
    :return:
    """
    i_from = 0
    new_text = ''
    for match in pattern.finditer(txt):
        i_start, i_end, text = match.start(), match.end(), match.group()

        new_text += txt[i_from:i_start]
        br_comma_br = replace_function(text)
        new_text += br_comma_br
        i_from = i_end
    new_text += txt[i_from:]
    return new_text


def handle_semi_colon_followed_by_space(txt, new_text='#;\n'):
    comment_processed_text = process_semi_colon_followed_by_space_comment(txt)
    pattern = get_pattern_semi_colon_followed_by_space()
    replaced, count = pattern.subn(new_text, comment_processed_text)
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
    pattern = get_pattern_bracket_string()
    return apply_replace_to_matches(txt, pattern, convert_bracket_string)


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
    txt_arange = process_to_arange(txt_list)

    return txt_arange


def convert_m_2_py(m_filename):
    matlab_script = read_txt(m_filename)
    python_script = convert_matlab_2_python(matlab_script)
    write_txt(m_filename_2_py_filename(m_filename), python_script)


def get_pylab_name():
    return 'pylab', 'pl'


def get_signal_name():
    return 'scipy.signal', 'ss'


def get_control_name():
    return 'control', 'control'


def main(argv):
    if 1 < len(argv):
        convert_m_2_py(argv[1])


if __name__ == '__main__':
    main(sys.argv)
