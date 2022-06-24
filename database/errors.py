
class DatabaseError(Exception):
    pass

class DatabaseConnectionError(DatabaseError):
    pass

class DatabaseProgrammingError(DatabaseError):
    pass

class DataNotFoundError(DatabaseError):
    """ 데이터가 없을 경우 발생하는 예외
    
    Read 할 때 데이터가 없을 경우에는 빈 []를 반환하나,
    그 외의 Update, Delete 할 때는 예외를 발생시킵니다.
    """
    pass