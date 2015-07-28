#!/usr/bin/python

from __future__ import with_statement
from pysqlite2 import dbapi2 as sqlite3

def storeData(temp, humid):
    with sqlite3.connect("./smartfandb") as conn:
        conn.execute("INSERT INTO t_sensor_logs(temperature,humidity) VALUES(?,?)", (temp,humid,))

def getLastTrio():
    with sqlite3.connect("./smartfandb") as conn:
        conn.row_factory = sqlite3.Row
        list = []
        for row in conn.execute("SELECT * FROM (SELECT * FROM t_sensor_logs ORDER BY id DESC LIMIT 3) ORDER BY id ASC"):
            list.append({'temperature':row['temperature'], 'humidity':row['humidity'], 'timestamp':row['timestamp']})
        return list

def getLogsAfterTimestamp(timestamp):
    with sqlite3.connect("./smartfandb") as conn:
        conn.row_factory = sqlite3.Row
        list = []
        for row in conn.execute("SELECT * FROM t_sensor_logs WHERE timestamp > ? ORDER BY id", (timestamp,)):
            list.append({'temperature':row['temperature'], 'humidity':row['humidity'], 'timestamp':row['timestamp']})
        return list
