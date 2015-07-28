#! /bin/bash
sqlite3 -echo -bail smartfandb 'CREATE TABLE t_sensor_logs(id INT PRIMARY KEY, temperature INT NOT NULL, humidity INT NOT NULL, timestamp TEXT DEFAULT CURRENT_TIMESTAMP);'