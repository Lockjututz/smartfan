#!/usr/bin/python

from __future__ import with_statement
from pysqlite2 import dbapi2 as sqlite3

with sqlite3.connect("/home/pi/smartfan/smartfandb") as con:
    con.execute("insert into t_sensor_logs(temperature,humidity) values(1337,108)")
