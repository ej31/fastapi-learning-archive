import datetime

import MySQLdb
from MySQLdb.cursors import DictCursor

from src.db.db_mysqlclient import MySQLClientConnector

if __name__ == '__main__':
    _db_conn = MySQLClientConnector(
        host="",
        port=0000,
        user_nm="",
        password="",
        schema_nm="",
    )

    q = """
        INSERT INTO user (name, password, nick, email, phone_num)
        VALUES (%s, %s, %s, %s, %s)
        """
    values = [
        ('고길동', 'p@sswoRd!^', 'GoGoGo', 'hoyhoy@gmail.com', '010-1414-1414'),
        ('김덕배', 'p@sswoRd!^', 'DuckShip', 'duckship@naver.com', '010-1111-2222')
    ]
    _db_conn.executemany(q, values)
    _db_conn.commit()

    q = """
    SELECT id, name, nick, email, phone_num, created_dt, updated_dt
    FROM user WHERE created_dt between %(start_dt)s and %(end_dt)s 
    """
    d = {
        # timedelta(days=1): 현재부터 하루를 뺀 시간을 반환
        "start_dt": datetime.timedelta(days=1),
        "end_dt": datetime.datetime.now()
    }
    # 쿼리 수행
    _db_conn.execute(q, d)

    # 수행 결과 가져오기
    _rows = _db_conn.fetchall()
    print(_rows)
