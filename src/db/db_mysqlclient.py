import os

import MySQLdb
from MySQLdb.cursors import DictCursor


class MySQLClientConnector:
    def __init__(self, schema_nm, user_nm, password, host, port):
        self.conn = MySQLdb.connect(
            host=host,
            port=int(port),
            user=user_nm,
            password=password,
            db=schema_nm,
            charset='utf8mb4'
        )
        self.cursor = self.conn.cursor(DictCursor)

    def executemany(self, query=None, args=None):
        self.cursor.executemany(query, args)

    def execute(self, query=None, args=None):
        return self.cursor.execute(query, args)

    def fetchone(self, query=None, args=None):
        self.cursor.execute(query, args)
        return self.cursor.fetchone()

    def fetchall(self, query=None, args=None):
        self.cursor.execute(query, args)
        return self.cursor.fetchall()

    def commit(self):
        return self.conn.commit()

    def close(self):
        return self.conn.close()


if __name__ == '__main__':
    _db = MySQLClientConnector()
    print(_db.execute("SELECT 1"))
