#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('/home/pi/smartfan/smartfandb')
c = conn.cursor()
c.execute('insert into t_sensor_logs(temperature,humidity) values(1337,108)')
conn.commit()
c.close()
