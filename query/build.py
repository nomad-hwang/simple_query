
from typing import Dict, List

from query.operator import Operator
from query.operator.comparison import Comparison
from query.operator.logical import AND, Logical

def insert(table, field_value: Dict[str, any]) -> str:
    fields, values = _separate_field_value(field_value)
    return f'INSERT INTO {table} ({fields}) VALUES ({values})'

def select(table, fields: List[str] = None, conditions: List[Operator]=None) -> str:
    w = _where(conditions, True)
    if w != '':
        w = ' ' + w

    if fields is None:
        return f'SELECT * FROM {table}{w}'
    return f'SELECT {",".join(fields)} FROM {table}{w}'

def update(table, field_value: Dict[str, any], conditions: List[Operator]):
    s = ''
    for fields, values in field_value.items():
        s += f'{fields} = {values}, '
    return f'UPDATE {table} SET {s[:-2]} {_where(conditions)}'

def delete(table, conditions: List[Operator]):
    return f'DELETE FROM {table} {_where(conditions)}'
   
####################################################################
####################################################################


def _separate_field_value(field_value: Dict[str, any]):
    if len(field_value) == 0:
        raise ValueError('field_value is empty')
    fields, values = '', ''
    for key, value in field_value.items():
        fields += f'{key}, '
        values += f'{value}, '
    return fields[:-2], values[:-2]

def _where(conditions: List[Operator], allow_empty: bool = False) -> str:
    if not _validate_condition(conditions):
        if allow_empty is False:
            raise ValueError('conditions is empty')
        return ''
    
    where = 'WHERE '
    for i, c in enumerate(conditions):
        if i % 2 == 0:
            where += str(c)
        else:
            where += ' ' + str(c) + ' '
    return where

def _validate_condition(conditions: List[Operator]):
    if conditions is None:
        return False
    if len(conditions) == 0:
        return False

    # even number only. 
    # since every Logical operator should place between two Comparison operators
    if len(conditions) % 2 == 0: 
        raise ValueError('conditions is invalid')

    # check if Logical operator is placed between two Comparison operators
    for i, c in enumerate(conditions):
        if i % 2 == 0:
            if not isinstance(c, Comparison):
                raise ValueError('conditions is invalid')
        else:
            if not isinstance(c, Logical):
                raise ValueError('conditions is invalid')
    return True
           