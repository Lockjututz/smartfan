#! /bin/bash
sqlite3 -echo -bail smartfandb "CREATE TABLE t_sensor_logs(id INTEGER PRIMARY KEY NOT NULL, temperature INTEGER NOT NULL, humidity INTEGER NOT NULL, timestamp TEXT DEFAULT (datetime('now','localtime')));"
