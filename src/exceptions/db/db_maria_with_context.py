import os
import pymysql


class MariaDBConnector:
    def __init__(self, host, port: int, user, password, database):
        self.host = host
        self.user = user
        self.port = port
        self.password = password
        self.database = database
        self.conn = None
        self.curs = None

    def __enter__(self):
        self.conn = pymysql.connect(
            host=self.host,
            user=self.user,
            port=self.port,
            password=self.password,
            database=self.database,
        )
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.close()

    def execute(self, query=None, args=None):
        if args is None:
            self.curs.execute(query)
        else:
            self.curs.execute(query, args)

    def executemany(self, query=None, args=None):
        self.curs.executemany(query, args)

    def execute_query(self, query):
        cursor = self.conn.cursor()
        cursor.execute(query)
        return cursor

    def fetchone(self, query=None, args=None):
        """
        query 조회 내용 중 한 건만 조회 할 경우
        Args:
            query: 입력 Query (sql_generator format : pyformat)
            args: sql_generator 입력 용 dictionary
        Returns:
            sql_generator 조회 결과
        """
        self.curs.execute(query, args)
        return self.curs.fetchone()

    def fetchall(self, query=None, args=None):
        self.curs.execute(query, args)
        return self.curs.fetchall()

    def commit(self):
        return self.conn.commit()

    def close(self):
        return self.conn.close()
