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
