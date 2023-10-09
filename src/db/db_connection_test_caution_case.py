import datetime

import MySQLdb
from MySQLdb.cursors import DictCursor


def get_user_by_criteria(column_nm, value, password):
    conn = MySQLdb.connect(
        host="",
        port=3306,
        user="",
        password="",
        db="",
        charset='utf8mb4'
    )
    _cursor = conn.cursor(DictCursor)

    query = f"""
    SELECT * FROM user WHERE {column_nm} = {value} and password = {password}
    """
    print(query)
    _cursor.execute(query)
    return _cursor.fetchall()


if __name__ == '__main__':
    _result = get_user_by_criteria("name", "'1'; drop table user; commit; --", "p@sswoRd!^")
    print(_result)
