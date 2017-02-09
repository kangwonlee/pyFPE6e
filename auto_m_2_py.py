import re


def get_pattern_semi_colon_followed_by_space():
    return re.compile(r';\s+')

