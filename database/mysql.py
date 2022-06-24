
import atexit
from typing import Dict, List

from peewee import MySQLDatabase

from database import DatabaseInterface
from database.mysql_util import handle_exception, parse_cursor

class MySql(DatabaseInterface, MySQLDatabase):
    def __init__(self, host: str, port: int, user: str, password: str, database: str):
        self.host, self.port, self.user, self.password, self.database = host, port, user, password, database

        DatabaseInterface.__init__(self)
        MySQLDatabase.__init__(self, self.database, host=self.host, user=self.user, passwd=self.password, autoconnect=False)

        atexit.register(self.disconnect)

    @property
    def connected(self) -> bool:
        return MySQLDatabase.is_connection_usable(self)

    @handle_exception
    def connect(self):
        MySQLDatabase.connect(self)

    def disconnect(self):
        MySQLDatabase.close(self)

    @parse_cursor
    def query(self, query, *args, **kwargs):
        return MySQLDatabase.execute_sql(self, query, *args, **kwargs)