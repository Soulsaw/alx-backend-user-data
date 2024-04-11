#!/usr/bin/env python3
"""Module well documented"""
from typing import List
import re
"""Import doc in python"""


def filter_datum(fds: List[str], redact: str, mes: str, sep: str):
    """Doc of the filter function"""
    return re.sub(r'({})[^{}]+'.format( '|'.join(f + '=' for f in fds),
                                       sep), r'\1{}'.format(redact), mes)
