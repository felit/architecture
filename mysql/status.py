# -*- coding:utf8 -*-
import MySQLdb


def get_conn():
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='admin',
        db='nginx_logs',
    )
    cur = conn.cursor()
    return conn, cur


import random
from datetime import datetime


def status():
    sql = """
        select count(*) from orders
    """
    conn, cursor = get_conn()
    cursor.execute(sql)
    print cursor.fetchall()
    conn.close()


if __name__ == '__main__':
    status()

