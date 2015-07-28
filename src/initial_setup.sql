CREATE DATABASE smartfandb;

\c smartfandb

CREATE TABLE t_sensor_logs(id SERIAL PRIMARY KEY, temperature INT NOT NULL, humidity INT NOT NULL, timestamp TEXT DEFAULT CURRENT_TIMESTAMP);

