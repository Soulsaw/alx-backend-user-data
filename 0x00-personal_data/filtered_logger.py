#!/usr/bin/env python3
"""Doc of the module"""
import re
from typing import List
import logging
"""Doc of the import"""


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """This function returns the log message ofscustable"""
    pattern = '|'.join(f'{field}=[^{separator}]*' for field in fields)
    return re.sub(pattern, lambda m: m.group().split('=')[0] +
                  '=' + redaction, message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """This method permit to filter values in incomming log record"""
        record.message = filter_datum(self.fields, self.REDACTION,
                                      record.getMessage(), self.SEPARATOR)
        return super(RedactingFormatter, self).format(record)
