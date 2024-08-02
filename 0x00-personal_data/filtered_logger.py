import re


def filter_datum(fields, redaction, message, separator):
    pattern = '|'.join(f'{field}=[^;]*' for field in fields)
    return re.sub(pattern, lambda m: m.group().split('=')[0] +
                  '=' + redaction, message)
