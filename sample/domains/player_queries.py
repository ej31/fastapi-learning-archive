from src.db.db_mysqlclient import MySQLClientConnector


def find_player_by_id(db: MySQLClientConnector, id: int):
    q = """SELECT * FROM player WHERE %(player_id)s"""
    d = {"player_id": id}
    return db.fetchone(q, d)

