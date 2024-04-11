#!/usr/bin/env python3
"""Module well documented"""
from typing import List
import re
"""Import doc in python"""


def filter_datum(fields: List[str], redaction: str, message: str, separator: str):
    """Doc of the filter function"""
    return re.sub(r'({})[^{}]+'.format(
        '|'.join(field + '=' for field in fields),
        separator), r'\1{}'.format(redaction), message)
