#!/usr/bin/env python3
"""Doc of the module"""
import re
from typing import List
import logging
import mysql.connector
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


def get_db() -> mysql.connector.connection.MySQLConnection:
    """This function permit to connect to mysql database"""
    db_username = os.getenv("PERSONAL_DATA_DB_USERNANE", 'root')
    db_password = os.getenv("PERSONAL_DATA_DB_PASSWORD", '')
    db_host = os.getenv("PERSONAL_DATA_DB_HOST", 'localhost')
    db_name = os.getenv("PERSONAL_DATA_DB_NAME", 'my_db')
    connection = mysql.connector.connection.MySQLConnection(
        user=db_username,
        password=db_password,
        host=db_host,
        database=db_name
    )
    return connection


def main():
    """This function permit to fetch data from the database"""
    logger = get_logger()
    db = get_db()
    cursor = db.cursor()
    cursor.execute('select * from users;')
    rows = cursor.fetchall()
    colums = [column[0] for column in cursor.description]
    all_rows = [dict(zip(colums, row)) for row in rows]
    for row in all_rows:
        filter = ';'.join(f"{key}={value}" for key, value in row.items())
        logger.info(filter)
    cursor.close()
    db.close()


if __name__ == "__main__":
    """Implementing the main"""
    main()
