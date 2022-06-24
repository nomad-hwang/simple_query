
from typing import Dict
from peewee import PeeweeException

from database.errors import DatabaseProgrammingError

def handle_exception(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except PeeweeException as e:    # TODO : handle specific exception
            raise DatabaseProgrammingError(e)
    return wrapper

@handle_exception
def parse_cursor(func):
    def wrapper(*args, **kwargs):
        return results_to_dict(func(*args, **kwargs))
    return wrapper

def results_to_dict(cursor):
    if cursor is None:
        raise DatabaseProgrammingError('cursor is null. It\'s likely a programming error')

    records = cursor.fetchall()
    if len(records) == 0:
        return []

    columns = [column[0] for column in cursor.description]
    return [dict(zip(columns, record)) for record in records]
