#!/usr/bin/python

from __future__ import with_statement
from pysqlite2 import dbapi2 as sqlite3

def storeData(temp, humid):
    with sqlite3.connect("./smartfandb") as conn:
        conn.execute("insert into t_sensor_logs(temperature,humidity) values(%s,%s)", (temp,humid,))

def getLastTrio():
    with sqlite3.connect("./smartfandb") as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM t_sensor_logs ORDER BY id DESC LIMIT 3")
            return cur.fetchall()

def getLogsAfterTimestamp(timestamp):
    with sqlite3.connect("./smartfandb") as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM t_sensor_logs WHERE timestamp > %s ORDER BY id", (timestamp,))
            return cur.fetchall()
