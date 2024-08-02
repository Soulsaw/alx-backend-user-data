#!/usr/bin/env python3
"""Doc of the module"""
import re
"""Doc of the import"""


def filter_datum(fields, redaction, message, separator):
    """Doc of the funxtion"""
    pattern = '|'.join(f'{field}=[^{separator}]*' for field in fields)
    return re.sub(pattern, lambda m: m.group().split('=')[0] +
                  '=' + redaction, message)
