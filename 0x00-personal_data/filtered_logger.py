#!/usr/bin/env python3
"""Doc of the module"""
import re
from typing import List
import logging
from mysql.connector import connect
import os
"""Doc of the import"""
PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


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
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.getMessage(), self.SEPARATOR)
        return super(RedactingFormatter, self).format(record)


def get_logger() -> logging.Logger:
    """This function compute"""
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    formater = RedactingFormatter(fields=PII_FIELDS)
    handler.setFormatter(formater)
    logger.addHandler(handler)
    return logger


def get_db():
    """This function permit to connect to mysql database"""
    USERNANE = os.getenv("PERSONAL_DATA_DB_USERNANE")
    PASSWORD = os.getenv("PERSONAL_DATA_DB_PASSWORD")
    HOST = os.getenv("PERSONAL_DATA_DB_HOST")
    DB_NAME = os.getenv("PERSONAL_DATA_DB_NAME")
    try:
        conn = connect(host=HOST, database=DB_NAME,
                       user=USERNANE, password=PASSWORD)
        return conn
    except Exception:
        pass
