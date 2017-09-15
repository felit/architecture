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


def batch_insert(total_num=1000, step=100):
    sql = """
        INSERT into orders(custom_id,price,created_time,updated_time)
        values(%s,%s,%s,%s)
    """
    conn, cursor = get_conn()
    for i in range(0, total_num, step):
        cursor.executemany(sql, [(j, j % 100 * random.random(), datetime.now(), datetime.now())
                                 for j in range(i * step, (i + 1) * step)])
        conn.commit()
    conn.close()


if __name__ == '__main__':
    batch_insert(total_num=100000, step=1000)

